$(function(){
//    var websocket;
//    var name= '{{username}}';
    // 首先判断是否支持WebSocket
    if('WebSocket' in window){
        //处理收发消息
        msgsocket = new WebSocket("ws://176.140.10.222:8000/chat/friend_id");
        //处理接收好友列表
        // listsocket = new WebSocket("ws://176.140.10.222:8000/chat/friend_list");
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
                'dataType':0})
                )
            }
        }
    });

    //    发送添加好友的结果
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
            if (msgsocket.readyState===1){
                msgsocket.send(JSON.stringify({
                'sender': $('#S').html(),
                'reciver': $('#R').html(),
                'step':2,
                'dataType':0,
                'status':status})
                )
            }
        }
        $('#addTips').remove()
    })


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
        //收到添加好友的请求
        if(data.dataType == '0' && data.step== '1'){
            var addTips = $('<div id="addTips"></div>')
            $('body').append(addTips)
            console.log('====111====')
            var addTips_html=''
            addTips_html ="<p>"+"<span id='R'>"+reciver+"</span>"+"您好:"+"</p>"
            addTips_html +='<p>'+'<span id="S">'+sender+'</span>'+'请求添加您为好友,是否同意?'+'</p>'
            addTips_html +='<input class="res" id="Y" type="submit" value="是">'
            addTips_html +='<input class="res" id="N" type="submit" value="否">'
            console.log(addTips_html)
            addTips.html(addTips_html)
         //收到添加好友的结果
        }else if(data.dataType == '0' && data.step == '3'){
            if(data.status == '1' ){
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