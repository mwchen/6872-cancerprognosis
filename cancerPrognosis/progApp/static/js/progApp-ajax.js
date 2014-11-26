function updateFields(json_data) {
	$.getJSON(json_data, function(data) {
		console.log(data['cancer']);
	});
	console.log("yay");
}

// function updateID(json_data, id){
//     var result = {{json_data|safe}};
//     var paragraph = document.createElement('p');
//     var cancerText = document.createTextNode(result['cancer']);
//     paragraph.appendChild(cancerText);

//     // Replace the cancer type.
//     var child = document.getElementById('cancerText')
//     document.getElementById('main').replaceChild(paragraph, child);
//     console.log(result['cancer']);
// };
