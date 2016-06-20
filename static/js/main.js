
function showResult(str) {
    if (str.length==0)
    {
        document.getElementById("livesearch").innerHTML="";
        document.getElementById("livesearch").style.border="0px";
        return;
    }
    else
    {
        document.getElementById("livesearch").innerHTML=str;
    }
}

// function updateDay() {
//     $(document).on('submit','#new_day_form', function(e){
//         e.preventDefault() //prevent page from getting refreshed
//
//         $.ajax({
//             type: 'POST',
//             url: '/day/',
//             data:{
//                 day_num: $('#day').val(),
//                 csrfmiddlewaretoken:$('input[name=csrfmiddlewartoken]').val()
//             },
//             success:function(){
//                 alert("success")
//             }
//         });
//     });
// }

$(document).ready(function () {
    showResult();
    // updateDay();
})
