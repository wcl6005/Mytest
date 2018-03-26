from django.contrib import admin
from polls.models import Poem
# Register your models here.

@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):    
    list_display = ('id','title','author')


#admin.site.register(Poem)