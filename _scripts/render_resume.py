"""Render the CV with the same company logos used on the website."""

import subprocess
import sys
import re
from pathlib import Path

import yaml
from rendercv.renderer.pdf_png import get_typst_compiler


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / "_data/cv.yml"
    assets = root / "assets/rendercv"
    subprocess.run(
        [
            str(Path(sys.executable).with_name("rendercv")),
            "render",
            str(source),
            "--settings",
            str(assets / "settings.yaml"),
            "--design",
            str(assets / "design.yaml"),
            "--locale-catalog",
            str(assets / "locale.yaml"),
            "--dont-generate-pdf",
        ],
        cwd=root,
        check=True,
    )
    cv = yaml.safe_load(source.read_text())["cv"]
    organizations = yaml.safe_load((root / "_data/organizations.yml").read_text())
    output = assets / "rendercv_output"
    typst_file = output / (cv["name"].replace(" ", "_") + "_CV.typ")
    content = typst_file.read_text()
    profiles = {entry["network"]: entry["username"] for entry in cv["social_networks"]}
    contacts = [
        ("globe", cv["website"]),
        ("envelope", f"mailto:{cv['email']}"),
        ("linkedin", f"https://www.linkedin.com/in/{profiles['LinkedIn']}/"),
        ("x-twitter", f"https://x.com/{profiles['X']}"),
        ("github", f"https://github.com/{profiles['GitHub']}"),
    ]
    connections = "#connections(\n" + "\n".join(
        f'  [#link("{url}", icon: false)[#connection-with-icon("{icon}")[]]],'
        for icon, url in contacts
    ) + "\n)"
    content, count = re.subn(r"#connections\(\n.*?\n\)", lambda _: connections, content, count=1, flags=re.S)
    if count != 1:
        raise ValueError("Expected one résumé contact block")
    for entry in cv["sections"]["Experience"]:
        company = entry["company"]
        logo = organizations[company]["logo"]
        if not (root / logo.lstrip("/")).is_file():
            raise FileNotFoundError(logo)
        heading = f"#strong[{company}]"
        if content.count(heading) != 1:
            raise ValueError(f"Expected one company heading for {company}")
        image = (
            '#box(inset: 2pt, fill: white, radius: 2pt, baseline: 20%)['
            f'#image("{logo}", width: 14pt, height: 14pt, fit: "contain")] '
        )
        content = content.replace(heading, image + heading)
    typst_file.write_text(content)
    # Use the repository root so Typst can read assets/img without copying logos.
    compiler = get_typst_compiler(source, root)
    pdf_file = typst_file.with_suffix(".pdf")
    compiler.compile(input=typst_file, format="pdf", output=pdf_file)
    print(f"Rendered {pdf_file}")


if __name__ == "__main__":
    main()
