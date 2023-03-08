$(document).ready(function(){
    $("#new-client-form").submit(function(event){

        const formData = $(this).serialize();

        console.log(formData);
        event.preventDefault();

    });
});