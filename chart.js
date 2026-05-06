function loadChart(score, total) {
    const wrong = total - score;

    new Chart(document.getElementById("chart"), {
        type: "doughnut",
        data: {
            labels: ["Correct", "Wrong"],
            datasets: [{
                data: [score, wrong],
                backgroundColor: ["#66bb6a", "#ef5350"], // soft colors
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: "bottom",
                    labels: {
                        font: { size: 11 }
                    }
                }
            }
        }
    });
}




