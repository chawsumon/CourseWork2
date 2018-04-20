$(function(){
	$('#queue').text("waiting for results");
	setInterval(refreshQueue,5000);
});

function refreshQueue(){
	$.getJSON('/getQueue',function(d){
		$('#queue').empty();
		for (var i = 0; i <d.length; i++) {
			$('<div/>')
				.append($('<span/>',{text:d[i][0] + " " + d[i][1]}))
				.appendTo('#queue');
				$("span:contains('processing')").css("background-color","gray");
				$("span:contains('processing')").css("color","white");
				
		}
	})
}