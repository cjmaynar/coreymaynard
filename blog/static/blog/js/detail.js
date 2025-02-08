$().ready(function() {
    $("a[rel=lightbox]").fancybox({
        'transitionIn'		: 'fade',
        'transitionOut'		: 'fade',
        'titlePosition' 	: 'over',
        'titleFormat'		: function(title, currentArray, currentIndex, currentOpts) {
            return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
        }
    });
    $("#id_extra").parent().hide();
    $('#contents').tableofcontents({empty: false, scope: '#post', exclude: ['h1', 'h2']});
});
