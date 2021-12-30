from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, Author, Category, Tag
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles=Article.objects.filter(state=1)   
    categories=Category.objects.filter(state=1)
    authors=Author.objects.filter(state=1)
    return render(request,"blog/index.html",
    {
        "articles":articles,
        "categories":categories,
        "authors":authors
    }
    )

def show(request, slug):
    article=get_object_or_404(Article,slug=slug)
    categories=Category.objects.filter(state=1)
    authors=Author.objects.filter(state=1)
    return render(request,"blog/show.html",
    {
        "article":article,
        "categories":categories,
        "authors":authors
    })

def articles_by_author(request, slug):
    author=Author.objects.get(slug=slug)
    articles=Article.objects.filter(author=author.id,state=1)
    categories=Category.objects.filter(state=1)
    authors=Author.objects.filter(state=1)
    return render(request,"blog/articles_by_author.html",
    {
        "author":author,
        "articles":articles,
        "categories":categories,
        "authors":authors
    }
    )

def articles_by_category(request,category):
    ctg_id=Category.objects.get(name=category).id
    articles=Article.objects.filter(state=1,category=ctg_id) 
    categories=Category.objects.filter(state=1)
    authors=Author.objects.filter(state=1)
    return render(request,"blog/articles_by_category.html",
    {
        "category":category,
        "articles":articles,
        "categories":categories,
        "authors":authors
    }
    )   

def articles_by_tag(request,tag):
    tg = Tag.objects.get(name=tag)
    articles=tg.article_set.all() 
    categories=Category.objects.filter(state=1)
    authors=Author.objects.filter(state=1)
    return render(request,"blog/articles_by_tag.html",
    {
        "tag":tag,
        "articles":articles,
        "categories":categories,
        "authors":authors
    }
    ) 
    

def edit(request, id):
    article=Article.objects.get(pk=id)

    if request.method == 'POST':
        form=ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect("list_of_articles")

    form= ArticleForm(instance=article)
    return render(request,"blog/edit.html",{"form":form})

def create(request):
    form= ArticleForm
    if request.method == 'POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_of_articles")
    return render(request,"blog/create.html",{"form":form})

def delete(request, id):
    article=Article.objects.get(pk=id)
    if request.method == 'POST':
        article.delete()
        return redirect("list_of_articles")
    return render(request,"blog/delete.html",{"article":article})

