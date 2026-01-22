---
layout: default
title: Research
parent: Browse by tags
nav_order: 57
---

{% include resource-styles.html %}

{% assign items = site.data.foinse | where_exp: "item", "item.tags contains 'Research'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
