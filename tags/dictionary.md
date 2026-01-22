---
layout: default
title: Dictionary
parent: Browse by tags
nav_order: 21
---

{% include resource-styles.html %}

{% assign items = site.data.foinse | where_exp: "item", "item.tags contains 'Dictionary'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
