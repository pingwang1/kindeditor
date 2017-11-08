#encoding:utf-8
from django.contrib import admin
from .models import *
# Register your models here.
class ContentManager(admin.ModelAdmin):

	class Media:
		js = (
			'/static/js/kindeditor/kindeditor.js',
			'/static/js/kindeditor/kindeditor-all.js',
			'/static/js/kindeditor/conf.js',#自己定义的配置文件
		)
admin.site.register(AdminManager,ContentManager)