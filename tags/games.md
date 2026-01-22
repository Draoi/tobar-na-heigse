---
layout: default
title: Games
parent: Browse by tags
nav_order: 32
---

{% include resource-styles.html %}

{% assign items = site.data.foinse | where_exp: "item", "item.tags contains 'Games'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
