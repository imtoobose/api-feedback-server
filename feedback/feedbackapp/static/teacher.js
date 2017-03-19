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

	var slider
	/*

<li class="short">
	<input class="mdl-slider mdl-js-slider" type="range" id="s1" min="0" max="10" value="4" step="2" disabled>
</li>

	*/

	var sli, inp
	var pover = document.getElementById('prac-overall')
	var tover = document.getElementById('theory-overall')

	for(var i in response.averageTheory){
		th.push({
			index: i,
			value: response.averageTheory[i]}
		)

		sli = document.createElement('li')
		// span = document.createElement('span')
		// sli.classList.add("short")
		sli.innerHTML = dict[i] + ': <span style="font-weight:900">' + response.averageTheory[i] + ' \/ 5'  +"</span>"
		// inp = document.createElement('input')
		// inp.classList.add("mdl-slider")
		// inp.classList.add("mdl-js-slider")
		// // inp.classList.add('is-upgraded')
		// inp.id = "st"+i
		// inp.type = 'range'
		// inp.min = 0
		// inp.step = 1
		// inp.max = 5
		// inp.value = response.averageTheory[i]

		// sli.appendChild(inp)
		// tover.appendChild(sli)

		tover.appendChild(sli)

	}

	for(i in response.averagePractical){
		pr.push({
			index: i,
			value: response.averagePractical[i]
		});
		
		// sli = document.createElement('li')
		// sli.classList.add("short")
		// inp = document.createElement('input')
		// inp.classList.add("mdl-slider")
		// inp.classList.add("mdl-js-slider")
		// // inp.classList.add('is-upgraded')
		// inp.id = "sp"+i
		// inp.type = 'range'
		// inp.min = 0
		// inp.step = 1
		// inp.max = 5
		// inp.value = response.averagePractical[i]

		// sli.appendChild(inp)
		// pover.appendChild(sli)

		sli = document.createElement('li')
		// sli.classList.add("short")
		sli.innerHTML = pracdict[i] + ': <span style="font-weight:900">' + response.averagePractical[i] + ' \/ 5' +'</span>'
		// inp = document.createElement('input')
		// inp.classList.add("mdl-slider")
		// inp.classList.add("mdl-js-slider")
		// // inp.classList.add('is-upgraded')
		// inp.id = "st"+i
		// inp.type = 'range'
		// inp.min = 0
		// inp.step = 1
		// inp.max = 5
		// inp.value = response.averageTheory[i]

		// sli.appendChild(inp)
		// tover.appendChild(sli)

		pover.appendChild(sli)

	}

	th = th.sort((a,b)=>b.value-a.value)
	pr = pr.sort((a,b)=>b.value-a.value)
	console.log('hello')
	var positiveTh = [],
	negativeTh = [],
	positivePr = [],
	negativePr = [];

	var thul = document.getElementById('theory')
	var prul = document.getElementById('prac')
	var tnul = document.getElementById('theory-neg')
	var pnul = document.getElementById('prac-neg')
	var tli;

	var key;
	for(i = 0; i<3; i++){
		// positiveTh.push(dict[th[i].index])
		// negativeTh.push(dict[th[8-i].index])

		tli = document.createElement('ul')
		tli.innerHTML = dict[th[i].index]
		thul.appendChild(tli)

		tli = document.createElement('ul')
		tli.innerHTML = dict[th[8-i].index]
		tnul.appendChild(tli)
	}

	positivePr.push(pracdict[pr[0].index])
	negativePr.push(pracdict[pr[4].index])
	
	tli = document.createElement('ul')
	tli.innerHTML= pracdict[pr[0].index]
	prul.appendChild(tli)

	tli = document.createElement('ul')
	tli.innerHTML= pracdict[pr[4].index]
	pnul.appendChild(tli)

	var bestones = response.bestones
	var reviews = document.getElementById('reviews')
	Object.keys(bestones).map((key)=>{
		var arr = bestones[key]
		var ul = document.createElement('ul')
		var h5 = document.createElement('h5')

		h5.innerHTML = "<span style='font-weight:900; margin-left:40px; font-size:14px; text-decoration:underline'>"+ key + '</span'
		// reviews.appendChild(li)
		arr.map(_data=>{
			var li = document.createElement('li')
			li.innerHTML = _data
			ul.appendChild(li)
		})

		reviews.appendChild(h5)
		reviews.appendChild(ul)
	})

	var comments = response.comments
	var poscomments = comments.filter(data=>data.commentSentiment==1)
	var negcomments = comments.filter(data=>data.commentSentiment==0)

	var posCom = document.getElementById('pos-reviews')
	var negCom = document.getElementById('neg-reviews')

	poscomments.map(_comment=>{
		var li = document.createElement('li')
		li.innerHTML = _comment.comment
		posCom.appendChild(li)
	})

	negcomments.map(_comment=>{
		var li = document.createElement('li')
		li.innerHTML = _comment.comment
		negCom.appendChild(li)
	})
}