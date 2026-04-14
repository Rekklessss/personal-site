---
layout: page
title: projects
permalink: /projects/
description: Case studies, experiments, and products I have worked on.
nav: true
nav_order: 2
---

<div class="projects">
{% assign sorted_projects = site.projects | sort: "importance" %}

{% if sorted_projects.size > 0 %}

  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
{% else %}
  <div class="card mt-3 p-4">
    <h3 class="card-title">Projects are coming soon</h3>
    <p class="card-text">
      I’m curating a few project write-ups for this section. Until then, you can browse my
      <a href="{{ '/repositories/' | relative_url }}">GitHub repositories</a>.
    </p>
  </div>
{% endif %}
</div>
