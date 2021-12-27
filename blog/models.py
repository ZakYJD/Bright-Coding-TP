from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField

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

# Article Model
class Article(models.Model):
    title = CharField(max_length=120)
    state = IntegerField(default=0, choices=LIST_STATE)
    category = ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    tags = ManyToManyField(Tag)
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

