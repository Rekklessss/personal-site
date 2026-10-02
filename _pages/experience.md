---
layout: page
title: experience
permalink: /experience/
description: Software engineering, open-source work, and competitive experience.
nav: true
nav_order: 3
---

{% for role in site.data.experience %}

<section class="experience-entry">
  <div class="experience-heading">
    <h2 class="organization-name">{% include organization_logo.liquid company=role.company %} {{ role.company }}</h2>
    <div class="experience-meta">
      {% if role.start_date %}<span>{{ role.start_date | append: '-01' | date: '%b %Y' }} – {{ role.end_date | append: '-01' | date: '%b %Y' }}</span>{% endif %}
      {% if role.location %}<span class="experience-location">{{ role.location }}</span>{% endif %}
    </div>
  </div>
  <p class="experience-role">{{ role.position }}</p>
  {% if role.summary %}<p>{{ role.summary }}</p>{% endif %}
  {% if role.highlights %}
  <ul class="experience-highlights">
    {% for highlight in role.highlights %}
    <li>{{ highlight }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</section>
{% endfor %}

## Education and community

I completed my B.Tech in Computer Science and Engineering at **SRM Institute of Science and Technology in 2025**, with a final **CGPA of 8.5/10**. I also collaborated with student developers through Think Digital.

Before university, I was a school sports captain and competed in swimming at national and inter-state events. I completed grade 10 at an ICSE school in 2019.
