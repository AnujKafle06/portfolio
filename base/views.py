from django.shortcuts import render, redirect
from. models import Skill, Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import FileResponse, Http404
import os

# Create your views here.
def home(request): 
    fetch= Skill.objects.all()
    project = Project.objects.all()
    context={
        "fetch" : fetch,
        "project" : project
    }

    return render(request, 'base/index.html', context=context)

def contactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            subject = f"New message from {cd['name']}"
            purpose = cd['purpose']
            from_email = cd['email']
            recipient_list = ['kaflea063@gmail.com']  # Your Gmail

            send_mail(subject, purpose, from_email, recipient_list)

            return redirect('Home')
    else:
        form = ContactForm()

    context = {
        "form": form
    }
    return render(request, 'base/contact.html', context)

def view_pdf(request):
    File_path =os.path.join('static/files', 'Anuj Kafle-cv.pdf')
    try:
        return FileResponse(open(File_path,'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("PDf Not Found! ")

def projectPage(request, id):
    project =Project.objects.get(id=id)
    context={
        "project": project
    }
    return render(request, 'base/project.html', context)


