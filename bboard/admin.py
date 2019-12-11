from django.contrib import admin

from .models import Bb
from .models import Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')  # имена в списки записей
    list_display_links = ('title', 'content')                  # в гиперсылки на стр правки записи
    search_fields = ('title', 'content')                       # по которым выполн фильтр


admin.site.register(Bb, BbAdmin)  # регист своего прилож и модели
admin.site.register(Rubric)
