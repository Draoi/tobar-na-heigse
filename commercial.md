---
layout: default
title: Commercial
nav_order: 10
---

{% include resource-styles.html %}

# Commercial
Commercial entities related to Irish.

{% assign items = site.data.foinse | where: "type", "commercial" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
