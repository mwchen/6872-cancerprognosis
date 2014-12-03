$(document).ready(function () {
    document.getElementById('results-container').style.display = 'none';
    document.getElementById('treatment-container').style.display = 'None';
});

$('#look-up-form').on('submit', function(event) {
	event.preventDefault();
	look_up();
});

$('#pdf-button').click(function(){
 		window.location.href = "../../pdf?stage="+$('#id_stage').val()+'&gender='+$('#id_gender').val()+'&age='+$('#id_age').val() +'&cancer='+$('#id_cancer').val();
		
});

$('#clinical-trial-button').click(function(){
	$.ajax({
        url : "../lookup/", // the endpoint
        type : "POST", // http method
        data: { csrfmiddlewaretoken: "{{ csrf_token }}", 'stage':$('#id_stage').val(), 'gender':$('#id_gender').val(), 
        	'age':$('#id_age').val(), 'cancer':$('#id_cancer').val()},
        	
       // data : { lookup : $('#look-up-form').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
        
        	if(json['age'] < 16){
        	age = '0';
        	}
        	else if(json['age'] < 65){
        	age  = '1';
        	}
        	else{
        	age = '2';
        	}
        	numt = json['stage'] - 1;
        	window.location.href = 'https://clinicaltrials.gov/ct2/results?term='+json['cancer']+'+cancer&recr=&rslt=&type=&cond=&intr=&titles=&outc=&spons=&lead=&id=&state1=&cntry1=&state2=&cntry2=&state3=&cntry3=&locn=&gndr=&age='+age+'&phase='+String((numt))+'&rcv_s=&rcv_e=&lup_s=&lup_e='

            //$('#look-up-form').val(''); // remove the value from the input
            
        },

    });
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
            document.getElementById('treatment-container').style.display = 'None';
         },
        	
       // data : { lookup : $('#look-up-form').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
        	$('#wait').hide();
            //$('#look-up-form').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            document.getElementById('results-container').style.display = 'block';
            document.getElementById('treatment-container').style.display = 'block';
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
            // Clear the previous treatments.
            document.getElementById('treatments').innerHTML ="";
            
            // Iterate through the treatments for this type of cancer.
            var treatmentOptions = result[key];
            for (i=0; i < treatmentOptions.length; i++) {
                var currentTreatment = treatmentOptions[i];
                var treatmentDiv = document.createElement('div');
                treatmentDiv.className = "row treatment";

                // Add treatment name.
                var treatmentName = document.createElement('div');
                treatmentName.innerHTML="<div class='field-heading'> Treatment "+ (i+1) + ": </div>" + currentTreatment['name'];
                treatmentName.className = "treatment-name text col-md-4";

                // Add treatment cost.
                var treatmentCost = document.createElement('div');
                treatmentCost.innerHTML="<div class='field-heading'> Cost: </div>" + currentTreatment['cost'];
                treatmentCost.className = "treatment-cost text col-md-4";

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
                treatmentQOL.className = "treatment-quality-of-life text col-md-3";

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
    $("#mainChart").replaceWith("<canvas id='mainChart'></canvas>");
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
    var myNewChart = new Chart(ctx).Line(data);
}
