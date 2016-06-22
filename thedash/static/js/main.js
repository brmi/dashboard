$(document).ready(function () {
    $(document).on('click', '.clickable-row', (function(e){

        window.document.location = $(this).data("href");
    }));
});

