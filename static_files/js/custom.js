$(function() {

    /* Handler show/hide on scroll */
    $(window).scroll(function() {
        console.log($(document).scrollTop());
        if ($(document).scrollTop() > 100) {
            $('.footer-container').addClass("show");
        } else {
            $('.footer-container').removeClass("show");
        }
    });

    /* Handle onClick show/hide */
    $('.footer-container').click(function(){
        console.log("yolo");
        $('.footer-container').toggleClass("show");
    })
})
