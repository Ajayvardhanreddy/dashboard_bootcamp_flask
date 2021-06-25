//Mentor CC Score
let mccscore = document.getElementById('myCCmentor').getContext('2d');

let MentorCodingChallenge = new Chart(mccscore, {
    type: 'line',
    data: {
        labels:['Class 1', 'Class 2', 'Class 3', 'Class 4'],
        datasets:[{
            label: 'Rating',
            data:[10,20,30,77],
            backgroundColor: 'red',
            hoverBorderWidth: 2,
            hoverBorderColor: 'red'
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