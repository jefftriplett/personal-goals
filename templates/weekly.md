---
---
# This Week's Accomplishments: {{ date.strftime('%B %d, %Y') }}

## Things I Did From the List ([Resources](resources.md))

{% if daily %}### Daily Goals
{% for task in daily %}
- [ ] {{ task.name }}{% endfor %}{% endif %}

{% if weekly %}### Weekly Goals
{% for task in weekly %}
- [ ] {{ task.name }}{% endfor %}{% endif %}

{% if monthly %}### Monthly Goals
{% for task in monthly %}
- [ ] {{ task.name }}{% endfor %}{% endif %}

{% if quarterly %}### Quarterly Goals
{% for task in quarterly %}
- [ ] {{ task.name }}{% endfor %}{% endif %}

## Additional Things I Did

## Things I Didn't Get To / Finish

## Things I'll Do Next Week

## Week In Review
