"""myinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from myindex.views import my_index, show_articlelist, show_article, timeshow, imgshow

urlpatterns = [
    url(r'^index/$', my_index,name='首页'),
    url(r'^articlelist/$', show_articlelist,name='展示列表'),
    url(r'^article/(?P<id>\d+)$', show_article,name='展示'),
    url(r'^time/$', timeshow,name='时光'),
    url(r'^img/$', imgshow,name='照片'),
]
