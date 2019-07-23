$(function(){
    $('.login-content input').focus(function(){
        $(this).prev().prev().css('color','#999999');
    });
    $('.login-content input').blur(function(){
        $(this).prev().prev().css('color','#000000');
    });
    $('.login-content #cell_verify').mouseover(function () {
        $(this).css('opacity','1');
      });

    // TODO 勾选后颜色变化
    console.log($("#remember").is(":checked"))
    if($("#remember").is(":checked")){
        $("#remember").next().css('color','#ff0035');
    }else{
        $("#remember").next().css('color','#999999');
    };

   
})