---
layout: default
title: Oriel
parent: Browse by tags
nav_order: 51
---

{% include resource-styles.html %}

{% assign items = site.data.foinse | where_exp: "item", "item.tags contains 'Oriel'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
