from django.contrib import admin
from django.contrib.auth.models import User
from .models import Reserva,Material,Sala
# Register your models here.


class ReservaInline(admin.StackedInline):
	model = Reserva
	extra=3

class MaterialInline(admin.StackedInline):
	model = Material
	extra=3

class UserAdmin(admin.ModelAdmin):
	exlude=[]
	inlines = [ReservaInline]

class ReservaAdmin(admin.ModelAdmin):
	exlude=[]
	list_display=('user_f','reserva_date','show_material')
class MaterialAdmin(admin.ModelAdmin):
	exlude=[]
	list_display=('sala_f','text_material')
class SalaAdmin(admin.ModelAdmin):
	exlude=[]
	inlines = [MaterialInline]


admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Material,MaterialAdmin)
admin.site.register(Sala,SalaAdmin)