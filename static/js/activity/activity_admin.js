$(document).ready(function () {
    $('#activity_status').change(function () {
        if ($(this).val() != "")
            $('#activity_list').load('/activity/admin/list/' + $(this).val());
    });
});