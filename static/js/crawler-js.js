
$(function() {
	$('#name_field').bind('input', function(){
		$.getJSON("_auto_results", {
			name: $('#name_field').val(),
			location: $('#location_field').val()
		}, function(data) {
			console.log(data);
			console.log(data.name);
		});
	});
});