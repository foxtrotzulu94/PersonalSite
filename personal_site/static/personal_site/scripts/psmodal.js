/**
 * Created by foxtrot on 14/05/16.
 */

// Function that handles populating the modular modal to display more info on a display item.
// Takes an event that should have the following fields as data (shown as [field name] -> [type of value when accessed])
//  - title         -> String
//  - description   -> String
//  - imgs          -> List of strings (URLs)
//  - date_active   -> String
//  - tech          -> string
modal_popup = function (event) {
    var popupModal = window.POPUP_MODAL;

    //Open modal
    popupModal.modal("show");

    //Populate the text sections first
    var fullTitle = event.data.title + event.data.date_active;
    $("#modal_title",popupModal).html(fullTitle);
    $("#modal_description",popupModal).html(event.data.description);
    $("#modal_tech",popupModal).html(event.data.tech);

    //Now fill the images
    $("#modal_")
};