from django.shortcuts import render
def moror_index(request):
    template_name='index.html'
    #context={}
    return render(request,template_name)

def ser_pg(request):
    template_name='sp_fr_dist.html'
    return render(request,template_name)    

def brnd_pg(request):
    template_name='sp_brnd_mngmt.html'
    return render(request,template_name)     

def ba_pg(request):
    template_name='sp_BA.html'
    return render(request,template_name)    

def sur_pg(request):
    template_name='survey.html'
    return render(request,template_name)

def sm_mrkt_pg(request):
    template_name='sm_marketing.html'
    return render(request,template_name)    

def FB_mrkt_pg(request):
    template_name='FB_marketing.html'
    return render(request,template_name)       

def insta_mrkt_pg(request):
    template_name='Insta_marketing.html'
    return render(request,template_name)     

def utube_mrkt_pg(request):
    template_name='utube_marketing.html'
    return render(request,template_name)

def twitter_mrkt_pg(request):
    template_name='twitter_marketing.html'
    return render(request,template_name)    

def sm_lead_mrkt_pg(request):
    template_name='sm_lead_generation.html'
    return render(request,template_name)    

def video_pg(request):
    template_name='video.html'
    return render(request,template_name)  

def web_videos_pg(request):
    template_name='web_videos.html'
    return render(request,template_name)

# Create your views here.
