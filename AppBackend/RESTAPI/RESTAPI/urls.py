"""RESTAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from APIapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^api/topContribFollowers', views.topContribFollowerData.as_view()),
    url(r'^tweetclf/predict', views.tweetclf.as_view()),
    url(r'^api/commitData', views.commit52.as_view()),
    url(r'^api/starGrowth', views.starGrowth.as_view()),
    url(r'^api/totalStars', views.totalStars.as_view()),
    url(r'^api/summarizerEngine', views.summarizerEngine.as_view()),
    url(r'^api/ghubtrending', views.ghubTrending.as_view()),
    url(r'^api/getMarketMap', views.MarketMap.as_view()),

]
