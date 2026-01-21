---
layout: default
title: Institutions
nav_order: 8
---

{% include resource-styles.html %}

# Institutions
Institutions involved with Irish.

{% assign items = site.data.foinse | where: "type", "institution" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
