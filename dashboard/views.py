from django.shortcuts import render


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