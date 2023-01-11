from django.contrib import admin

from .models import Categories, Tags, Articles, Toc

# Register your models here.

admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Articles)
admin.site.register(Toc)
