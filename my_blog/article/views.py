from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import ArticlePost 

def article_list(request):
    # return HttpResponse("Hello World!")
    # 取出所有博客文章
    articles=ArticlePost.objects.all()
    context={"articles":articles}
    return render(request,'article/list.html',context)

# 文章详情
import markdown

def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])

    context = { 'article': article }
    return render(request, 'article/detail.html', context)