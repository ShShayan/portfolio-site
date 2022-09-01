from django.shortcuts import render
from .models import Job
from publication.models import Publication

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def CV(request):
    jobs = Job.objects
    pubs = Publication.objects
    return render(request, 'jobs/cv.html', {'jobs':jobs, 'pubs':pubs})

def portfolio(request):
    return render(request, 'jobs/portfolio.html')

def projects(request):
    return render(request, 'jobs/projects.html')

def contact(request):
    return render(request, 'jobs/contact.html')