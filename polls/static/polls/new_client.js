// $(document).ready(function(){
//     $("#new-client-form").submit(function(event){
        
//         /* stop form from submitting normally */
//         event.preventDefault();

//         /* get the action attribute from the <form action=""> element */
//         var $form = $(this),
//             url = $form.attr('action');
        

//         /* Send the data using post with element id name and name2*/
//         var posting = $.post(url, {
//             csrfmiddlewaretoken: $('#csrfmiddlewaretoken').val(),
//             client_first_name: $('#client-first-name').val(),
//             client_last_name: $('#client-last-name').val(),
//             client_email: $('#client-email').val(),
//             client_phone: $('#client-phone').val(),
//         });

//         /* Alerts the results */
//         posting.done(function(data) {
//             alert("Form submitted!");
//         });
//         posting.fail(function() {
//             alert("Form submission failed.");
//         });
//     });
// });

// $("#btn-new-client").click(function(){
//     const url = $("#new-client-form").attr('action');
//     alert(url);

//     $.post(
//         url,
//         {
//             csrfmiddlewaretoken: $('#csrfmiddlewaretoken').val(),
//             client_first_name: $('#client-first-name').val(),
//             client_last_name: $('#client-last-name').val(),
//             client_email: $('#client-email').val(),
//             client_phone: $('#client-phone').val()
//         },
//         function(data, status){
//             alert("Data: " + data + "\nStatus: " + status);
//         });
// });

function tellme(value){
    alert(value);
};