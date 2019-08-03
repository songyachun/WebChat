function createXhr() {
    // 根据不同的浏览器对象创建不懂的异步对象
    if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest();
        console.log('支持XMLHttpRequest')
    } else {
        xhr = new ActiveXObject('Microsoft.XMLHTTP');
        console.log('支持ActiveXObject')
    }
    return xhr;
}

