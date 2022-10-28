$(function() {
    let alertList = document.querySelectorAll('.alert');
    alertList.forEach(function (alert) {
        let myAlert = new bootstrap.Alert(alert);
        $(myAlert).delay(3100).queue(function() {
            myAlert.close();
            $(this).dequeue();
        });
    });
});