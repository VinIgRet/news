from django.urls import path
from news.views import index, getcat,getnews,addnews

urlpatterns = [
    path('', index, name='allnews'),
    path("cat/<int:catid>/", getcat, name="catnews"),
    path("news/<int:newsid>/", getnews, name="newsdetail"),
    path("news/add", addnews, name="addnews"),
]