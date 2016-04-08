---
Date: 03/08/2016
Title: Django `UserPassesTestMixin`
Categories:
 - Django
Tags:
 - python
 - django
 - mixins
---

# Django `UserPassesTestMixin`

I stumbled on [`django.contrib.auth.mixins.UserPassesTestMixin`](https://docs.djangoproject.com/en/1.9/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin) while helping a friend out with a quick code review. While the `test_func` feels weird at first, but it's a useful alternative to writing a bunch of one-off decorators.
