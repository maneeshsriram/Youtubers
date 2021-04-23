from django.shortcuts import render
from .models import Slider, Team, aboutData, HeaderData
from youtubers.models import Youtuber


# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    all_youtubers = Youtuber.objects.order_by('created_date')
    featured_youtubers = Youtuber.objects.order_by(
        '-created_date').filter(is_featured=True)
    header_data = HeaderData.objects.first()
    data = {
        'sliders': sliders,
        'teams': teams,
        'all_youtubers': all_youtubers,
        'featured_youtubers': featured_youtubers,
        'headerData': header_data
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    teams = Team.objects.all()
    about_data = aboutData.objects.first()
    header_data = HeaderData.objects.first()
    data = {
        'teams': teams,
        'aboutData': about_data,
        'headerData': header_data
    }
    return render(request, 'webpages/about.html', data)


def contact(request):
    header_data = HeaderData.objects.first()
    data = {
        'headerData': header_data
    }
    return render(request, 'webpages/contact.html', data)
