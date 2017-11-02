$(document).ready(function () {
    $('input[type=button]').button();
    bind();

    $('#s_topic').selectmenu({
        change: function (event, data) {
            if (data.item.value != '')
                $.get('/newsadmin/specialplace/newslist/' + data.item.value, {}, function (html) {
                    $('#s_news').html(html);
                    $('#s_news').selectmenu('refresh');
                });
        }
    });

    $('#s_news').selectmenu({
        change: function (event, data) {
            if (data.item.value != '') {
                $('#news_list').append(
                    '<li class="news_item">' +
                    '<span hidden class="news_id">' + data.item.value + '</span>' +
                    '<span class="NewsTitle">' + data.item.label + '</span>' +
                    '</li>');
                bind();
            }
        }
    });

    function bind() {
        $("#news_list").sortable({
            placeholder: "news_item"
        });
        $("#news_list").disableSelection();

        $('.news_item').button();
        $('#delete_position').droppable({
            drop: function (event, ui) {
                $(ui.draggable).remove();
            }
        });

    }

    $('#submit_change').click(function () {
        var rs = "[";
        $('#news_list').find('li').each(function () {
           rs += ($(this).find('.news_id').html()) + ",";
        });
        rs = rs.substr(0, rs.length - 1);
        rs += ']';
        $.get('newsadmin/specialplace/' + $('#edit_by_place').val(),
            {rs: rs},
            function () {
                $('#editSection').load('newsadmin/specialplace/' + $('#edit_by_place').val());
            }
        );
    })

});