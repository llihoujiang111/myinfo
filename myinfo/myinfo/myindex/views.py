from django.shortcuts import render
from myindex.models import Article_my

# Create your views here.
def my_index(request):
    artall = Article_my.objects.all()
    context = {
        'artall': artall
    }
    return render(request , 'myboke/lw-index.html' , context=context)



def show_articlelist(request):
    artall=Article_my.objects.all()
    context={
        'artall':artall
    }
    return render(request,'myboke/lw-index-noslider.html',context=context)

def show_article(request,id):
    artall=Article_my.objects.get(pk=id)
    context={
        'artall':artall
    }
    return render(request,'myboke/lw-article-fullwidth.html',context=context)

def timeshow(request):
    artall=Article_my.objects.all()
    context={
        'artall':artall
    }
    return render(request,'myboke/lw-timeline.html',context=context)


def imgshow(request):
    artall=Article_my.objects.all()
    context={
        'artall':artall
    }
    return render(request,'myboke/lw-img.html',context=context)