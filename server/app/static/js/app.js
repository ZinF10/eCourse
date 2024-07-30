function generateRandomColor(alphat = 0.2) {
	const red = Math.floor(parseInt(Math.random() * 255));
	const green = Math.floor(parseInt(Math.random() * 255));
	const blue = Math.floor(parseInt(Math.random() * 255));

	return `rgb(${red},${green},${blue}, ${alphat})`;
}

function loadChart(ctx, type, labels, title, yAxisLabel, data, backgroundColor, borderColor) {
	if (window.myChart) {
		window.myChart.destroy();
	}
	window.myChart = new Chart(ctx, {
		type: type,
		data: {
			labels: labels,
			datasets: [{
				label: yAxisLabel,
				data: data,
				backgroundColor: backgroundColor,
				borderColor: borderColor,
				borderWidth: 1
			}]
		},
		options: {
			responsive: true,
			scales: {
				y: {
					beginAtZero: true
				}
			},
			animations: {
				tension: {
					duration: 1000,
					easing: 'linear',
					from: 1,
					to: 0,
					loop: true
				},
			},
			plugins: {
				title: {
					display: true,
					text: title
				}
			},
			transitions: {
				show: {
					animations: {
						x: {
							from: 0
						},
						y: {
							from: 0
						}
					}
				},
				hide: {
					animations: {
						x: {
							to: 0
						},
						y: {
							to: 0
						}
					}
				}
			}
		}
	});
}