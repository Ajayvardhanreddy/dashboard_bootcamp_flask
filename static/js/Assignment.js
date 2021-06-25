//Assignment Score
let score = document.getElementById('myAss').getContext('2d');

let asscore = new Chart(score, {
    type: 'bar',
    data: {
//        labels:['Class 1', 'Class 2', 'Class 3', 'Class 4'],
        labels:[
          {% for item in labels %}
           "{{ item }}",
          {% endfor %}
	],
        datasets:[{
            label: 'Percentage',
            data:[{% for item in values %}
               "{{ item }}",
              {% endfor %}
	       ],
            backgroundColor: '#FF1300',
            hoverBorderWidth: 2,
            hoverBorderColor: 'black'
        }],
    },
    options: {
        scales: {
            y: {
                min: 0,
                max: 100,
              }
        }
    }
});