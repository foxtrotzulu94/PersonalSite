/**
 * Created by foxtrot on 14/05/16.
 */

$( document ).ready(function() {

    window.POPUP_MODAL = $("#test_popup");

    var divToAppendTo = $('#project_div');
    var projects = $(".grid-item",divToAppendTo);


    for(var i=0; i < projects.length; i++){
        var element = projects.eq(i);
        var anchor = $("a",element);
        anchor.removeAttr("target");
        anchor.attr("href","");
        var pk = element.attr("id");
        anchor.click({category: "projects", pk: pk, idx:i},modal_popup);
        // anchor.removeAttr("href");
    }

    console.log( "Done loading" );
});

$(window).load(function(){
    console.log("Images Loaded!");
    $('.grid').masonry(); //Kick masonry to fire up again
});

