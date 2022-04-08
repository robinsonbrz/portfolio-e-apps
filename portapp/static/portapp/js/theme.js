(function($) {
	'use strict';
	
	
	/*-------------------------------------------------------------------------------
	  Navbar seleciona qual deve ser o nav class active - Robinson 03-03-2022
	-------------------------------------------------------------------------------*/
	$(".nav-item").each(function() {
	// varre itens de nav e remove a classe active
	  $(this).removeClass("active");
	});

	$(".nav-item").each(function() {
	 // varre nav e procura qual ancora possui link igual ao titulo da pag atual
	 // console.log($(this).children().text()); 
	 // console.log($("title").text().replace(" | Robinson",""));
		if ($(this).children().text() == $("title").text().replace(" | Robinson",""))  {
			$(this).addClass("active")
		}
	});
	
	

	var nav_offset_top = $('header').height() + 50;
	/*-------------------------------------------------------------------------------
	  Navbar 
	-------------------------------------------------------------------------------*/

	//* Navbar Fixed
	function navbarFixed() {
		if ($('.header_area').length) {
			$(window).scroll(function() {
				var scroll = $(window).scrollTop();
				if (scroll >= nav_offset_top) {
					$('.header_area').addClass('navbar_fixed');
				} else {
					$('.header_area').removeClass('navbar_fixed');
				}
			});
		}
	}
	navbarFixed();

	/*----------------------------------------------------*/
	/*  MailChimp Slider
    /*----------------------------------------------------*/
	function mailChimp() {
		$('#mc_embed_signup').find('form').ajaxChimp();
	}
	mailChimp();

	$('select').niceSelect();
	/* ---------------------------------------------
            Isotope js Starts
         --------------------------------------------- */
	$(window).on('load', function() {
		$('.portfolio-filter ul li').on('click', function() {
			$('.portfolio-filter ul li').removeClass('active');
			$(this).addClass('active');

			var data = $(this).attr('data-filter');
			$workGrid.isotope({
				filter: data
			});
		});

		if (document.getElementById('portfolio')) {
			var $workGrid = $('.portfolio-grid').isotope({
				itemSelector: '.all',
				percentPosition: true,
				masonry: {
					columnWidth: '.all'
				}
			});
		}
	});

	/*----------------------------------------------------*/
	/* Start Magnific Pop Up
	/*----------------------------------------------------*/
	if ($('.img-gal').length > 0) {
		$('.img-gal').magnificPopup({
			type: 'image',
			gallery: {
				enabled: true
			}
		});
	}
	/*----------------------------------------------------*/
	/*  End  Magnific Pop Up
	/*----------------------------------------------------*/

	/*----------------------------------------------------*/
	/*  Testimonials Slider
    /*----------------------------------------------------*/
	function testimonials_slider() {
		if ($('.testi_slider').length) {
			$('.testi_slider').owlCarousel({
				loop: true,
				margin: 30,
				items: 2,
				autoplay: true,
				smartSpeed: 2500,
				dots: true,
				responsiveClass: true,
				responsive: {
					0: {
						items: 1
					},
					991: {
						items: 2
					}
				}
			});
		}
	}
	testimonials_slider();

	/*----------------------------------------------------*/
	/*  Google map js
    /*----------------------------------------------------*/

	if ($('#mapBox').length) {
		var $lat = $('#mapBox').data('lat');
		var $lon = $('#mapBox').data('lon');
		var $zoom = $('#mapBox').data('zoom');
		var $marker = $('#mapBox').data('marker');
		var $info = $('#mapBox').data('info');
		var $markerLat = $('#mapBox').data('mlat');
		var $markerLon = $('#mapBox').data('mlon');
		var map = new GMaps({
			el: '#mapBox',
			lat: $lat,
			lng: $lon,
			scrollwheel: false,
			scaleControl: true,
			streetViewControl: false,
			panControl: true,
			disableDoubleClickZoom: true,
			mapTypeControl: false,
			zoom: $zoom,
			styles: [
				{
					featureType: 'water',
					elementType: 'geometry.fill',
					stylers: [
						{
							color: '#dcdfe6'
						}
					]
				},
				{
					featureType: 'transit',
					stylers: [
						{
							color: '#808080'
						},
						{
							visibility: 'off'
						}
					]
				},
				{
					featureType: 'road.highway',
					elementType: 'geometry.stroke',
					stylers: [
						{
							visibility: 'on'
						},
						{
							color: '#dcdfe6'
						}
					]
				},
				{
					featureType: 'road.highway',
					elementType: 'geometry.fill',
					stylers: [
						{
							color: '#ffffff'
						}
					]
				},
				{
					featureType: 'road.local',
					elementType: 'geometry.fill',
					stylers: [
						{
							visibility: 'on'
						},
						{
							color: '#ffffff'
						},
						{
							weight: 1.8
						}
					]
				},
				{
					featureType: 'road.local',
					elementType: 'geometry.stroke',
					stylers: [
						{
							color: '#d7d7d7'
						}
					]
				},
				{
					featureType: 'poi',
					elementType: 'geometry.fill',
					stylers: [
						{
							visibility: 'on'
						},
						{
							color: '#ebebeb'
						}
					]
				},
				{
					featureType: 'administrative',
					elementType: 'geometry',
					stylers: [
						{
							color: '#a7a7a7'
						}
					]
				},
				{
					featureType: 'road.arterial',
					elementType: 'geometry.fill',
					stylers: [
						{
							color: '#ffffff'
						}
					]
				},
				{
					featureType: 'road.arterial',
					elementType: 'geometry.fill',
					stylers: [
						{
							color: '#ffffff'
						}
					]
				},
				{
					featureType: 'landscape',
					elementType: 'geometry.fill',
					stylers: [
						{
							visibility: 'on'
						},
						{
							color: '#efefef'
						}
					]
				},
				{
					featureType: 'road',
					elementType: 'labels.text.fill',
					stylers: [
						{
							color: '#696969'
						}
					]
				},
				{
					featureType: 'administrative',
					elementType: 'labels.text.fill',
					stylers: [
						{
							visibility: 'on'
						},
						{
							color: '#737373'
						}
					]
				},
				{
					featureType: 'poi',
					elementType: 'labels.icon',
					stylers: [
						{
							visibility: 'off'
						}
					]
				},
				{
					featureType: 'poi',
					elementType: 'labels',
					stylers: [
						{
							visibility: 'off'
						}
					]
				},
				{
					featureType: 'road.arterial',
					elementType: 'geometry.stroke',
					stylers: [
						{
							color: '#d6d6d6'
						}
					]
				},
				{
					featureType: 'road',
					elementType: 'labels.icon',
					stylers: [
						{
							visibility: 'off'
						}
					]
				},
				{},
				{
					featureType: 'poi',
					elementType: 'geometry.fill',
					stylers: [
						{
							color: '#dadada'
						}
					]
				}
			]
		});
	}

		// Somente em todo app  #######################
        // alert("carregado");
        $('#id_username').attr('autocomplete', 'off');

        //$("#teste_btn").event.preventDefault();
        $("#teste_btn").on('click', function () {
            console.log("teste");

            $("#id_username").val("testuser2");
            $("#id_password").val("t3stU5er@");
            $( ".button" ).trigger('click');
        })
		// Somente em todo app  #######################


		
		
		// validação de e-mail validate #######################
		//Guarda o form em uma variável
		var form = $("#contactForm");
		$('#contactForm').validate({
			// regras pode se colocar regra de required aqui ao invés de no HTML
			// length também pode ser inserido aqui

			rules: {
				name: {
					required: true,
					minlength: 5
				},
				// valida se senha 1 é igual a senha 2
				email: {
					required: true
				},
				subject: {
					required: true,
					minlength: 15
				},
				// valida se senha 1 é igual a senha 2
				message: {
					required: true,
					minlength: 20
				}
			},
			// mensagens da validação 
			messages: {
				name: {
					required: "Precisamos de seu nome para contato"
					
				},
				email: {
					required: "Campo email é necessário",
					email: "Digite um email válido"
				},
				subject: {
					required: "Breve descrição",
					minlength: "no mínimo {0} caracteres"
				},
				message: {
					required: "Descreva como posso te ajudar",
					minlength: "no mínimo {0} caracteres"
				}

			}
		})
// validação de e-mail validate #######################




		// envio de email ajax form inicial #######################
		$('#contactForm').on('submit', function(event){
			event.preventDefault();
			//console.log("form submitted!")  // sanity check
			if (form.valid()) {
				create_post();
			};
		});
	
		// AJAX for posting
		function create_post() {
			//console.log("create post is working!") // sanity check
			let nome    = $('#name').val();
			let email   = $('#email').val();
			let subject = $('#subject').val();
			let message = $('#message').val();

			$.ajax({
				type : "POST", // http method
				url : "enviaemail/", // the endpoint
				data : { 
					name    : nome    , 
					email   : email   ,
					subject : subject ,
					message : message ,
					csrfmiddlewaretoken : $('input[name = csrfmiddlewaretoken]').val(),
						}, // data sent with the post request
				// handle a successful response
				success : function(json) {
					// console.log(json); // log the returned json to the console
					// console.log("success"); // another sanity check
					$("#alert-email").addClass("alert-success").removeClass("d-none").removeClass("alert-danger")
					$("#alert-email").html("Muito obrigado <b>" + nome + "</b> !<br>Breve você receberá uma resposta em: " + email+ ".");

					//d-none" role="alert" id="alert-email"
					alert("Obrigado " + nome + "! Sua mensagem foi enviada!");
					$('#name').val(''); // remove the value from the input
					$('#email').val(''); 
					$('#subject').val('');
					$('#message').val('');

				},
		
				// handle a non-successful response
				error : function(xhr,errmsg,err) {
					$("#alert-email").addClass("alert-danger").removeClass("d-none").removeClass("alert-success")
					$("#alert-email").html("Desculpe! <br>Erro no processamento! <br> Por favor, tente novamente mais tarde.")
			
					console.log("Erro apresentado: "+ err);
					console.log("Erro apresentado: "+ errmsg);
				}
			});






		};


		// envio de email ajax #######################




})(jQuery);
