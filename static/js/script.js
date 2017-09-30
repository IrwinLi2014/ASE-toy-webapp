$(document).ready(function() {
	$("#add").click(function() {
		var ticker = $('input[name="st"]').val();
		$.post("add_stock", {"ticker": ticker}, function(data) {
			alert(data);
			for (var i = 0; i < data.length; i++) {
				$(".stocks").append("<p>"+stocks[i]+"</p>");
			}
		});
	});
});