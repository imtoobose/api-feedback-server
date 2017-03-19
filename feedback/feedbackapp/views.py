from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect, csrf_exempt
# from django.core.serializers import json
import json
from django.http import HttpResponse, JsonResponse
from .models import Teacher
# Create your views here.

def index(request):
	print 'HERE'
	return HttpResponse('hello')


# @csrf_exempt
def save_feedback(request):

	'''
		{
			"name": "Saumitra Bose",
			"subject": "Computers",
			"feedback": ["Hello", "World"],
			"comments": "ASDASdsadasdsadsadad adasdsad",
			"division": "SE-A",
			"isPractical": False
		}
	'''

	print request.body.decode('utf-8')
	value = json.loads(request.body.decode('utf-8'))
	print value
	feedback = value['feedback']
	name = value['name']
	subject = value['subject']
	comments = value['comments']
	isPractical = False
	if value['isPractical'] == 'True':
		isPractical = True
	elif value['isPractical'] == 'False':
		isPractical = False
	else:
		return JsonResponse({'error': 'Invalid value for isPractical'})

	division = value['division']

	teach = Teacher(
				name=name,
				subject=subject,
				comments=comments,
				feedback=feedback,
				division=division,
				isPractical=isPractical,
			)

	teach.save()

	return HttpResponse('success')


def show_all_teachers(request):
	return render(request, 'all-teachers.html', {})


def get_teachers(request, isPractical="False"):
	print isPractical
	_isPractical = ""

	if isPractical == "False":
		_isPractical = False
	else:
		_isPractical = True

	allTeachers = Teacher.objects.filter(isPractical=_isPractical)
	# print allTeachers

	context = {
		'teachers': {},
	}

	teachersDict = {}

	length = 0

	if _isPractical:
		length = 5
	else:
		length = 9

	# context['averages'] = [0 for x in range(length)]
	# count = 0

	for teach in allTeachers:
		feedback = teach.feedback.split(',')
		if teach.name in context['teachers']:
			context['teachers'][teach.name].append({
				"subject": teach.subject,
				"comments": teach.comments,
				"feedback": feedback,
			})
		else:
			context['teachers'][teach.name] = [{
				"subject": teach.subject,
				"comments": teach.comments,
				"feedback": feedback,
			}]

		# for i in range(length):
		# 	context['averages'][i] = context['averages'][i]*count + int(feedback[i])
		# count+=1

	return JsonResponse(context)


def teacher(request, teacher_name):
	print teacher_name
	return render(request, 'teacher.html', {"teacher": teacher_name})


def get_one_teacher(request, teacher_name):
	teacher = Teacher.objects.filter(name=teacher_name)
	context = {
		"name": teacher_name,
		"comments": [],
		"averageTheory": [0 for x in range(9)],
		"averagePractical": [0 for x in range(5)]
	}

	countTh = 0
	countPr = 0
	for teach in teacher:
		context['comments'].append(
			{
				"division": teach.division,
				"comment": teach.comments,
				"subject": teach.subject,
			})

		feedback = teach.feedback.split(',')

		if teach.isPractical:
			for i in range(5):
				context['averagePractical'][i] = (context['averagePractical'][i]*countPr + int(feedback[i])) / (countPr + 1)
			countPr += 1

		else:
			for i in range(9):
				context['averageTheory'][i] = (context['averageTheory'][i]*countTh + int(feedback[i])) / (countTh + 1)
			countTh += 1

	return JsonResponse(context)