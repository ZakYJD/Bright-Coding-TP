from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, SlugField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils.text import slugify

LIST_STATE=((0,"Disable"),(1,"Enable")) 

# Tag Model
class Tag(models.Model):
    name=CharField(max_length=20,unique=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):

    name=CharField(max_length=30,unique=True)
    state=IntegerField(default=0, choices=LIST_STATE)      
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#Author Model
class Author(models.Model):
    name = CharField(max_length=30)        
    profile = TextField(null=True)
    picture = models.ImageField(null=True,upload_to="authors")
    profile_picture = models.ImageField(null=True,upload_to="authors")
    state = IntegerField(default=0, choices=LIST_STATE)  
    slug = SlugField(max_length=40, unique= True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        super().save(*args, **kwargs)   


# Article Model
class Article(models.Model):
    title = CharField(max_length=120)
    author = ForeignKey(Author,null=True,on_delete=models.SET_NULL)
    state = IntegerField(default=0, choices=LIST_STATE)
    category = ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    tags = ManyToManyField(Tag)
    slug = SlugField(max_length=120, unique= True, db_index=True,null=True, blank=True)
    picture = models.ImageField(null=True,upload_to="articles")
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args, **kwargs)

 