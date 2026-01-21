---
layout: default
title: Historical
parent: Browse by dialect
nav_order: 5
---

{% include resource-styles.html %}

{% assign items = site.data.foinse | where_exp: "item", "item.dialect contains 'Historical'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
