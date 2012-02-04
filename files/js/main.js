$().ready(function() {
	$('.info').hide();

	var timer
	$('.post-title').hover(function() {
		$('.info').hide();
		clearTimeout(timer);
		$info = $(this).next();
		timer = setTimeout(function(){$info.slideDown(90);},350);
	}, function() {
		clearTimeout(timer);
		$info = $(this).next();
		timer = setTimeout(function(){$info.slideUp(90);},1500);
	});
});
