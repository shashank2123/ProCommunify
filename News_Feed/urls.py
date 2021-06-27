from django.urls import path
from News_Feed import views

app_name = 'News_Feed'

urlpatterns = [
	path('',views.News_Feed_View.as_view(),name='news_feed_url')
]