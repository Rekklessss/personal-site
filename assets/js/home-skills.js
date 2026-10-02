document.querySelectorAll("[data-skills-widget]").forEach((widget) => {
  const buttons = [...widget.querySelectorAll(".skill-filter")];
  const skills = [...widget.querySelectorAll(".skill-chip")];
  const status = widget.querySelector(".skills-status");
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const category = button.dataset.category;
      buttons.forEach((filter) => filter.setAttribute("aria-pressed", String(filter === button)));
      let visible = 0;
      skills.forEach((skill) => {
        skill.hidden = category === "core" ? skill.dataset.core !== "true" : category !== "all" && skill.dataset.category !== category;
        if (!skill.hidden) visible += 1;
      });
      status.textContent = `Showing ${visible} skills`;
    });
  });
});
