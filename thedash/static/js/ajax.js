$(function(){
    $('#search').keyup(function(){

        $.ajax({
            type: 'POST',
            url: "/day/",
            data: {
                'search_day' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}