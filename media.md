---
layout: default
title: Media
nav_order: 6
---

{% include resource-styles.html %}

# Media
Various Irish-medium media outlets and accounts.

{% assign media_items = site.data.foinse | where: "type", "media" %}

## News
{% assign news_items = media_items | where_exp: "item", "item.tags contains 'News'" | sort: "name" %}
<div class="resource-list">
{% for item in news_items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>

## Radio
{% assign radio_items = media_items | where_exp: "item", "item.tags contains 'Radio'" | sort: "name" %}
<div class="resource-list">
{% for item in radio_items %}
  {% include resource-entry.html item=item %}
{% endfor %}
</div>

## Social
Social media accounts and personalities associated with Irish. As there are many individuals spread across many networks I have generally posted one entry per individual, as it is possible to find their other accounts on other platforms easily.

{% assign social_items = media_items | where_exp: "item", "item.tags contains 'Social'" | sort: "name" %}
<div class="resource-list">
{% for item in social_items %}
  {% include resource-entry.html item=item show_host=true %}
{% endfor %}
</div>
