$(document).ready(function () {
    $("#sign_in_activity").click(function () {
        var user_name = $("input[name=u_name]").val();
        var password = $("input[name=pwd]").val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $(document).ready(function () {
            $.post("/account/sign_in", {
                    'user_name': user_name,
                    'password': password,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken
                },
                function (data) {
                    if (data == "succeed") {
                        $(document).refresh();
                    } else {
                        $("#errorDiv").html("User Name and Password Mismatch!");
                    }
                });


        })
    });
});
