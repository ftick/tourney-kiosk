function is_letter_input(input) {
    if (event.keyCode >= 48 && event.keyCode <= 57) return true; // number
    if (event.keyCode >= 65 && event.keyCode <= 90) return true; // letter
    return false;
}

function create_name_list(list) {
    $('#search_results').slideDown(400);
    $('#name_list').children().each(function(index) {
        $(this).text(list[index].tag);
        $(this).data('uuid', list[index].uuid);
    });
}

function load_player_data() {
    var search_field = $("#name_search_input");
    var hover = get_current_hover();
        if (hover !== null) {
            search_field.val(hover.text());
            $('#search_results').slideUp(400);
            $('#player_stats_box').fadeIn();
            $('#player_tag').text("loading...");
            $('#player_rank').text("loading...");
            $('#data_provider').text("loading...");
            $.ajax({
                method: "POST",
                url: "/ajax/playerstats",
                data: { uuid: hover.data('uuid') }
            })
                .done(function(msg) {
                    var json = JSON.parse(msg);
                    $('#player_tag').text(json.tag);
                    if (json.ranking.rank !== -1) {
                        $('#player_rank').text(
                            'ranked ' +
                            json.ranking.rank + 
                            json.ranking.rank_suffix);
                        $('#data_provider').text("Data provided by " + json.provider);
                        $('#data_provider').fadeIn();
                    } else {
                        $('#player_rank').text('unranked!');
                        $('#data_provider').fadeOut();
                    }
                });
        }
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
    if (!(is_letter_input(event.which))) return;
    if ($(this).val().trim().length === 0) return;
    if (!(event.which === 38 || event.which === 40))
        $("#name_list").children().mouseleave();
    if (event.which === 13) return;
    $.ajax({
        method: "POST",
        url: "/ajax/namesearch",
        data: { name: $(this).val() }
    })
        .done(function(msg) {
            create_name_list(JSON.parse(msg));
        });
});

$("#name_search_input").blur(function(event) {
    $('#search_results').slideUp(400);
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

$("#name_list").children().mouseup(function(event) {
    load_player_data();
});

$("#name_search_input").keydown(function(event) {
    // 38 is up, 40 is down, 13 is enter
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

    if (event.which === 13) {
        load_player_data();
    }
});


});