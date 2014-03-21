var filename = "data.txt"; // The file to monitor for changes


var previous = "";
setInterval(function() {
  var ajax = new XMLHttpRequest();
  ajax.onreadystatechange = function() {
    if(ajax.readyState == 4) {
      if(ajax.responseText != previous) {
        previous = ajax.responseText;
        processData(previous);
      }
    }
  };
  ajax.open("POST", filename, true); //Use POST to avoid caching
  ajax.send();
}, 1000);


function processData(data) {
  var items = data.split('\n');
  var html = '<thead><tr><td>Name</td><td>Score</td><td>Kills</td><td>Deaths</td></tr></thead><tbody>';
  for(i = 0; i < items.length; i++) {
    var line = items[i].split(' ');
    html += '<tr>';
    for(j = 0; j < line.length; j++) {
      if(j != 1 && j != 2) {
        html += '<td>' + line[j] + '</td>';
      }
    }
    html += '</tr>';
  }
  html += '</tbody>';
  document.getElementById("data").innerHTML = html;
}