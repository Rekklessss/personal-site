---
layout: page
permalink: /blog/
title: blog
nav: true
nav_order: 4
---

{% if site.posts.size > 0 %}
{% for post in site.posts %}

<article class="writing-entry">
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p>{{ post.description }}</p>
</article>
{% endfor %}
{% else %}
<div class="blog-empty" role="status">
  <i class="fa-regular fa-pen-to-square" aria-hidden="true"></i>
  <h2>No posts yet</h2>
  <p>Notes on LLMs, systems, and performance will appear here.</p>
</div>
{% endif %}
