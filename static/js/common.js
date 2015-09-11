/**
 * Created by alexy on 28.05.15.
 */
$(function() {
  $('section').addClass("hidden").viewportChecker({
    classToAdd: 'visible animated fadeIn',
    offset: 100
  });

  $.validator.messages.required = "* поле обязательно для заполнения";
  $( ".ticket-1 form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      },
      email: {
        required: true
      },
    },
    submitHandler: function(e) {
      $('.ticket-1 form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('form').trigger('reset');
          }
      });
    }
  });
  $( ".ticket-2 form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      },
      email: {
        required: true
      },
    },
    submitHandler: function(e) {
      $('.ticket-2 form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('form').trigger('reset');
          }
      });
    }
  });
  $( ".ticket-3 form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      },
      email: {
        required: true
      },
    },
    submitHandler: function(e) {
      $('.ticket-3 form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('form').trigger('reset');
          }
      });
    }
  });
  $( ".ticket-form form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      },
      email: {
        required: true
      },
    },
    submitHandler: function(e) {
      $('.ticket-form form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('form').trigger('reset');
          }
      });
    }
  });

  $(".js-certificate").fancybox();

  $(document).on('click', 'a[href^=#]', function () {
    $('html, body').animate({ scrollTop:  $('a[name="'+this.hash.slice(1)+'"]').offset().top }, 300 );
    return false;
  });

  $('.js-certificate-slider').flexslider({
    animation: "slide",
    animationLoop: true,
    controlNav: false,
    itemWidth: 178,
    itemMargin: 3
  });

});