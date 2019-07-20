$(function (){
    /*点击'设置'显示dropdown_set*/
    $('#setting').click(function (e){
        e.stopPropagation();
        $('#dropdown_set').slideToggle();
        if($('#dropdown_set').is(':visible')){
        $(document).one('click',function() {
            $('#dropdown_set').hide();
        })
        }
    });
    /*点击#address显示下拉列表*/
    $('#address ul>li').click(function (e){
        e.stopPropagation();
        $('#address ol').slideToggle();
        if($('#address ol').is(':visible')){
        $(document).one('click',function() {
            $('#address ol').hide();
        })
        }
    });
//    var list_1=$('#address ol').children;
//    console.log(list_1)
//    for(var i=0; i<list_1.length;i++){
//        console.log(list_1[i])
//        list[i].onclick=function(){
//        $('#address ul>li').html($(this).html())
//        }
//    }
    $('#address ol li').click(function (){
       /*var data=$(this).html();*/
       $('#address ul>li').html($(this).html())
    });

    $('#left').delegate('div[data-target]',
    'click',function (){
        var target = $(this).data('target');
        console.log(target);
        if(target == '#list_chat'){
            $(target).show();
            $('#list_news,#list_friend').hide();
        }else if(target=='#list_news'){
            $(target).show();
            $('#list_chat,#list_friend').hide();
        }else{
            $(target).show();
            $('#list_chat,#list_news').hide();
        }
    })
    $('.chat_item').click(function (){
        $('#right').show();
        $('#right_blank,#right_news,#right_news').hide()
    })
    $('.news_item').click(function (){
        $('#right_news').show();
        $('#right_blank,#right,#right_friend').hide()
    })
    $('.friend_item').click(function (){
        $('#right_friend').show();
        $('#right_blank,#right,#right_news').hide()
    })





})