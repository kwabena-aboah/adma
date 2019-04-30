from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
	path('assembly/', views.assembly, name='assembly'),
	path('koose/', views.koose, name='koose'),
	path('sutsrunaa/', views.sutsrunaa, name='sutsrunaa'),
	path('gbentanaa/', views.gbentanaa, name='gbentanaa'),
	path('nii/', views.nii, name='nii'),
]