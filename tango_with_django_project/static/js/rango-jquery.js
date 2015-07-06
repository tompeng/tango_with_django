$(document).ready(function() {

        // JQuery code to be added in here.

        $('#likes').click(function() {
        	var catid;
        	catid = $(this).attr("data-catid");
        	$.get(
        		'/rango/like_category/',
        		{category_id:catid},
        		function(data) {
        			$('#like_count').html(data);
        			$('#likes').hide();
        		});
        });

        $('#suggestion').keyup(function(){
        	var query;
        	query = $(this).val();
        	$.get('/rango/suggest_category/', {suggestion: query}, function(data){
        		$('#cats').html(data);
        	});
        });

        $('.rango-add').click(function() {
        	var catid = $(this).attr("data-catid");
        	var link = $(this).attr("data-link");
        	var title = $(this).attr("data-title");
        	$.get('/rango/auto_add/', {catid: catid, link: link, title: title}, function(data){
        		$('.pages-list').html(data);
        	});
        });

    });