from django.contrib import admin
from interface_app.models import TestCase


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'module', 'status'
    ,'url', 'method', 'header', 'parameter_type', 'parameter_body', 
    'response_assert', 'create_user']


admin.site.register(TestCase, TestCaseAdmin)
