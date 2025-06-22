window.onload = function () {

  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    theme: "light2",
    title: {
      text: "Semesterly Marking Expenditure"
    },
    axisY: {
      title: "Expenditure (USD)",
      includeZero: false
    },
    axisX: {
      title: "Semester"
    },
    data: [{
      type: "line",
      dataPoints: [
        { label: "2019-I", y: 12000 },
        { label: "2019-II", y: 12300 },
        { label: "2020-I", y: 12150 },
        { label: "2020-II", y: 12500 },
        { label: "2021-I", y: 12400 },
        { label: "2021-II", y: 12750 },
        { label: "2022-I", y: 12600 },
        { label: "2022-II", y: 12900 },
        { label: "2023-I", y: 12850 },
        { label: "2023-II", y: 13200 }
      ]
    }]
  });

  var chart2 = new CanvasJS.Chart("perfChart", {
    animationEnabled: true,
    theme: "light2",
    title: {
      text: "Yearly Average GPA vs Semester"
    },
    axisY: {
      title: "Average GPA",
      minimum: 2.0,
      maximum: 4.0,
      interval: 0.5
    },
    axisX: {
      title: "Semester"
    },
    data: [
      {
        type: "line",
        name: "Year 1",
        showInLegend: true,
        dataPoints: [
          { label: "2019-I", y: 3.1 },
          { label: "2019-II", y: 3.0 },
          { label: "2020-I", y: 3.2 },
          { label: "2020-II", y: 3.1 },
          { label: "2021-I", y: 3.0 },
          { label: "2021-II", y: 3.2 },
          { label: "2022-I", y: 3.3 },
          { label: "2022-II", y: 3.2 },
          { label: "2023-I", y: 3.3 },
          { label: "2023-II", y: 3.4 }
        ]
      },
      {
        type: "line",
        name: "Year 2",
        showInLegend: true,
        dataPoints: [
          { label: "2019-I", y: 3.0 },
          { label: "2019-II", y: 3.0 },
          { label: "2020-I", y: 3.0 },
          { label: "2020-II", y: 3.0 },
          { label: "2021-I", y: 3.0 },
          { label: "2021-II", y: 3.0 },
          { label: "2022-I", y: 3.0 },
          { label: "2022-II", y: 3.0 },
          { label: "2023-I", y: 3.0 },
          { label: "2023-II", y: 3.0 }
        ]
      },
      {
        type: "line",
        name: "Year 3",
        showInLegend: true,
        dataPoints: [
          { label: "2019-I", y: 2.9 },
          { label: "2019-II", y: 2.8 },
          { label: "2020-I", y: 2.7 },
          { label: "2020-II", y: 2.6 },
          { label: "2021-I", y: 2.5 },
          { label: "2021-II", y: 2.4 },
          { label: "2022-I", y: 2.3 },
          { label: "2022-II", y: 2.2 },
          { label: "2023-I", y: 2.1 },
          { label: "2023-II", y: 2.0 }
        ]
      }
    ]
  });


  setTimeout(() => {
    chart.render();
    chart2.render();
  }, 1000);


}