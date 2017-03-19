var teacher_name = document.getElementById('teacher-name').value


var dict = {
	0: "Ability to understand student's difficulties and willingness to help them",
	1: "Regularity and Punctuality",
	2: "Commitment to academic work in the class",
	3: "Interaction in the class",
	4: "Coverage of syllabus",
	5: "Planning of lessons throughout the Semester",
	6: "Effective communication of subject matter",
	7: "Management of lecture and class control",
	8: "Overall ability to maintain sanctity of Teaching - Learning process",
}

var pracdict = {
   0: "Planned Laboratory instructions including management of practicals",
   1: "Uniform coverage of work guidance for writing journals",
   2:"Checking of journals and marking continuous assessments of term work",
   3: "Preparation and display of instructional material, charts, models etc.",
   4: "Discussion on latest and relavant applications in the field",
}

qwest.get('/get-one-teacher/'+teacher_name+'/')
.then(function(res){
	var response = JSON.parse(res.response)
	console.log(response)
	createAttributes(response);
})

function createAttributes(response){
	console.log('woo')
	var th = []
	var pr = []

	for(var i in response.averageTheory){
		th.push({
			index: i,
			value: response.averageTheory[i]}
		)
	}

	for(i in response.averagePractical){
		pr.push({
			index: i,
			value: response.averagePractical[i]
		});
	}

	th = th.sort((a,b)=>b.value-a.value)
	pr = pr.sort((a,b)=>b.value-a.value)
	console.log('hello')
	var positiveTh = [],
	negativeTh = [],
	positivePr = [],
	negativePr = [];


	var key;
	for(i = 0; i<3; i++){
		positiveTh.push(dict[th[i].index])
		negativeTh.push(dict[th[8-i].index])
	}

	positivePr.push(pracdict[pr[0].index])
	negativePr.push(pracdict[pr[4].index])

	console.log( positiveTh, positivePr, negativeTh, negativePr)

	console.log(th, pr);
}