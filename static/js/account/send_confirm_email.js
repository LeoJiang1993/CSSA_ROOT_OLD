$(document).ready(function () {
   $('.resend_confirm_email').click(function () {
       $.get('/account/resend_verify_email',{},function () {
           $('#info').html('Email Sent.');
       })
   })
});