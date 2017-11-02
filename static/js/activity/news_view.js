$(document).ready(function () {
    var activity_id = parseInt($('#activity').html())
    var url = '/activity/innews/' + activity_id;
    load();

    function load() {
        $.get(url, {}, function (html) {
            $('#activity').html(html);

            $('#a_cancel').click(function () {
                $.get('/activity/reserve', {
                    operation: 'cancel',
                    activity_id: activity_id
                }, function (text) {
                    // todo:给提示。。。。
                    load();
                });
            });

            $('#a_reserve').click(function () {
                $.get('/activity/reserve', {
                    operation: 'reserve',
                    activity_id: activity_id
                }, function (text) {
                    // todo:给提示。。。。
                    load();
                });
            });

        });

    }


});