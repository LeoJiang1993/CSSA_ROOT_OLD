$(document).ready(function () {
    $("#signIn").click(function () {
        var user_name = $("input[name=userName]").val();
        var password = $("input[name=password]").val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $(document).ready(function () {
            $.post("/account/sign_in", {
                    'user_name': user_name,
                    'password': password,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken
                },
                function (data) {
                    if (data == "succeed") {
                        reloadHeader();
                    } else {
                        $("#errorDiv").html("User Name and Password Mismatch!");
                    }
                });


        })
    });


    $("#logOut").click(function () {
        $.get("/account/logout",{},reloadHeader);

    });


    //todo： 不能reload header 会导致js绑定无效
    function reloadHeader() {
        $("header").load("/header")
    }

    $("#signUp").click(function () {
        open("/account/sign_up");
    });
});