// ChartJs 


const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: lista_datas,
        datasets: [{
            label: 'Lista Cotacoes',
            data: lista_cotacoes,
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
            ],
            pointStyle: 'circle',
            borderWidth: 2,
            pointRadius: 1,
            pointHoverRadius: 15
        }, ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});


// Apex Chart
var options = {
    chart: {
        type: 'line'
    },
    stroke: {
        width: 2
    },
    series: [{
        name: 'Cotações',
        data: lista_cotacoes
    }],
    xaxis: {
        categories: lista_datas
    },

    grid: {
        row: {
            colors: ['#e5e5e5', 'transparent'],
            opacity: 0.5
        },
        column: {
            colors: ['#f8f8f8', 'transparent'],
        },
        xaxis: {
            lines: {
                show: true
            }
        },
        yaxis: {
            lines: {
                show: true
            }
        },
        padding: {
            top: 0,
            right: 0,
            bottom: -30,
            left: 0
        },
    },
}
var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();