$(document).ready(function () {
    $('header').load('/header')
    $(document).ajaxComplete(function () {
        $('.button').click(function () {
            var $list = $(this).find(".header_list");
            $list.toggle();
        });

    });

});