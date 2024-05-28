function generateRandomColor(alphat = 0.2) {
	let red = Math.floor(parseInt(Math.random() * 255));
	let green = Math.floor(parseInt(Math.random() * 255));
	let blue = Math.floor(parseInt(Math.random() * 255));

	return `rgb(${red},${green},${blue}, ${alphat})`;
}

function loadChart(
	newCtx,
	type,
	lables,
	title,
	label,
	data,
	backgroundColor,
	borderColor,
) {
	new Chart(newCtx, {
		type: type,
		data: {
			labels: lables,
			datasets: [
				{
					label: label,
					data: data,
					backgroundColor: backgroundColor,
					borderColor: borderColor,
					borderWidth: 1,
				},
			],
		},
		options: {
			scales: {
				y: {
					beginAtZero: true,
				},
			},
			plugins: {
				title: {
					display: true,
					text: title,
					padding: {
						top: 10,
					}
				},
			},
		},
	});
}
