var teacher_name = document.getElementById('teacher-name').value

qwest.get('/get-one-teacher/'+teacher_name+'/')
.then(function(res){
	var response = JSON.parse(res.response)
	console.log(response)
})

