---
layout: default
title: Creative Resources
nav_order: 9.5
---

{% include resource-styles.html %}

# Creative Resources
Resources for creative work in Irish.

{% assign items = site.data.foinse | where: "type", "creative-resource" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
