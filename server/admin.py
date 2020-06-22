from django.contrib import admin

# Register your models here.
from simple_sso.sso_server.models import Consumer

admin.site.register(Consumer)
