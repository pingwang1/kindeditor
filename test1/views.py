#encoding:utf-8
import os
from django.shortcuts import render,HttpResponse
from django.conf import settings
from .models import *

# Create your views here.
def index(request):
	return render(request,'test1/index.html')

def upload_files(request):
	print 111
	if request.method=="POST":
		# print request.POST
		# print type(request.POST)
		pic = request.FILES['picture']
		# content = request.
		print("debug1==%s"%request.FILES)
		print("debug2==%s" % request.POST)
		#保存路径
		img = AdminManager()
		img.name=request.POST['name']
		img.content=request.POST['content']
		img.image=pic
		img.save()
		#保存文件
		# pic_path = os.path.join(settings.MEDIA_ROOT, str(pic))
		# with open(pic_path,'wb+') as f:
		# 	f.write(str(pic))
		return HttpResponse(AdminManager.objects.all())