$(document).ready(function () {
    document.getElementById('results-container').style.display = 'none';
});

$('#look-up-form').on('submit', function(event) {
	event.preventDefault();
	look_up();
});

// AJAX for posting
function look_up() {
	console.log("look up is working");
	$.ajax({
        url : "../lookup/", // the endpoint
        type : "POST", // http method
        data: { csrfmiddlewaretoken: "{{ csrf_token }}"},
        //data : { lookup : $('#look-up-form').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //$('#look-up-form').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            document.getElementById('results-container').style.display = 'block';
            update_fields(json);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#error').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function update_fields(result) {
    $.each(result, function(key, value) {
        // If the key is a treatment, we want to populate the treatment.
        if (key == "treatments") {

            var treatmentOptions = result[key];
            for (i=0; i < treatmentOptions.length; i++) {
                var currentTreatment = treatmentOptions[i];
                var treatmentDiv = document.createElement('div');
                treatmentDiv.className = "row treatment";

                // Add treatment name.
                var treatmentName = document.createElement('div');
                treatmentName.innerHTML="Treatment: " + currentTreatment['name'];
                treatmentName.className = "treatment-name col-md-3";

                // Add treatment cost.
                var treatmentCost = document.createElement('div');
                treatmentCost.innerHTML="Cost: " + currentTreatment['cost'];
                treatmentCost.className = "treatment-cost col-md-3";

                // Add treatment quality of life.
                var treatmentQOL = document.createElement('div');
                treatmentQOL.innerHTML="Quality of Life: " + currentTreatment['quality_of_life'];
                treatmentQOL.className = "treatment-quality-of-life col-md-3";

                treatmentDiv.appendChild(treatmentName);
                treatmentDiv.appendChild(treatmentCost);
                treatmentDiv.appendChild(treatmentQOL);
                document.getElementById('treatments').appendChild(treatmentDiv);
            }
        }

        // If it is another field (not a treatment), fill it in accordingly.
        else if (document.getElementById(key) != null) {
            var child = document.getElementById(key);
            child.innerHTML += value;
        }
    });
}