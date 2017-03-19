from django.conf.urls import url, include
# from django.views.decorators.csrf import csrf_exempt
from . import views 

urlpatterns = [
	url(r'show-teachers/$', views.show_all_teachers, name='show-teachers'),
	url(r'get-teachers/(?P<isPractical>[\w-]+)/$', views.get_teachers, name='get-teachers'),
	url(r'save-feedback/$', views.save_feedback, name='save-feedback'),
	url(r'get-one-teacher/(?P<teacher_name>[\w ]+)/$', views.get_one_teacher, name='get-one-teacher'),
	url(r'$', views.index, name='index'),
]