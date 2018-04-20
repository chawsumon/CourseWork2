$(function(){
	var order_num = $('#order_num').text();
	$.getJSON('/order/'+order_num,function(d){
		$('#debug').text(d);
		for(var i = 0;i<d.length;i++){
			var tr = $('<tr/>')
			    .append($('<td/>',{text:d[i][0]}))
				.append($('<td/>',{text:d[i][1]}))
				.append($('<td/>',{text:d[i][2]}))
				.append($('<td/>',{text:d[i][3]}))
				.appendTo('#order_list')
		}

});

$('#addToOrder').click(function(){
	var item = $('#new_product').val();
	var order_num = $('#order_num').text();
	$.ajax({url:'/order/'+order_num+'/'+item,method:"POST"});
})
});