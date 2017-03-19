console.log('hello there');

qwest.get('get-teachers/False/')
.then(function(res){
	console.log(res.response);
})