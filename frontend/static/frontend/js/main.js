'use strict';
/**
 * Fixed navbar when scrolling
 */

function fixToTop() {
  var menu = $('.navbar');
  var logo = $('.navbar-logo');
  var list = $('.navbar-nav>li>a');

  menu.addClass('navbar-fixed-top').addClass('navbar-fixed');
  logo.removeClass('navbar-logo').addClass('navbar-logo-fixed');
  list.css('padding-top', 0);
}

$(window).scroll(function () {
  var menu = $('.navbar');
  if ($(window).scrollTop() >= menu.offset().top) {
    fixToTop();
  } else {
    menu.removeClass('navbar-fixed-top');
  }
});
/**
 * Search by Muluneh Awoke
 * https://codepen.io/muluneh/pen/doZdEx
 */
(function($) {

  $('#search-button').on('click', function(e) {
    if($('#search-input-container').hasClass('hdn')) {
      e.preventDefault();
      $('#search-input-container').removeClass('hdn')
      return false;
    }
  });

  $('#hide-search-input-container').on('click', function(e) {
    e.preventDefault();
    $('#search-input-container').addClass('hdn')
    return false;
  });

})(jQuery);
