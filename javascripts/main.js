$(document).ready(function() {
    //método para stylear código
    SyntaxHighlighter.all();

    //tablas
    $(".header-tabs li a").on("click", function (e){
        e.preventDefault();
        $(this).parent().siblings().removeClass("active")
        $(this).parent().addClass("active")
        var endpoint = $(this).attr("href");
        $(endpoint).siblings().hide();
        $(endpoint).show();
    });
});