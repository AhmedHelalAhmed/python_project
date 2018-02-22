		window.onscroll = function() {scrollFunction()};

	function scrollFunction() {
	    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
	        document.getElementById("myBtn").style.display = "block";
	    } else {
	        document.getElementById("myBtn").style.display = "none";
	    }
	}

	// When the user clicks on the button, scroll to the top of the document
	function topFunction() {
	    document.body.scrollTop = 0; // For Safari
	    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
	} 


$(".sub").on("click",function(e){
	e.preventDefault()
		$.ajax({
				type : 'GET',
				url : '/bloggawy/create',
				data : {
					category : $(this).attr("name"),
					user : $(this).attr("id"),
					type : $(this).html()
				}
				// dataType : 'json',
			});
	});	

	$(".sub").on("click",function(e){
		var text = $(this).html()
		if(text == 'Subscribe')
		{
			$(this).html('UnSubscribe')
		}
		else if(text == 'UnSubscribe')
		{
			$(this).html('Subscribe')
		}
			
	});

