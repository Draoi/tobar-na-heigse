---
layout: default
title: Ulster
parent: Browse by dialect
nav_order: 4
---

{% include resource-styles.html %}

{% assign items = site.data.foinse | where_exp: "item", "item.dialect contains 'Ulster'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
