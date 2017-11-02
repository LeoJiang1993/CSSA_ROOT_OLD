$(document).ready(function () {
    $('#edit_by_topic').selectmenu({
        change: function (event, data) {
            if (data.item.value != '')
                $('#editSection').load('/newsadmin/newslist/' + data.item.value);
        }
    });
    $('#edit_by_place').selectmenu({
        change: function (event, data) {
            if (data.item.value != '')
                $('#editSection').load('newsadmin/specialplace/' + data.item.value);
        }
    });

    $('button').button();
});