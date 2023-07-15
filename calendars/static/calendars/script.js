$(function() {

    function toggleChangeBtn() {
      var slideIndex = $('.slide').index($('.active'));
      $('.change-btn').removeClass('hidden');
      if (slideIndex == 0) {
        $('.prev-btn').addClass('hidden');
      } else if (slideIndex == $('.slide').length -1) {
        $('.next-btn').addClass('hidden');
      }
    }

    $(function() {
      var date = new Date();
      var month = date.getMonth() + 1;

      var className = ".slide-" + month;

      $(className).addClass('active');
      toggleChangeBtn();
    });

    $('.hide-btn').click(function() {
      $('.form-view').hide();
    });

    $('.number-btn').click(function() {
      $('.active').removeClass('active');
      var clickedIndex = $('.number-btn').index($(this));
      $('.slide').eq(clickedIndex).addClass('active');
      toggleChangeBtn();
    });
    
    $('.change-btn').click(function() {
      var $displaySlide = $('.active');
      $displaySlide.removeClass('active');
      if ($(this).hasClass('next-btn')) {
        $displaySlide.next().addClass('active');
      } else {
        $displaySlide.prev().addClass('active');
      }
      toggleChangeBtn();
    });

    $('#show-form-btn').click(function() {
      $('#form-container').show();
    });

    $('.data-in-calendar').click(function() {
      $('.data-details').hide();
      
      var dataClicked = $(this).attr('id');
      dataDisplayed = "#data-details-"+dataClicked;
      $(dataDisplayed).show();
    });
  
});