var xmlHttp = new XMLHttpRequest();
xmlHttp.open("GET", "http://localhost:8081/results", false); // false for synchronous request
xmlHttp.send(null);
var response = xmlHttp.responseText;
console.log(response); //testing
var response = JSON.parse(response);

var Labels = []
var Data = []

response.results.forEach(function (datapoint) {
  Labels.push(datapoint.label); Data.push(datapoint.score[0]);
});

var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: Labels,
    datasets: [{
      label: 'Label',
      data: Data,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 205, 86, 0.2)'
      ],
      borderColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(255, 205, 86)'
      ],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        } 
      }]
    }
  }
});