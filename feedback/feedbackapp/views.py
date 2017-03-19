from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect, csrf_exempt
# from django.core.serializers import json
import json
from django.http import HttpResponse, JsonResponse
from .models import Teacher
from sklearn.externals import joblib
# Create your views here.

COUNT_VECT = "{base_path}/sklearn-models/count_vect.pkl".format(
    base_path=os.path.abspath(os.path.dirname(__file__))
)

TF_TRANS = "{base_path}/sklearn-models/tf_transformer.plk".format(
    base_path=os.path.abspath(os.path.dirname(__file__))
)

CLF = "{base_path}/sklearn-models/clf.plk".format(
    base_path=os.path.abspath(os.path.dirname(__file__))
)

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


def show_all_teachers(request, isPractical):
	allTeachers = Teacher.objects.all()
	context = {
		'teachers': [],
	}

	for teach in allTeachers:
		context['teachers'].append({
			"name": teach.name,
			"subject": teach.subject,
			"comments": teach.comments,
			"feedback": teach.feedback.split(','),
			})

	print context

	return render(request, 'all-teachers.html', context)


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


"""
Pass single string or list of string to get single int or array of int as output.
1 indicates Positive sentiment while 0 indicate negative sentiment
"""
def analysis_sentence(sentence):
	count_vect = joblib.load(COUNT_VECT) 
	tf_transformer = joblib.load(TF_TRANS) 
	clf = joblib.load(CLF)

	x_test_counts = count_vect.transform(lines)
	x_test_tf = tf_transformer.transform(x_test_counts)

	predicted = clf.predict(x_test_tf)

	return predicted