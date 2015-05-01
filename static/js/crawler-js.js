



$(function() {
	$('#name_field').bind('input', function(){
		
		search();

	
	});
});


function search(){

	$.getJSON("_auto_results", {
			name: $('#name_field').val(),
			location: $('#location_field').val()
		}, function(data) {
			console.log(data);
			results_box = $(".auto_results");
			results_box.html(data.name + "<img src = " + data.images[0] + ">" + data.position + data.location + data.industry);



		});

}