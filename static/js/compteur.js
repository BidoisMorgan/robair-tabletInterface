$(function() {

if (document.body){
  var larg = (document.body.clientWidth);
  var haut = (document.body.clientHeight);
  if (larg + haut >1000){
	var note = $('#note'), ts = new Date(2012, 0, 1), newYear = true;

	if ((new Date()) > ts) {
		// in this case 10*24*60*60*1000 represent 10j 24h 60' 60"
		// IMPORTANT : ne pas supprimer le *1000
		ts = (new Date()).getTime() + 1 * 2 * 60 * 60 * 1000;
		newYear = false;
	}

	$('#countdown').countdown({
		timestamp : ts,
		callback : function(days, hours, minutes, seconds) {

			var message = "";
			message += hours + " hour" + (hours == 1 ? '' : 's' ) + ", ";
			message += minutes + " min" + (minutes == 1 ? '' : 's' ) + " and ";
			//message += seconds + " sec" + (seconds == 1 ? '' : 's' ) + " <br />";

			if (newYear) {
				message += "jusqu a la fin";
				// date
			} else {
				message += ".";
			}

			note.html(message);
		}
	});
     }
  }
}); 
