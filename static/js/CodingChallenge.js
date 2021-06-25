//Coding Challenge Score
let ccscore = document.getElementById('myCCscore').getContext('2d');

let CodingChallenge = new Chart(ccscore, {
    type: 'bar',
    data: {
        labels:['Class 1', 'Class 2', 'Class 3', 'Class 4'],
        datasets:[{
            label: 'Percentage',
            data:[10,20,30,77],
            backgroundColor: '#FD00FF',
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