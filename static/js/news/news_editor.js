$(document).ready(function () {
    var editor = CKEDITOR.replace('editor', {});

    $("input[name=submit]").click(function () {
        $('textarea[name=content]').html(editor.getData());
        $.post('/newsadmin/editnews/' + $('input[name=id]').val(),
            $('#newsEditor').serialize(), function (text) {
                alert(text);
            }
        );
    });


});
