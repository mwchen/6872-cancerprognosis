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
        data: { csrfmiddlewaretoken: "{{ csrf_token }}", 'stage':$('#id_stage').val(), 'gender':$('#id_gender').val(), 
        	'age':$('#id_age').val(), 'cancer':$('#id_cancer').val()},
        beforeSend: function() { 
        $('#wait').show();
        document.getElementById('results-container').style.display = 'None';
        
        
         },
        	
        
        
       // data : { lookup : $('#look-up-form').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            //$('#look-up-form').val(''); // remove the value from the input
            $('#wait').hide();
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
                treatmentName.innerHTML="<div class='field-heading'> Treatment: </div>" + currentTreatment['name'];
                treatmentName.className = "treatment-name col-md-4";

                // Add treatment cost.
                var treatmentCost = document.createElement('div');
                treatmentCost.innerHTML="<div class='field-heading'> Cost: </div>" + currentTreatment['cost'];
                treatmentCost.className = "treatment-cost col-md-4";

                // Add treatment quality of life.
                var treatmentQOL = document.createElement('div');
                treatmentQOL.innerHTML = "<div class='field-heading'> Quality of Life: </div>";
                if( currentTreatment['quality_of_life'] == 2){
                
                treatmentQOL.innerHTML += '<i class="fa fa-smile-o fa-2x"></i>';
                }
                if( currentTreatment['quality_of_life'] == 1){
                
                treatmentQOL.innerHTML += '<i class="fa fa-meh-o fa-2x"></i>';
                }
                if( currentTreatment['quality_of_life'] == 0){
                
                treatmentQOL.innerHTML += '<i class="fa fa-frown-o fa-2x"></i>';
                }
                treatmentQOL.className = "treatment-quality-of-life col-md-3";

                // Add graph for treatment.
                var treatmentData = get_data(currentTreatment);
                var canvas = document.createElement('canvas');
                canvas.className = "col-md-4";
                canvas.setAttribute("id", "treatment-chart-" + i);

                treatmentDiv.appendChild(treatmentName);
                treatmentDiv.appendChild(treatmentCost);
                treatmentDiv.appendChild(treatmentQOL);
                treatmentDiv.appendChild(canvas);

                document.getElementById('treatments').appendChild(treatmentDiv);
                create_chart("#treatment-chart-"+i, treatmentData);
            }
        }

        // If it is another field (not a treatment), fill it in accordingly.
        else if (document.getElementById(key) != null) {
            var child = document.getElementById(key);
            if (child.childNodes.length > 3) {
                child.removeChild(child.lastChild);
            }
            child.innerHTML += "<div class='field-text'>" + value + "</div>";
        }
    });

    // Add the years to create the main graph.
    data = get_data(result);
    create_chart("#mainChart", data);
}

function get_data(input_array) {    
    var data = { 
        labels: ["1 year", "2 years", "3 years", "4 years", "5+ years"],
        datasets: [
            {
                label:"expected",
                fillColor: "#3E606F",
                data:[input_array['1year'],input_array['2year'],input_array['3year'],input_array['4year'],input_array['5year']]
            }
        ]
    };
    return data;
}

// Create a chart at the expected location with a particular dataset.
function create_chart(location, data) {
    var ctx = $(location).get(0).getContext("2d");
    console.log($(location).get(0).getContext("2d"));
    var myNewChart = new Chart(ctx).Line(data);
}