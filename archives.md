---
layout: default
title: Archives
nav_order: 7
---

{% include resource-styles.html %}

# Archives
Various archives of Irish-related materials.

{% assign items = site.data.foinse | where: "type", "archive" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
