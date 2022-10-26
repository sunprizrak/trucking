$(function(){
    let url = $(location).attr('href');
    let tab_name = url.split('/').slice(-1)[0];
    $('#nav-profile a[name=tab-' + tab_name + ']').addClass('active');
});