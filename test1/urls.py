#encoding:utf-8
from django.conf.urls import url
from .views import index,upload_files


#http://127.0.0.1:8001/static/js/kindeditor/php/upload_json.php?dir=image
urlpatterns = [
    url(r'^index',index),
    url(r'^upload_files',upload_files)
]