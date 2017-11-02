$(document).ready(function () {

    $("#signUpBtn").click(function () {
        var formData = new FormData();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        var signUpUserName = $("input[name=signUpUserName]").val();
        var signUpPassword = $("input[name=signUpPassword]").val();
        var passwordRepeat = $("input[name=passwordRepeat]").val();
        var nickName = $("input[name=nickName]").val();
        var photo = $("#photo")[0].files[0];
        var email = $("input[name=email]").val();
        var last_name = $('input[name=last_name]').val();
        var first_name = $('input[name=first_name').val();

        // todo: 验证输入
        formData.append('csrfmiddlewaretoken', csrfmiddlewaretoken);
        formData.append("photo", photo);
        formData.append('user_name', signUpUserName);
        formData.append('password', signUpPassword);
        formData.append('nick_name', nickName);
        formData.append('email', email);
        formData.append('last_name',last_name);
        formData.append('first_name',first_name);

        $.ajax({
            url: '/account/create_account',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (responseText, statusText, xhr, $form) {
                if (responseText == 'succeed') {
                    window.location.href = "/";
                } else {
                    alert("Error!");
                    //todo: tell where wrong.
                }
            },
            error: function (responseStr) {
                alert(responseStr.toString());
                console.log("error");
            }
        });

    });
});