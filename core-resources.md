---
layout: default
title: Core resources
nav_order: 2
---

{% include resource-styles.html %}

# Core resources
The most valuable learning resources online.

{% assign items = site.data.foinse | where_exp: "item", "item.tags contains 'Core'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
