$(document).ready(function()
{
    $(".submit_btn").click(function()
    {
        var password = $("#pwd").val();
        var conform_password = $("#confirm_pwd").val();
        
        if(password == conform_password)
        {
            return true;
        }
        
        else
        {
            iziToast.error({
                title:"Error",
                message:"You have entered wrong Password",
            });
            password = $("#pwd").val("");
            conform_password = $("#confirm_pwd").val("");
        } 
    })
})