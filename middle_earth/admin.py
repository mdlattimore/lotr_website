from django.contrib import admin
from .models import Verses, Characters
# Register your models here.

class VersesAdmin(admin.ModelAdmin):
    list_filter = ["book", "speaker"]
    list_display = ("book", "speaker", "short_text")
    ordering = ("book", "sub_book", "chapter", "page", "speaker",)
    readonly_fields = ('id',)

    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text


class CharactersAdmin(admin.ModelAdmin):
    list_filter = ['name', 'race']
    list_display = ('name', 'race')
    ordering = ('name',)
    readonly_fields = ('id',)


admin.site.register(Verses, VersesAdmin)
admin.site.register(Characters, CharactersAdmin)
