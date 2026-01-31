---
layout: default
title: Textbooks
nav_order: 3
---

{% include resource-styles.html %}

<style>
  .book-entry .resource-title span {
    font-weight: 600;
    font-size: 1.05rem;
  }

  .book-meta {
    margin: 6px 0 8px;
    color: #c7cdd8;
    font-size: 0.9rem;
  }

  .book-meta-label {
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.7rem;
    color: #9aa3af;
    margin-right: 6px;
  }

  .book-links {
    margin: 8px 0 0;
  }

  .book-link-list {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 4px;
  }

  .book-link-list.book-link-list--stacked {
    flex-direction: column;
    gap: 4px;
  }

  .book-link-list a {
    font-size: 0.85rem;
  }
</style>

# Textbooks
Textbooks for learning Irish.

## Beginner
{% assign items = site.data.leabhair | where: "level", "Beginner" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include book-entry.html item=item %}
{% endfor %}
</div>

## Intermediate
{% assign items = site.data.leabhair | where: "level", "Intermediate" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include book-entry.html item=item %}
{% endfor %}
</div>

## Advanced
{% assign items = site.data.leabhair | where: "level", "Advanced" | sort: "name" %}
<div class="resource-list">
{% for item in items %}
  {% include book-entry.html item=item %}
{% endfor %}
</div>
