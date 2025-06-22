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
      text: "Aggregate Average Grade vs Semester"
    },
    axisY: {
      title: "Aggregate Average Grade",
      minimum: 0,
      maximum: 100,
      interval: 10
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
          { label: "2019-I", y: 78 },
          { label: "2019-II", y: 75 },
          { label: "2020-I", y: 80 },
          { label: "2020-II", y: 77 },
          { label: "2021-I", y: 76 },
          { label: "2021-II", y: 79 },
          { label: "2022-I", y: 82 },
          { label: "2022-II", y: 80 },
          { label: "2023-I", y: 81 },
          { label: "2023-II", y: 84 }
        ]
      },
      {
        type: "line",
        name: "Year 2",
        showInLegend: true,
        dataPoints: [
          { label: "2019-I", y: 74 },
          { label: "2019-II", y: 74 },
          { label: "2020-I", y: 74 },
          { label: "2020-II", y: 74 },
          { label: "2021-I", y: 74 },
          { label: "2021-II", y: 74 },
          { label: "2022-I", y: 74 },
          { label: "2022-II", y: 74 },
          { label: "2023-I", y: 74 },
          { label: "2023-II", y: 74 }
        ]
      },
      {
        type: "line",
        name: "Year 3",
        showInLegend: true,
        dataPoints: [
          { label: "2019-I", y: 70 },
          { label: "2019-II", y: 68 },
          { label: "2020-I", y: 66 },
          { label: "2020-II", y: 64 },
          { label: "2021-I", y: 62 },
          { label: "2021-II", y: 60 },
          { label: "2022-I", y: 58 },
          { label: "2022-II", y: 56 },
          { label: "2023-I", y: 54 },
          { label: "2023-II", y: 52 }
        ]
      }
    ]
  });


  setTimeout(() => {
    chart.render();
    chart2.render();
  }, 1000);


}