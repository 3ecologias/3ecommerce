/*-----------------------------------------------------------------------------------
/*
/* Init JS
/*
-----------------------------------------------------------------------------------*/
jQuery(document).ready(function($) {

/*---------------------------------------------------- */
/* Preloader
------------------------------------------------------ */
  	$(window).load(function() {

   	// will first fade out the loading animation
    	$("#status").fadeOut("slow");

    	// will fade out the whole DIV that covers the website.
    	$("#preloader").delay(500).fadeOut("slow").remove();

  	})

/*---------------------------------------------------- */
/* Menu
------------------------------------------------------ */
  	var toggle_button = $("<a>", {
                        id: "toggle-btn",
                        html : "Menu",
                        title: "Menu",
                        href : "#" }
                        );
  	var nav_wrap = $('nav#nav-wrap')
  	var nav = $("ul#nav");

  	/* id JS is enabled, remove the two a.menu-btns
  	and dynamically prepend a.toggle-btn to #nav-wrap */
  	nav_wrap.find('a.menu-btn').remove();
  	nav_wrap.prepend(toggle_button);

  	toggle_button.on("click", function(e) {
   	e.preventDefault();
    	nav.slideToggle("fast");
  	});

  	if (toggle_button.is(':visible')) nav.addClass('mobile');
  	$(window).resize(function(){
   	if (toggle_button.is(':visible')) nav.addClass('mobile');
    	else nav.removeClass('mobile');
  	});

  	$('ul#nav li a').on("click", function(){
   	if (nav.hasClass('mobile')) nav.fadeOut('fast');
  	});


/*----------------------------------------------------*/
/* Backstretch Settings
------------------------------------------------------ */

	$("#intro").backstretch("../images/header-background.jpg");


/*----------------------------------------------------*/
/*	Back To Top Button
/*----------------------------------------------------*/
	var pxShow = 300; //height on which the button will show
	var fadeInTime = 400; //how slow/fast you want the button to show
	var fadeOutTime = 400; //how slow/fast you want the button to hide
	var scrollSpeed = 300; //how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'

   // Show or hide the sticky footer button
	jQuery(window).scroll(function() {

		if (jQuery(window).scrollTop() >= pxShow) {
			jQuery("#go-top").fadeIn(fadeInTime);
		} else {
			jQuery("#go-top").fadeOut(fadeOutTime);
		}

	});


/*----------------------------------------------------*/
/*  Placeholder Plugin Settings
------------------------------------------------------ */
	$('input, textarea').placeholder()


/*----------------------------------------------------*/
/* FitText Settings
------------------------------------------------------ */
   setTimeout( function() {

	  //  $('h1.responsive-headline').fitText(1, { minFontSize: '40px', maxFontSize: '90px' });

   }, 100);

/*----------------------------------------------------*/
/* Final Countdown Settings
------------------------------------------------------ */
	var finalDate = '2016/01/01';

	$('div#counter').countdown(finalDate)
   	.on('update.countdown', function(event) {

   		$(this).html(event.strftime('<span>%D <em>days</em></span>' +
   										 	 '<span>%H <em>hours</em></span>' +
   										 	 '<span>%M <em>minutes</em></span>' +
   										 	 '<span>%S <em>seconds</em></span>'));

   });


/*----------------------------------------------------*/
/* Smooth Scrolling
------------------------------------------------------ */

   $('.smoothscroll').on('click',function (e) {
	    e.preventDefault();

	    var target = this.hash,
	    $target = $(target);

	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, 800, 'swing', function () {
	        window.location.hash = target;
	    });
	});


/*----------------------------------------------------*/
/* Highlight the current section in the navigation bar
------------------------------------------------------*/

	var sections = $("section");
	var navigation_links = $("#nav-wrap a");

	sections.waypoint({

      handler: function(event, direction) {

		   var active_section;

			active_section = $(this);
			if (direction === "up") active_section = active_section.prev();

			var active_link = $('#nav-wrap a[href="#' + active_section.attr("id") + '"]');

         navigation_links.parent().removeClass("current");
			active_link.parent().addClass("current");

		},
		offset: '35%'

	});


/*----------------------------------------------------*/
/*	Make sure that #intro height is
/* equal to the browser height.
------------------------------------------------------ */

   $('#intro, #map').css({ 'height': $(window).height() });
   $(window).on('resize', function() {

        $('#intro, #map').css({ 'height': $(window).height() });
        $('body').css({ 'width': $(window).width() })

        $("#intro").backstretch("../images/header-background.jpg");
   });


   /*----------------------------------------------------*/
   /*	https://github.com/desandro/masonry/
   /* Mansory
   ------------------------------------------------------ */
    var $grid = $('.grid').masonry({
      itemSelector: '.grid-item',
      percentPosition: true,
      columnWidth: '.grid-sizer'
    });
    // layout Isotope after each image loads
    $grid.imagesLoaded().progress( function() {
      $grid.masonry();
    });


    $("#itens").slider({
    range: "min",
    value: 3000,
    step: 100,
    min: 100,
    max: 50000,
    slide: function( event, ui ) {
        $( ".slider" ).val( ui.value + " itens");
    }
  });


  $(".slider").change(function () {
      var value = this.value.substring(1);
      console.log(value);
      $("#itens").slider("value", parseInt(value));
  });

  $(".switch-wrapper").switchButton({
          on_label: 'Sim',
          off_label: 'Não',
          width: 30,
          height: 20,
          button_width: 20
        }

  );



});
