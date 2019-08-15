$(function(){
//    var websocket;
//    var name= '{{username}}';
    // 首先判断是否支持WebSocket
    if('WebSocket' in window){
        //处理收发消息
        msgsocket = new WebSocket("ws://176.140.10.222:8000/chat/friend_id");
        //处理接收好友列表
        listsocket = new WebSocket("ws://176.140.10.222:8000/chat/friend_list");
        console.log("支持websocket")
    }else if('MozWebSocket' in window){
        msgsocket = new MozWebSocket("ws://176.140.10.222:8000/chat/friend_id");
        listsocket = new MozWebSocket("ws://176.140.10.222:8000/chat/friend_list");
    }else{
        msgsocket = new SockJS("ws://176.140.10.222:8000/chat/friend_id");
        listsocket = new SockJS("ws://176.140.10.222:8000/chat/friend_list");
    }
    // 打开连接时
    msgsocket.onopen = function(event) {
        //formatMsg("系统提示：","您已连接 ，消息提示系统！！",2000)
//        console.log("您已连接 ，消息提示系统！！")
        console.log(msgsocket.readyState)
    };

    //开启获取好友列表的socket
    listsocket.onopen = function(event){
        console.log('开启成功')
    }

    //设置好友 data-records
    var setRecords = function (msgObj){
        var target = '#'+msgObj.reciver
            var records =$(target).attr('data-records')
            console.log(records)
            records=JSON.prase(records).push(msgObj)
            records = JSON.stringify(records)
            $(target).attr('data-records',records)
    }

    //获取时间
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

    //创建time item
    var timeItem = function (){
        var h4 = $('<h4 class="time"></h4>')
        $('#right_bd').append(h4)
        h4.html(getDateTime())
    }

    //创建content item
       //1.创建发送消息内容框
    var toContent = function (msgObj,src){
//            var div = $('<div style="width:30px;height:30px;background:#f00"></div>');
//           $("#right_bd").append(div)
//         var div=$("<div></div>");
        var div = $("<div class='to_content'><div>"+msgObj.msg+"</div><img src='"+src+"'></div>")
        var content_img = $('<img>')
//        div.addClass('to_content')
        $('#right_bd').append(div)
//        $('.to_content').append(content_div)
//        $('.to_content').append(content_img)
//        content_div.html(msgObj.msg)
//        content_img.attr('src',src)
    }

        //2.创建接收消息内容框
    var fromContent = function (data){
        var div = $("<div class='from_content'><div>"+data.msg+"</div><img src='"+src+"'></div>")
        var content_img = $('<img>')
        $('#right_bd').append(div)
    }


    //创建friend_item
    var createItem = function (friend_list){
        console.log('~~~~~~~')
        var div = $('<div></div>')
        $('#list_friend').append(div)
        var img = $('<img>')
        var h4 = $('<h4></h4>')
        div.addClass('friend_item')
        img.attr('src',friend_list.profile_head)
        h4.html(friend_list.username)
        div.append(img)
        div.append(h4)
    }


    //接收好友列表并更新
    listsocket.onmessage = function(event){
        console.log(event.data);//{'code':200,'friends':[{'username':username,...}]}
        var data = JSON.parse(event.data)
        if(data.code=='200'){
            console.log('2~~~~~')
            var friend_list = data.friends
            console.log(friend_list.length,'$$$')
            for(var i=0;i<friend_list.length;i++){
                console.log('3~~~~~~')
                createItem(friend_list[i])
            }

        }
    }


    //发送添加好友的请求
    $('#add_friend').click(function(){
        var sender = $('#user_name').html()
        var reciver = $('#search').val()
        if(!msgsocket){
            alert("Please connect server.");
        }else{
            console.log(msgsocket.readyState)
            //添加状态判断，当为OPEN时，发送消息
            if (msgsocket.readyState===1){
                msgsocket.send(JSON.stringify({
                'sender': $('#user_name').html(),
                'reciver': $('#search').val(),
                'step':'0',
                'dataType':'0'})
                )
            }
        }
    });

    // 发送添加好友的结果
    $(document).on("click",".res",function (){
        console.log('====222===')
        var status = $(this).val()
        if(status=='是'){
            status = '1'
        }else if(status=='否'){
            status = '0'
        }
        console.log(status)
        if(!msgsocket){
            alert("Please connect server.");
        }else{
            if(msgsocket.readyState===1){
                msgsocket.send(JSON.stringify({
                'sender': $('#S').html(),
                'reciver': $('#R').html(),
                'step':'2',
                'dataType':'1',
                'status':status})
                )
            }
        }
        $('#addTips').remove()
    })

    //发送聊天信息
    var sender = $('#user_name').html();
    var src = $('#user_icon').attr('src')
    $('#send_info').click(function (){
        var sendMsg = $('#chat_input').val()
        if(!sendMsg){
            alert('消息不能为空')
        }else{
            var dateTime = getDateTime();
            var reciver = $('#chat_title').html();
            var msgObj ={
                sender:sender,
                reciver:reciver,
                time:dateTime,
                msg:sendMsg,
                dataType:'2'
            };
//            setRecords(reciver,sendMsg)
            timeItem()
            toContent(msgObj,src)
            msgStr =JSON.stringify(msgObj);
            $('#chat_input').val('');
            if(!msgsocket){
                alert("Please connect server.");
            }else{
                console.log(msgsocket.readyState)
                //添加状态判断，当为OPEN时，发送消息
                if(msgsocket.readyState===1){
                    msgsocket.send(msgStr)
                }
            }
        }
    })
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


    // 收到消息时
    msgsocket.onmessage = function(event) {
        console.log(event.data)
        //{"code": 200, "sender": "Ski", "reciver": "news", "dataType": 0, "step": 1}
        // 将json字符串转换为js对象
        var data =JSON.parse(event.data);
        console.log(data,'======')
        // formatMsg(data.title,data.data,10000)
        var sender = data.sender
        var reciver = data.reciver
        console.log(data.dataType,data.step,'=====')
        //收到聊天信息
        if(data.dataType == '2'){
            fromContent(data)
        }
        //收到添加好友的请求
        if(data.dataType == '0' && data.step== '1'){
            var addTips = $('<div id="addTips"></div>')
            $('body').append(addTips)
            console.log('====111====')
            var addTips_html=''

            addTips_html ="<p>"+"<b id='R'>"+reciver+"</b>"+"您好:"+"</p>"
            addTips_html +='<p>'+'<b id="S">'+sender+'</b>'+'请求添加您为好友,是否同意?'+'</p>'
            addTips_html += '<br>'
            addTips_html +='<input class="res" id="Y" type="submit" value="是">'
            addTips_html +='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
            addTips_html +='<input class="res" id="N" type="submit" value="否">'
            console.log(addTips_html)
            addTips.html(addTips_html)
         //收到添加好友的结果
        }else if(data.dataType == '1' && data.step == '3'){
            console.log(data.status,'~~~~~~')
            if(data.status == '1' ){
                alert(reciver+'同意您的添加!')
            }else{
                alert(reciver+'拒绝您的添加!')
            }
        }

        // 刷新好友列表
        if(data.code=='200'&& data.step == '5'){
            console.log('2~~~~~')
            var friend_list = data.friends
            console.log(friend_list.length,'$$$')
            for(var i=0;i<friend_list.length;i++){
                console.log('3~~~~~~')
                createItem(friend_list[i])
            }

        }

    };



    // 错误时
    msgsocket.onerror = function(event) {
        console.log("websocket.onerror");
    };
    // 断开连接时
    msgsocket.onclose = function(event) {
        alert("已断开服务器，无法接收消息提示（请重新刷新页面）")
    };
    //关闭websocket连接
    $('#close_websocket').click(function(){
        if(websocket){
            websocket.close();
        }
    });

});