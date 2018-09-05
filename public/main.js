function create_name_list(list) {
	var name_list_dom = $("<ul></ul>");
	for(i=0;i<list.length;i++) {
		var list_item = $("<li></li>");
		list_item.text(list[i].tag);
		name_list_dom.append(list_item);
	}
	$('#log_area').html(name_list_dom);
}

$( document ).ready(function() {
$( "#name_search_input" ).keyup(function() {
	if ($(this).val().trim().length === 0) return;
  	$.ajax({
		method: "POST",
	 	url: "/ajax/namesearch",
	  	data: { name: $(this).val() }
	})
	  	.done(function( msg ) {
	    	create_name_list(JSON.parse(msg));
	  	});
});
});