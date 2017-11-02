$(document).ready(function () {
    var $comment_div = $('#comment');
    var news_id = parseInt($comment_div.html());
    load(1);

    function bind() {
        $('.pg_btn').unbind('click').click(function () {
            switch ($(this).html()) {
                case '<<':
                    target = parseInt($('#c_current').html()) - 1;
                    load(target);
                    break;
                case '>>':
                    target = parseInt($('#c_current').html()) + 1;
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
    }

    function load(page) {
        $.get('/comment/' + news_id, {page: page}, function (html) {
            $comment_div.html(html);
            bind();

            $('#submit_comment').click(function () {
                var content = $('input[name=content]').val();
                $.get('/comment/comment', {
                    news_id: news_id,
                    content: content
                }, function (text) {
                    alert(text);
                    load(1);
                });
            });

            $('#cancel_comment').click(function () {
                $('#add_comment').show();
                $('#add_comment_form').hide();
                $('input[name=content]').val('');
            });

            $('#add_comment').click(function () {
                $('#add_comment_form').show();
                $(this).hide();
            });

            $('.delete_comment').click(function () {
                var comment_id = parseInt($(this).find('div').html());
                $.get('/comment/delete', {id: comment_id}, function () {
                    load(parseInt($('#c_current').html()));
                });
            })
        });
    }


});