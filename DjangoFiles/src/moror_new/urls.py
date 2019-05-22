"""moror_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from index.views import moror_index,ser_pg, brnd_pg, ba_pg, sur_pg, sm_mrkt_pg, FB_mrkt_pg, insta_mrkt_pg,utube_mrkt_pg,twitter_mrkt_pg,sm_lead_mrkt_pg,video_pg,web_videos_pg
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    #url('', moror_index),
    path('', moror_index,name='home'),
    path('service_page_franchisee_distributor/',ser_pg,name='service'),
    path('Service_page_BRAND_MANAGEMENT/',brnd_pg,name='brand'),
    path('Service_page_BRAND_ANALYSIS/',ba_pg,name='BA'),
    path('survey/',sur_pg,name='survey'),
    path('social_media_marketing_and_contest/',sm_mrkt_pg,name='social_media'),
    path('facebook_marketing_and_contest/',FB_mrkt_pg,name='Facebook'),
    path('instagram_marketing_and_contest/',insta_mrkt_pg,name='Instagram'),
    path('youtube_marketing_and_contest/',utube_mrkt_pg,name='Youtube'),
    path('twitter_marketing_and_contest/',twitter_mrkt_pg,name='Twitter'),
    path('social_media_lead_generation/',sm_lead_mrkt_pg,name='SM_lead_generation'),
    path('what_we_do/',video_pg,name='Video_content'),
    path('web/',web_videos_pg,name='Web_Videos'),
]
