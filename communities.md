---
layout: default
title: Communities
nav_order: 5
---

{% include resource-styles.html %}

# Communities
These are communities where you can use your Irish.

{% assign community_items = site.data.foinse | where: "type", "community" %}

## Physical
{% assign physical_items = community_items | where_exp: "item", "item.tags contains 'Physical'" | sort: "name" %}
<div class="resource-list">
{% for item in physical_items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>

## Online
{% assign online_items = community_items | where_exp: "item", "item.tags contains 'Online'" | sort: "name" %}
<div class="resource-list">
{% for item in online_items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>

## Language Planning Areas
{% assign lpa_items = community_items | where_exp: "item", "item.tags contains 'Language Planning Area'" | sort: "name" %}
<div class="resource-list">
{% for item in lpa_items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>
