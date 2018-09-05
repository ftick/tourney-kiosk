$( document ).ready(function() {

$( "#name_search_input" ).keyup(function() {
	if ($(this).val().trim().length === 0) return;
  	$.ajax({
		method: "POST",
	 	url: "/ajax/namesearch",
	  	data: { name: $(this).val() }
	})
	  	.done(function( msg ) {
	    	$("#log_area").text(msg)
	  	});
});

});