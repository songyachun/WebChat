$(function(){
    $('.login-content input').focus(function(){
        $(this).prev().css('color','#999999');
    })
    $('.login-content input').blur(function(){
        $(this).prev().css('color','#000000');
    });
   
})