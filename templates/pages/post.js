$.post({
    'url': '{% url "kshapp:delete-patient" %}',
    'data': {
        'action': 'delete-patient',
        'patientID': patientID
    },
    'success': function (response) {
        alert('test')
        response = JSON.parse(response);
        if (response.status == '1') {
            // success
            //alertPopup(response.title, response.message, 'success', 'Close', 'window.location.href=""');
        } else {
            // failed
            //alertPopup(response.title, response.message, 'danger', 'Close');
        }
    },
    'error': function () {
        alert("Server Error");
    }
});