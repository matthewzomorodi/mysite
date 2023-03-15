$(document).ready(function(){
    $("#new-client-form").submit(function(event){
        
        /* stop form from submitting normally */
        event.preventDefault();
        
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: {
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
                formData: $(this).serialize(),
            },
            success: function(response){
                alert("Form submitted!");
                alert("success.response==" + response);
                location.reload();
            },
            error: function(response){
                alert("Form submission failed.");
                console.log("error.response==" + response);

            }
        });

        // $.post(
        //     $(this).attr('action'),
        //     {
        //         csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        //         formData: $(this).serialize(),
        //     },
        //     function(data, status){
        //         console.log("Data: " + data + "\nStatus: " + status)
        //     }
        // );
    });
});

function tellme(value){
    alert(value);
};