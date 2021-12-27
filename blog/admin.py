from django.contrib import admin
from .models import Article
from .models import Category
from .models import Tag

admin.site.register([Article,Category,Tag]) 
