$(function (){
    /*点击'设置'显示dropdown_set*/
    var avatar = $("#user_icon").attr('src');
    avatar=avatar.substring(28,avatar.length)
    console.log(avatar)
    if (avatar==''){
        $("#user_icon").attr('src','/static/images/timg.jpeg')
        console.log($("#user_icon").attr('src'))
    }
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
          $("#address ol").hide();
        e.stopPropagation();
        $('#address ol').slideToggle();
        if($('#address ol').is(':visible')){
        $(document).one('click',function() {
            $('#address ol').hide();
        })
        }
    });



    $('#address ol li').click(function (){
       /*var data=$(this).html();*/
       $('#address ul span').html($(this).html())
       $('#s01').html('');
       $('#s02').html('');
       $.get('/chat/get_weather/',{'city':$(this).html()},
            function (resText){
                console.log($(resText));
                $('#s01').html($(resText)[0]);
                $('#s02').html($(resText)[1]);
            },
            'JSON')
    });



    $('#left').delegate('div[data-target]',
    'click',function (){
        var target = $(this).data('target');
//        console.log(target);
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
    $(document).on('click','.chat_item',function (){
        $('#right_blank,#right_news').hide()
        $('#right').show();
        var a = $(this).children('.f_name').html()
//        console.log(a)
        $('#chat_title').html(a)
    })

//    $('.news_item').click(function (){
//        $('#right_news').show();
//        $('#right_blank,#right,#right_friend').hide()
//    })
//    $(document).on('click','.friend_item',function (){
//        $('#right_friend').show();
//        $('#right_blank,#right').hide()
//        console.log($(this))
//        $.ajax({
//            data:$(this).children('h4').html(),
//            type:'GET',
//            url:'/chat/detial_info',
//            dataType:'json',
//            success:function (resText){
//                console.log('~~~~')
//                $('#detial').children('img').attr('src',resText.frofile_head);
//                $('#detial').children('h2').html(resText.nickname);
//                $('#detial').children('#u_01').html(resText.profile);
//                $('#detial').children('#u_02').html(resText.username);
//                $('#detial').find('#u_03').html(resText.sex);
//                $('#detial').find('#u_04').html(resText.birthday);
//                $('#detial').children('#u_05').html(resText.address);
//            }
//        })
//
//    })














})