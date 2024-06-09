from django.urls import path
from .views import index,getprof,gethumans,addperson

urlpatterns = [
    path('', index, name='allhumans'),
    path('prof/<int:profid>', getprof, name='profhumans'),
    path('humans/<int:humansid>', gethumans, name='humansdetail'),
    path("humans/add", addperson, name="addperson"),
]