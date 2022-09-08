from django.shortcuts import render
from .models import Job
from publication.models import Publication
from comments.models import Comment

def home(request):
    return render(request, 'jobs/home.html', {'title':'home'})

def CV(request):
    jobs = Job.objects
    pubs = Publication.objects
    return render(request, 'jobs/cv.html', {'jobs':jobs, 'pubs':pubs, 'title':'CV'})

def portfolio(request):
    return render(request, 'jobs/portfolio.html', {'title':'portfolio'})

def projects(request):
    return render(request, 'jobs/projects.html', {'title':'projects'})

def contact(request):
    if request.method == 'POST':
        # User has info and wants to send them!
        if request.POST['comment'] == '':
            return render(request, 'jobs/contact.html',  {'error':'Please input text for your message to be sent.'})
        else:
            e = 'not provided'
            com = Comment()
            com.text = request.POST['comment']
            if request.POST['email'] == '':
                com.email = e
            else:
                com.email = request.POST['email']
            if request.POST['author'] == '':
                com.name = e
            else:
                com.name = request.POST['author']
            if request.POST['subject'] == '':
                com.subject = e
            else:
                com.subject = request.POST['subject']
            com.save()
            return render(request, 'jobs/contact.html',  {'msg':'Your message has been send successfully!'})
    else:
        return render(request, 'jobs/contact.html', {'title':'contact'})

def arch_portfolio(request):
    return render(request, 'jobs/arch-portfolio.html', {'title':'portfolio'})

def energy_portfolio(request):
    return render(request, 'jobs/energy-portfolio.html', {'title':'portfolio'})

def web_portfolio(request):
    return render(request, 'jobs/web-portfolio.html', {'title':'portfolio'})

def photo_portfolio(request):
    return render(request, 'jobs/photo-portfolio.html', {'title':'portfolio'})