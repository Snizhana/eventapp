from django.contrib import admin

from application.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields if f.name != 'is_accepted']

admin.site.register(Application, ApplicationAdmin)
