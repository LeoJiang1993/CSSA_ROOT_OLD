function changeFrameHeight() {
    var ifm = document.getElementById("news_content");
    var scale = window.devicePixelRatio;
    ifm.height = $('#news_content').contents().find('body').height();
    //ifm.height = document.documentElement.clientHeight*scale;
}

window.onresize = function () {
    changeFrameHeight();
}