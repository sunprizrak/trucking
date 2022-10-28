function validate_form() {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  let forms = document.querySelectorAll('.needs-validation');

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add('was-validated');
      }, false)
    });
}

function validate_modal_form() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = document.querySelectorAll('.modal .needs-validation');
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            if (!form.checkValidity()) {
                e.stopPropagation();
                form.classList.add('was-validated');
            } else {
                let valid_form = $(this).serialize();
                let id_form = '#' + $(this).attr('id');
                $.ajax({
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    type: 'POST',
                    data: valid_form,
                    success: function(data) {
                        if (data.result == true) {
                            $(id_form + ' button[name=close_modal_form]').click();
                            let myAlert = $('<div' +
                                                 ' class="alert alert-success' +
                                                    ' d-flex align-items-center position-absolute' +
                                                    ' top-50 start-50 animate__animated animate__backInDown">' +
                                                 '<i class="fa-solid fa-circle-check"' +
                                                 ' style="margin-right: 0.5rem; font-size: 1.5rem;"></i>' +
                                                 '<div>Ставка запрошена успешно!</div>' +
                                             '</div>')
                            $('body main').append(myAlert).delay(5000).queue(function() {
                                $('body main .alert').remove();
                                $(this).dequeue();
                            });
                        } else {
                           $(id_form + ' .captcha-error').css('display', 'block');
                        }
                    }
                });
            }
        }, false);
    });
}

function clear_modal_form() {
    $('form button[name=close_modal_form]').on('click', function() {
        let form = $(this).parents('form');
        form[0].reset();
        if (form.hasClass('was-validated')) {
            form.removeClass('was-validated');
        }
        if ($('.captcha-error').css('display') == 'block') {
            $('.captcha-error').css('display', 'none');
        }
    });
}

$(function () {
    validate_form();
    validate_modal_form();
    clear_modal_form();
});
