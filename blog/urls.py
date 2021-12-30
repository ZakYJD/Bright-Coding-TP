from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name="list_of_articles"),
    path('<slug:slug>/',views.show, name="show_article"),
    path('edit/<int:id>/',views.edit, name="edit_article"),
    path('create/',views.create, name="create_article"),
    path('delete/<int:id>/',views.delete, name="delete_article"),
    path('author/<slug:slug>/',views.articles_by_author, name="show_articles_by_author"),
    path('category/<str:category>',views.articles_by_category,name="show_articles_by_category"),
    path('tag/<str:tag>',views.articles_by_tag,name="show_articles_by_tag")
] 