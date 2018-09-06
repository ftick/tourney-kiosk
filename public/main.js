function create_name_list(list) {
    $('#name_list').children().each(function(index) {
        $(this).text(list[index].tag);
    });
}

function get_current_hover() {
    var current_hover = null;
    $('#name_list').children().each(function(index) {
        if ($(this).hasClass("search_results_hovered"))
            return current_hover = $(this);
    });
    return current_hover;
}

$(document).ready(function() {
$("#name_search_input").keyup(function(event) {
    if ($(this).val().trim().length === 0) return;
    if (!(event.which === 38 || event.which === 40))
        $("#name_list").children().mouseleave();
    $.ajax({
        method: "POST",
        url: "/ajax/namesearch",
        data: { name: $(this).val() }
    })
        .done(function(msg) {
            create_name_list(JSON.parse(msg));
        });
});

$("#name_list").children().mousemove(function(event) {
    if ($(this).hasClass("search_results_hovered"))
        return; // don't run the mouse enter
                // junk if it's already hovered
    $(this).mouseenter();
});

$("#name_list").children().mouseenter(function(event) {
    $("#name_list").children().each(function(index) {
        $(this).mouseleave();
    });
    $(this).addClass("search_results_hovered");
});

$("#name_list").children().mouseleave(function(event) {
    $(this).removeClass("search_results_hovered");
});

$("#name_search_input").keydown(function(event) {
    // 38 is up, 40 is down
    // console.log(event.which); 
    if (event.which === 40) {
        var hover = get_current_hover();
        if (hover === null) {
            $('#name_list').children().first().mouseenter();
        } else {
            if (hover.next().length)
                hover.mouseleave();
                hover.next().mouseenter();
        }
    }

    if (event.which === 38) {
        var hover = get_current_hover();
        if (hover !== null) {
            hover.mouseleave();
            if (hover.prev().length)
                hover.prev().mouseenter();
        }
    }
});


});