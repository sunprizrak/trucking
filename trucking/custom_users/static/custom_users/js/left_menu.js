$(function () {
    let position = $('#left-menu').position();
    $('#left-menu').css('top', position.top);
    let height_nav_prof = $('#nav-profile').height();
    $('#nav-profile').css('height', height_nav_prof.toString() + 'px');
});