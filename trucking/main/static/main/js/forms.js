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
                let csrftoken = $.cookie('csrftoken');
                $.ajax({
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    type: 'POST',
                    data: valid_form,
                    success: function(data) {
                        if (data.result == true) {
                            clear_modal_form(id_form);
                            $(id_form + ' button[name=close_modal_form]').click();

                            let myAlert = $('<div' +
                                                 ' class="alert alert-success' +
                                                    ' d-flex align-self-center position-absolute' +
                                                    ' animate__animated animate__backInDown" style="left: 42.7%">' +
                                                 '<i class="fa-solid fa-circle-check"' +
                                                 ' style="margin-right: 0.5rem; font-size: 1.5rem;"></i>' +
                                                 '<div>Ставка запрошена успешно!</div>' +
                                             '</div>')
                            $('body main').append(myAlert).delay(3000).queue(function() {
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

function clear_modal_form(id_form) {
    let form = $(id_form);
    form[0].reset();
    localStorage.removeItem(form.attr('id'));
    if (form.hasClass('was-validated')) {
        form.removeClass('was-validated');
    }
    if ($('.captcha-error').css('display') == 'block') {
        $('.captcha-error').css('display', 'none');
    }
}

(function($) {
    $.fn.FormCache = function(options) {
        var settings = $.extend({
        }, options);

        function on_change(event) {
            var input = $(event.target);
            var key = input.parents('form').attr('id');
            var data = JSON.parse(localStorage[key]);

            if (input.attr('type') == 'radio') {
                if (input.attr('id').slice(-1) == 0) {
                    data[input.attr('name')] = true;
                } else {
                    data[input.attr('name')] = false;
                }
            } else if (input.attr('type') == 'checkbox') {
                data[input.attr('name')] = input.is(':checked');
            } else if (input.attr('type') == 'hidden') {} else {
                data[input.attr('name')] = input.val();
            }

            localStorage[key] = JSON.stringify(data);
        }

        return this.each(function() {
            var element = $(this);

            if (typeof(Storage) !== "undefined"){
                var key = element.attr('id');

                var data = false;
                if (localStorage[key]) {
                    data = JSON.parse(localStorage[key]);
                }

                if (!data) {
                    localStorage[key] = JSON.stringify({});
                    data = JSON.parse(localStorage[key]);
                }
                element.find('input, select').change(on_change);

                element.find('input, select').each(function() {
                    if ($(this).attr('type') != 'submit') {
                        var input = $(this);
                        var value = data[input.attr('name')];
                        if (input.attr('type') == 'radio') {
                            if (value) {
                                if (input.attr('id').slice(-1) == 0) {
                                    input.prop('checked', true);
                                } else {
                                    input.prop('checked', false);
                                }
                            } else {
                                if (input.attr('id').slice(-1) == 0) {
                                    input.prop('checked', false);
                                } else {
                                    input.prop('checked', true);
                                }
                            }
                        } else if (input.attr('type') == 'checkbox') {
                            if (value) {
                                input.prop('checked', true);
                            } else {
                                input.prop('checked', false);
                            }
                        } else if (input.attr('type') == 'hidden') {} else {
                            input.val(value);
                        }
                    }
                });
            }
            else {
                alert('local storage is not available');
            }
        });
    };
}(jQuery))


$(function () {
    validate_form();
    validate_modal_form();
    $('#pre_claim').FormCache();
    $('#ship_claim').FormCache();
});
