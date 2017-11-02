$(document).ready(function () {
    var $comment_div = $('#comment_list');
    var news_id = $('#news').val();
    var status = $('#comment_status').val();
    var current_page = parseInt($('#c_current').html());
    load(current_page);
    $('#topic').change(function () {
        var topic = $(this).val();
        if (topic=='')return;
        $('#news').load('/newsadmin/specialplace/newslist/' + topic);
    });

    $('#news').change(function () {
        news_id = $(this).val();
        load(1);
    });

    $('#comment_status').change(function () {
        status = $(this).val();
        load(1);
    });

    function bind() {
        $('.pg_btn').unbind('click').click(function () {
            current_page = parseInt($('#c_current').html());
            var html = $(this).html();
            switch (html) {
                case '&lt;&lt;':
                    target = current_page - 1;
                    load(target);
                    break;
                case '&gt;&gt;': // >>
                    target = current_page + 1;
                    load(target);
                    break;
                case '...':
                    break;
                default:
                    var target = $(this).html();
                    load(target);
                    break;
            }
        });

        $('.delete_comment').click(function () {
            var comment_id = parseInt($(this).find('div').html());
            $.get('/comment/delete', {id: comment_id}, function () {
                load(parseInt($('#c_current').html()));
            });
        });

        $('.active_comment').click(function () {
            var comment_id = parseInt($(this).find('div').html());
            $.get('/comment/active', {id: comment_id}, function () {
                load(parseInt($('#c_current').html()));
            });
        });

    }

    function load(page) {
        if (status == '' || news_id == '') return;
        $.get('/comment/admin/list', {
            page: page,
            news_id: news_id,
            status: status
        }, function (html) {
            $comment_div.html(html);
            bind();
        });
    }


});