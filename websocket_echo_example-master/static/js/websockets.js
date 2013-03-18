$(document).ready(function() {

	if ("WebSocket" in window) {
		var loc = window.location, new_uri;
		if (loc.protocol === "https:") {
			new_uri = "wss:";
		} else {
			new_uri = "ws:";
		}
		new_uri += "//" + loc.host;
		new_uri += loc.pathname + "/api";
		ws = new WebSocket(new_uri);
		ws.onmessage = function(msg) {
			$("#log").append("<p>" + msg.data + "</p>")
		};
	} else {
		alert("WebSocket not supported");
	}
});

function goTop() {
	ws.send($('#top').val())
	return true;
}

function goRight() {
	ws.send($('#right').val())
	return true;
}
function goBack() {
	ws.send($('#back').val())
	return true;
}
function goLeft() {
	ws.send($('#left').val())
	return true;
}
