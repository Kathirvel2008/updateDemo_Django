$(document).ready(function()
{
    $("#customTable").DataTable();

    $(".delete_link").click(function()
    {
        swal.fire({
            text:"Are you sure want to Delete ?",
            icon:"warning",
            confirmButtonText:"Delete",
            confirmButtonColor:"rgb(58, 207, 58)",
            confirmButtonClass:"btn swal_ok_btn",
            showCancelButton:true,
            cancelButtonText:"Cancel",
            cancelButtonColor:"rgb(221, 54, 54)",
            cancelButtonClass:"btn swal_cancel_btn",
            }).then(function(result)
            {
                if(result.value == true)
                {
                    delete_page();
                    console.log("You deleted the list");
                }
                else if(result.dismiss == 'cancel')
                {
                    console.log("You cancelled the delete");
                }
            })
    })
})