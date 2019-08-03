$(function(){
//    var websocket;
//    var name= '{{username}}';
    // 首先判断是否支持WebSocket
    if('WebSocket' in window){
        websocket = new WebSocket("ws://127.0.0.1:8000/chat/friend_id");
        console.log("支持websocket")
    }else if('MozWebSocket' in window){
        websocket = new MozWebSocket("ws://127.0.0.1:8000/chat/ws");
    }else{
        websocket = new SockJS("ws://127.0.0.1:8000/chat/ws");
    }
    // 打开连接时
    websocket.onopen = function(event) {
        //formatMsg("系统提示：","您已连接 ，消息提示系统！！",2000)
        console.log("您已连接 ，消息提示系统！！")
        console.log(websocket.readyState)
        console.log("222")
    };
    console.log("1111")
    //发送消息
    $('#send_message').click(function(){
            if(!websocket){
                alert("Please connect server.");
            }else{
                console.log(websocket.readyState)
                //添加状态判断，当为OPEN时，发送消息
                if (websocket.readyState===1){
                    websocket.send(JSON.stringify({
                    "sender":"news",
                    "reciver":"Andy",
                    "step":"0",
                    "type":"0"
                    })
                    )
                }
            }
    });
    $('#send_message1').click(function(){
            if(!websocket){
                alert("Please connect server.");
            }else{
                console.log(websocket.readyState)
                //添加状态判断，当为OPEN时，发送消息
                if (websocket.readyState===1){
                    websocket.send(JSON.stringify({
                    "sender":"news",
                    "reciver":"Andy",
                    "step":0,
                    "type":0
                    })
                    )
                }
            }
    });
    // 收到消息时
    websocket.onmessage = function(event) {
        // console.log(event,11111)
        // 将json字符串转换为js对象
        var data =JSON.parse(event.data);
        // formatMsg(data.title,data.data,10000)
        console.log(data.title)
        console.log(data.data)
    };
    // 错误时
    websocket.onerror = function(event) {
        console.log("websocket.onerror");
    };
    // 断开连接时
    websocket.onclose = function(event) {
        alert("已断开服务器，无法接收消息提示（请重新刷新页面）")
    };
    //关闭websocket连接
    $('#close_websocket').click(function(){
        if(websocket){
            websocket.close();
        }
    });

});
