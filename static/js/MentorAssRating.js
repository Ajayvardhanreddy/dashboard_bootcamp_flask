//Mentor Rating
let mentor = document.getElementById('myMentorAss').getContext('2d');

let MentorGraph = new Chart(mentor, {
    type: 'line',
    data: {
        labels:['Class 1', 'Class 2', 'Class 3', 'Class 4'],
        datasets:[{
            label: 'Rating',
            data:[7.5,8,9.2,8],
            backgroundColor: '#FD00FF',
            hoverBorderWidth: 2,
            hoverBorderColor: 'black'
        }],
    },
    options: {
        scales: {
            y: {
                min: 0,
                max: 10,
              }
        }
    }
});
