from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from . models import Projects
from . forms import ProjectsForm


def assembly(request):
	return render(request, 'dashboard/assembly.html')


def koose(request):
	return render(request, 'dashboard/koose.html')

def sutsrunaa(request):
	return render(request, 'dashboard/sutsrunaa.html')

def gbentanaa(request):
	return render(request, 'dashboard/gbentanaa.html')

def nii(request):
	return render(request, 'dashboard/nii.html')

def projects(request):
	media = Projects.objects.all()
	context = {'media': media}
	return render(request, 'dashboard/projects.html', context)