---
layout: default
title: Educational resources
nav_order: 3
---

{% include resource-styles.html %}

# Educational resources
These are resources of educational value, and reference materials.

{% assign items = site.data.foinse | where: "type", "educational-resource" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
