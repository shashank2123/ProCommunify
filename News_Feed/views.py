from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class News_Feed_View(TemplateView):
	template_name = "News_Feed/News_Feed_Page.html"