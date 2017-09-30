$(document).ready(function() {
	$("#add").click(function() {
		var ticker = $('input[name="st"]').val();
		$.post("add_stock", {"ticker": ticker}, function(data) {
			alert(data);
		});
	});
});