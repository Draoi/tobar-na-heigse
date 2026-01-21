---
layout: default
title: Blogs
nav_order: 9
---

{% include resource-styles.html %}

# Blogs
Various blogs in or about Irish dialects.

{% assign items = site.data.foinse | where: "type", "blog" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
