let webSocket = new WebSocket('ws://localhost:8007');
function sendMessage() {
    var message = {"messageType": "basicMessage"};
    webSocket.send(JSON.stringify(message));
}
webSocket.onmessage = function(e) { 
	var j = JSON.parse(e.data);
    console.log(j);
    if (j["messageType"]=="basicMessage") {
        console.log(j["data"]);
    }
    if (j["messageType"]=="thePart") {
        var s =
            j["data"]["name"] +
            "<br>" +
            "<img src='" + j["data"]["img_path"] + "'></img> <br>" +
            "Price: " + "$" + j["data"]["price"] + "<br>" +
            "Profit: " + "$" +
            '<div id="profit">' + j["data"]["profit"] + "</div> <br>" +
            '<button onclick="trade()">Trade</button>'
            ;
        document.getElementById('order').innerHTML = s;
        console.log(j["data"]);
    }
    if (j["messageType"]=="trade") {
        document.getElementById('order').innerHTML = "";
        document.getElementById('balance').innerHTML = j["balance"];
        document.getElementById('ordersLeftToday').innerHTML = j["ordersLeftToday"].toString();
    }
}
function autograb() {
    var message = {"messageType": "thePart", "session": document.cookie};
    webSocket.send(JSON.stringify(message));
}

function trade() {
    var message = {"messageType": "trade", "session": document.cookie};
    webSocket.send(JSON.stringify(message));
}