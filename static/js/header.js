$(document).ready(function () {
    $('header').load('/header')
    $(document).ajaxComplete(function () {
        alert('a');
        $('.button').click(function () {
            var $list = $(this).find(".header_list");
            alert($list.html());
            $list.toggle();
        });

    });

});