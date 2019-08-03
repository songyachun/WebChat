$(function(){
//    var websocket;
//    var name= '{{username}}';
    // 首先判断是否支持WebSocket
    if('WebSocket' in window){
        //收发消息
        msgsocket = new WebSocket("ws://127.0.0.1:8000/chat/friend_id");
        listsocket = new WebSocket("ws://127.0.0.1:8000/chat/friend_list");
        console.log("支持websocket")
    }else if('MozWebSocket' in window){
        msgsocket = new MozWebSocket("ws://127.0.0.1:8000/chat/friend_id");
        listsocket = new MozWebSocket("ws://127.0.0.1:8000/chat/friend_list");
    }else{
        msgsocket = new SockJS("ws://127.0.0.1:8000/chat/friend_id");
        listsocket = new SockJS("ws://127.0.0.1:8000/chat/friend_list");
    }
    // 打开连接时
    msgsocket.onopen = function(event) {
        //formatMsg("系统提示：","您已连接 ，消息提示系统！！",2000)
        console.log("您已连接 ，消息提示系统！！")
        console.log(websocket.readyState)
        console.log("222")
    };
    console.log("1111")
    //发送添加好友请求
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
                'step':0,
                'type':0})
                )
            }
        }
    });
    //发送添加好友的结果
    $('.res').click(function (){
        var status = $(this).val()
        if(!msgsocket){
            alert("Please connect server.");
        }else{
            if (msgsocket.readyState===1){
                msgsocket.send(JSON.stringify({
                'sender': $('#S').html(),
                'reciver': $('#R').html(),
                'step':3,
                'type':0,
                'status':status})
                )
            }
        }
        $('#addTips').hide()

    })

    // 收到消息时
    msgsocket.onmessage = function(event) {
        // 将json字符串转换为js对象
        var data =JSON.parse(event.data);
        // formatMsg(data.title,data.data,10000)
//        console.log(data.title)
//        console.log(data.data)
        var sender = data.sender
        var reciver = data.reciver
        //收到添加好友的请求
        if(data.type == 0 && data.step==1){
            var addTips = $('<div id="addTips"></div>')
            var addTips_html=''
            addTips_html ='<p>'+'<span id="R">'+reciver+'</span>'+'您好:'+'</p>'
            addTips_html +='<p>'+'<span id="S">'+sender+'</span>'+'请求添加您为好友,是否同意?'+'</p>'
            addTips_html +='<input class="res" id="Y" type="submit" value="是">'
            addTips_html +='<input class="res" id="N" type="submit" value="否">'
         //收到添加好友的结果
        }else if(data.type ==0 && data.step == 3){
            if(data.status == 1){
                alert(reciver+'同意您的添加!')
            }else{
                alert(reciver+'拒绝您的添加!')
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
