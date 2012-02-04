$(document).ready(function() {
	var slideWidth = 560;
	var slides = $('.slide');
	var count = slides.length;
    //Make a random number, between 1 and count
    var start = 1 + Math.floor(Math.random() * (count - 1));
	var current= start;

    slides.hide();
    $("#slide-" + start).show();

    $("#previous").click(function(event) {
        event.preventDefault();
        $("#slide-" + current).hide();
        if (current + 1 <= count) {
            current += 1;
        } else {
            current = 1;
        }
        $("#slide-" + current).fadeIn();
    });

    $("#next").click(function(event) {
        event.preventDefault();
        $("#slide-" + current).hide();
        if (current - 1 >= 1) {
            current -= 1;
        } else {
            current = count;
        }
        $("#slide-" + current).fadeIn();
    });
});
