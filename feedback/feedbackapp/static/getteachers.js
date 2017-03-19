console.log('hello there');

qwest.get('get-teachers/')
.then(function(res){
	console.log(res.response);
})