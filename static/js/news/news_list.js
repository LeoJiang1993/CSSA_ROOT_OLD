$(document).ready(function () {
    var $news_div = $('#news_list');
    var news_topic_id = parseInt($news_div.html());
    $news_div.html("");
    $news_div.show();
    load(1);
    var current_page = parseInt($('#c_current').html());

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
        if (news_topic_id == '') return;
        $.get('/newslist/list', {
            page: page,
            topic_id: news_topic_id
        }, function (html) {
            $news_div.html(html);
            bind();
        });
    }


});