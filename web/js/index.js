var mySwiper = new Swiper ('.swiper-container', {
	// effect: "fade",
    loop: true,
	speed: 700,
	longSwipes: true,
	longSwipesRatio: 1,
	autoplay: {
		delay: 7000,
	}
});
// $(function () {
// 	/* slick setting
// 	------------------------------------- */
// 	$('.responsive').slick({
// 		arrows: false,
// 		autoplay: true,
// 		draggable: true,
// 		autoplaySpeed: 0,
// 		cssEase: 'linear',
// 		speed: 5000,
// 		pauseOnHover: false,
// 		pauseOnFocus: false,
// 		pauseOnDotsHover: false,
// 		slidesToShow: 7,
// 		slidesToScroll: 1,
// 		responsive: [
// 			{
// 				breakpoint: 1024,
// 				settings: {
// 					slidesToShow: 7,
// 					slidesToScroll: 1,
// 					infinite: true,
// 					dots: false
// 				}
// 			},
// 			{
// 				breakpoint: 767,
// 				settings: {
// 					slidesToShow: 3,
// 					slidesToScroll: 1
// 				}
// 		]
// 	});
// });