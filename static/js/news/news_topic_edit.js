$(document).ready(function () {
    $('.modify').click(function () {
        submit_modify($(this))
    });

    function submit_modify($this) {
        var description = $this.parent().find('input[name=description]').val();
        var status = $this.parent().find('select[name=status]').val();
        var topic_id = parseInt($this.attr('name'));
        $.get('/newsadmin/topic/save', {
            'description': description,
            'status': status, 'topic_id': topic_id
        }, function (data) {
            $this.attr('name', data);
        })
    }

    $('input[name=new_topic]').click(function () {
        var $temp = $(this).prev('ul').find('li:last-child');
        var new_li = $temp.before('<li>' + $temp.html() + '</li>');
        $('.modify').unbind('click').click(function () {
            submit_modify($(this))
        });
    })
});