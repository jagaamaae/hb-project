
    const options = {
        responsive: true
      };
  
      
      let ctx_line = $("#lineChart").get(0).getContext("2d");
  
      $.get("/countries/{{country}}.json", function (data) {
      console.log(data)
      
      let myLineChart = Chart.Line(ctx_line, {
                                  data: data,
                                  type: "line",
                                  options: options
                              });
      $("#lineLegend").html(myLineChart.generateLegend());
      });
  