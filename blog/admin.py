from django.contrib import admin
from .models import Article, Author
from .models import Category
from .models import Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display =["title","slug","state","category","created"]
    list_filter = ["state","category"]
  
class AuthorAdmin(admin.ModelAdmin):
    list_display =["name","slug","state","created"]
    list_filter = ["state"]  

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register([Category,Tag]) 
