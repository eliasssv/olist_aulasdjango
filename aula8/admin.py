from django.contrib import admin
from .models import Pet
from .forms import PetForm

class PetAdmin(admin.ModelAdmin):
    fields = ('nome', 'data_nascimento', 'ativo')
    list_display = ('nome', 'data_nascimento', 'show_and_year', 'ativo')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    ordering = ('ativo',)
    form = PetForm

    def show_and_year(self, obj):
        return f"{obj.nome} {obj.data_nascimento}"

admin.site.register(Pet, PetAdmin)
