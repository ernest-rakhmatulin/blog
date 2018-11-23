from django.contrib import admin
from .models import Request, Rule, Profile

admin.site.register(Request)
admin.site.register(Rule)
admin.site.register(Profile)

