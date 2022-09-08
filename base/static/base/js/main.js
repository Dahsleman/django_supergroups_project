$(document).ready(function() {
    $("#id_recurring_event").change(function() {
        if ($(this).val() === "No") {
        $('#recurrence_pattern').hide();
        } else {
        $('#recurrence_pattern').show();
        }
    });
    $("#id_recurring_event").trigger("change")
    
})
