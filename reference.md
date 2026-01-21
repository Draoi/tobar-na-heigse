---
layout: default
title: Reference
nav_order: 4
---

{% include resource-styles.html %}

# Reference
Reference materials including important dictionaries.

{% assign items = site.data.foinse | where: "type", "reference" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
