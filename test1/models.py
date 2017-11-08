#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AdminManager(models.Model):
	content = models.TextField(verbose_name='内容')
	name = models.CharField(max_length=30,verbose_name='名字')
	age = models.IntegerField(verbose_name='年纪',default=18)
	image = models.ImageField(upload_to='images/%Y/%m')

	class Meta:
		verbose_name='内容管理'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.name
