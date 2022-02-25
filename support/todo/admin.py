from django.contrib import admin
from .models import Todo

# Register our model и прописываем, что мы хотим видеть в админке при работе с нашей моделью

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','description', 'date', 'done',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title','description', 'date',)
    list_editable = ('done',)
    list_filter = ('done',)


admin.site.register(Todo, TodoAdmin)