from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_url = "/index"
admin.site.register(Secretaria)
admin.site.register(AreaInteresse)
admin.site.register(Sugestoes)
admin.site.register(Questao)
admin.site.register(PalavrasChave)
admin.site.register(Novidade)