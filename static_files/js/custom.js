$(function() {

    /* Handler show/hide on scroll */
    $(window).scroll(function() {
        if ($(document).scrollTop() > 100) {
            $('.footer-container').addClass("kg-show");
        } else {
            $('.footer-container').removeClass("kg-show");
        }
    });

    /* Handle onClick show/hide */
    $('.footer-container').click(function(){
        $('.footer-container').toggleClass("kg-show");
    })
})
