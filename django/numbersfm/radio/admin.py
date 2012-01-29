from django.contrib import admin
from models import Show


class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Show, ShowAdmin)
