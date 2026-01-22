---
layout: default
title: Linguistic
parent: Browse by tags
nav_order: 39
---

{% include resource-styles.html %}

{% assign items = site.data.foinse | where_exp: "item", "item.tags contains 'Linguistic'" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
