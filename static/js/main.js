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
    $('.chat_item').click(function (){
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
    $('.friend_item').click(function (){
        $('#right_friend').show();
        $('#right_blank,#right').hide()
        $.ajax({
//            data:$(this).children('h4').html(),
            type:'GET',
            url:'/chat/detial_info',
            dataType:'json',
            success:function (resText){
                console.log('~~~~')
                $('#detial').children('img').attr('src',resText.frofile_head);
                $('#detial').children('h2').html(resText.nickname);
                $('#detial').children('#u_01').html(resText.profile);
                $('#detial').children('#u_02').html(resText.username);
                $('#detial').find('#u_03').html(resText.sex);
                $('#detial').find('#u_04').html(resText.birthday);
                $('#detial').children('#u_05').html(resText.address);
            }
        })

    })

    var getDateTime = function (){
        var date = new Date();
        var y = date.getFullYear();
        var m = date.getMonth() + 1;
        m = m < 10 ? ('0' + m) : m;
        var d = date.getDate();
        d = d < 10 ? ('0' + d) : d;
        var h = date.getHours();
        h=h < 10 ? ('0' + h) : h;
        var minute = date.getMinutes();
        minute = minute < 10 ? ('0' + minute) : minute;
        var second=date.getSeconds();
        second=second < 10 ? ('0' + second) : second;
        var time= y + '-' + m + '-' + d+' '+h+':'+minute+':'+second;
        return time
    }


    $('#send_info').click(function (){
        var dateTime = getDateTime()
        var sendMsg = $('#chat_input').val()
        var msgObj ={
            sender:'11111',
            reciver:'00000',
            time:dateTime,
            msg:sendMsg
        }
        msgStr =JSON.stringify(msgObj)
        $('#chat_input').val('')
//        if(sendMsg != ''){
//            $ajax{
//                data:msgStr,
//                type:'POST',
//                'url':'',
//                contentType: "application/json;charset=utf-8",
//                dataType : "json",
//                success : function(msg) {
////                    var content = $('<div class="content"></div>')
////                    $('#right_bd').append(content)
////                    var content_div = $('<div></div>')
////                    $(content_div).html(data)
////                    var content_img = $('<img src="/static/images/timg.jpeg">')
////                    $('.content').append(content_img)
////                    $('.content').append(content_div)
//                    console.log('成功')
//                },
//                error : function(msg) {
//                    console.log('失败')
//                }
//            }
//        }else{
//            alert('内容不能为空!')
//        }



    })




})