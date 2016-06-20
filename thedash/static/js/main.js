$(document).ready(function () {
    $(document).on('click', '.clickable-row', (function(){
        window.document.location = $(this).data("href");
    }));
});

