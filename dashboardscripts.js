

Apex.grid = {
  padding: {
    right: 0,
    left: 0
  }
}
var colorPalette = ['#A04740', '#8886CF', '#77BA99',"#1C9AAE" ,'#004A99']
// var colorPalette = ['#ea9999', '#f6b26b', '#39cccc',"#38761d" ,'#0b5394']
// var colorPalette3 = ['#9e8aa9', '#dfc0a1', '#c0d2a0',"#8aa2a5" ,'#c79c9c']
var colorPalette3 = ['#A04740', '#004A99', '#77BA99',"#1C9AAE" ,'#8886CF']

// var colorPalette3 = ['#004A99', '#A45F6E', '#EF9738', '#77BA99', '#D14F57']

// var colorPalette = ['#ffa600', '#89b326', '#00a973', '#0093a4', '#0075a4']
// var colorPalette = ['#b78adf', '#6F42C1', '#00CCCC', '#007BFF', '#004A99']
// var colorPalette3 = ['#004A99', '#6F42C1', '#00CCCC', '#007BFF', '#b78adf']

// var colorPalette = ['#ffa600', '#ff6b42', '#ff3274', '#cf26a3', '#6f42c1']
// var colorPalette3 = ['#6F42C1', '#0DCAF0', '#17A2B8', '#007BFF', '#808080']



var colorPalette2 = ['#0766AD', '#DF826C', '#EE9322', '#E9B824', '#C5E898']



$(document).ready(function () {
  $("#myInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".dropdown-menu li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});




fetch('/lnt/chart')
  .then(response => response.json())
  .then(data => {
    const {
      not_yet_started_process,
      not_yet_started_mech,
      not_yet_started_electrical,
      not_yet_started_instru,
      not_yet_started_other,
      pre_order_stage_process,
      pre_order_stage_mech,
      pre_order_stage_electrical,
      pre_order_stage_instru,
      pre_order_stage_other,
      preorder_completed_process,
      preorder_completed_mech,
      preorder_completed_electrical,
      preorder_completed_instru,
      preorder_completed_other,
      post_order_stage_process,
      post_order_stage_mech,
      post_order_stage_electrical,
      post_order_stage_instru,
      post_order_stage_other,
      completed_process,
      completed_mech,
      completed_electrical,
      completed_instru,
      completed_other,
      mech, process, electrical, instru, other,
      not_yet_started,
      pre_order_stage,
      preorder_completed,
      post_order_stage,
      completed,
      with_edrc_pre,
      with_edrc_post,
      with_vendor_pre,
      with_vendor_post
    } = data;
    const allpr=process+ mech+ electrical+instru+other



    const optionsBar = {
      colors: colorPalette,
      series: [{
        name: 'Not Yet Started',
        data: [not_yet_started_process, not_yet_started_mech, not_yet_started_electrical, not_yet_started_instru, not_yet_started_other,]
      }, {
        name: 'Pre Order Stage',
        data: [pre_order_stage_process, pre_order_stage_mech, pre_order_stage_electrical, pre_order_stage_instru, pre_order_stage_other,]
      }, {
        name: 'Pre Order Completed',
        data: [preorder_completed_process, preorder_completed_mech, preorder_completed_electrical, preorder_completed_instru, preorder_completed_other,]
      }, {
        name: 'Post Order stage',
        data: [post_order_stage_process, post_order_stage_mech, post_order_stage_electrical, post_order_stage_instru, post_order_stage_other,]
      }, {
        name: 'Completed',
        data: [completed_process, completed_mech, completed_electrical, completed_instru, completed_other,]
      }],
      chart: {
        fontFamily: 'Source Sans 3',
        type: 'bar',
        height: 340,
        width: '100%',
        stacked: true,
        stackType: '100%',
        events: {
          dataPointSelection: (event, chartContext, config) => {
             console.log(config.dataPointIndex)
             console.log(config.seriesIndex)
             console.log(config.labels)


              openPopup(config.dataPointIndex,config.seriesIndex)
             
            }
        },

    },
      fill: {
        type: 'gradient',
        gradient: {
          shade: 'dark',
          type: 'horizontal',
          shadeIntensity: 1,
          opacityFrom: 1,
          opacityTo: 1,
          stops: [0, 50, 100],
          colorStops: [],
        },
      },
      plotOptions: {
        bar: {
          horizontal: true,
        },
      },
      dataLabels: {
        enabled: true,
        style: {
          fontSize: '13px',
          fontWeight: 500,
          fontFamily: 'Source Sans 3',
          color: '#000000',
        },
        dropShadow: {
          enabled: false
        }
      },
      stroke: {
        width: 0,
        colors: ['#ffffff'],
      },
      title: {
        text: 'Progress (Discipline wise)',
        align: 'center',
        margin: 5,
        offsetX: 0,
        offsetY: 0,
        floating: false,
        style: {
          fontSize: '20px',
          fontWeight: 'bold',
          fontFamily: 'Source Sans 3',
          color: '#263238',
        },
      },
      subtitle:{
        text: 'Click on the bars to view more information',
        align: 'center',
        offsetY: 60,
      },
      xaxis: {
        categories: [' Process', 'Mechanical', 'Electrical', 'Instrumentation', 'others'],
      },
      fill: {
        opacity: 1,
      },
      legend: {
        position: 'bottom',
        horizontalAlign: 'center',
        fontWeight: 600,
        dropShadow:false,
        markers: {
          width: 25,
        }
      },
    };


    const optionsDonut = {
      colors: colorPalette,
      series: [not_yet_started, pre_order_stage, preorder_completed, post_order_stage, completed],
      legend: {
        position: 'bottom',
        offsetY: 8,
        dropShadow:false,
      },

      chart: {
      
        toolbar: {
          show: true,
          offsetX: 0,
          offsetY: 0,
          tools: {
            download: true,
            selection: true,
            zoom: true,
            zoomin: true,
            zoomout: true,
            pan: true,
            reset: true | '<img src="/static/icons/reset.png" width="20">',
            customIcons: []
          },
          export: {
            csv: {
              filename: undefined,
              columnDelimiter: ',',
              headerCategory: 'category',
              headerValue: 'value',
              dateFormatter(timestamp) {
                return new Date(timestamp).toDateString()
              }
            },
            svg: {
              filename: undefined,
            },
            png: {
              filename: undefined,
            }
          },
          autoSelected: 'zoom' 
        },
        width: 280,
        height:370,
        type: 'pie',
        fontFamily: "Source Sans 3",
        animations: {
          enabled: true,
          easing: 'easeinout',
          speed: 900,
          animateGradually: {
              enabled: true,
              delay: 150
          },
          dynamicAnimation: {
              enabled: true,
              speed: 950
          }
      }
      },  
      dataLabels: {
        enabled: true,
        dropShadow:false,
        textAnchor: 'start',
        distributed: true,
        style: {
          fontSize: '13px',
          fontWeight: 500,}
      },
     
      title: {
        text: "Status (By Stages)",
        align: 'center',
        margin: 20,
        offsetX: 0,
        offsetY: -13,
        floating: false,
        style: {
          fontSize: '20px',
          fontWeight: 'bold',
          fontFamily: "Source Sans 3",
        }
      },
      stroke: {
        width: .5,
        colors: ['#ffffff'],
      },
      labels: ['Not Yet Started', 'Pre Order Stage', 'Pre Order Completed', 'Post Order Stage', 'Completed'],
      legend:{
        position: 'bottom',
        horizontalAlign: 'center',
        fontWeight: 600,
        markers: {
          width: 25,
        }
      },
      responsive: [{
        breakpoint: 100,
        options: {
          chart: {
            width: "100%"
          },

        }
      }]
    }
    
    const optionsDonut2 = {
      series: [{
        name:"Total PR",
        data: [process, mech, electrical, instru, other]
      }],
      chart: {
        width: 445,
        height: 330,
        type: 'bar',
        fontFamily: "Source Sans 3",
      },
      colors: colorPalette3,
      subtitle: {
        text: "Total PRs: "+allpr,
        align: 'center',
        margin: 0,
      offsetX: 0,
      offsetY: 55,
      floating: false,
      style: {
        fontSize:  '20px',
        fontWeight:  'bold',
        fontFamily:  "Source Sans 3",
        color:  '#000'
      },
      },
      title: {
        text: "PR (By Discipline)",
        align: 'center',
        margin: 0,
        offsetX: 0,
        offsetY: 0,
        floating: false,
        style: {
          fontSize: '20px',
          fontWeight: 'bold',
          fontFamily: "Source Sans 3",
          color: '#263238'
        }
      },
      xaxis: {
        categories: ["Process", "Mechanical", "Electrical", "Instrumentation", "Others"],
      },
      plotOptions: {
        bar: {
          columnWidth: '45%',
          barHeight: '900px',

          distributed: true,
        }
      },
      dataLabels: {
        enabled: true,
        dropShadow:false,
        style: {
          fontSize: '13px',
          fontWeight: 500,}
      },
      legend:{
        position: 'bottom',
        horizontalAlign: 'center',
        fontWeight: 600,
        dropShadow:false,
        markers: {
          width: 15,
        }
      },
      responsive: [
        {
          options: {
            chart: {
              width: 400
            },
            legend: {
              position: 'bottom'
            }
          }
        }
      ]
    };

    var bar2options = {
      series: [{
      name:"With EDRC",
      data: [with_edrc_pre,with_edrc_post]
    }, {name:"With Vendor",
      data: [with_vendor_pre, with_vendor_post]
    }],
    legend: {
      show: true,
      dropShadow:false,
      style: {
        fontSize: '20px',
        fontWeight: 'bold',
        fontFamily: "Source Sans 3",
        color: '#000'
      }},
      chart: {
      type: 'bar',
      width: "100%",
      height: 330,
      fontFamily: "Source Sans 3",
    },
    plotOptions: {
      bar: {
        horizontal: false,
        dataLabels: {
          position: 'center',
        },
      }
    },
    dataLabels: {
      enabled: true,
      offsetX: 0,
      style: {
        fontSize: '13px',
          fontWeight: 500,
      }
    },
    stroke: {
      show: true,
      width: 1,
      colors: ['#fff']
    },
    tooltip: {
      shared: true,
      intersect: false
    },
    title: {
      text: "Average Time Consumed (In Days)",
      align: 'center',
      margin: 0,
      offsetX: 0,
      offsetY: 0,
      floating: false,
      style: {
        fontSize: '20px',
        fontWeight: 'bold',
        fontFamily: "Source Sans 3",
        color: '#263238'
      }},
      legend:{
        position: 'bottom',
        horizontalAlign: 'center',
        fontWeight: 600,
        markers: {
          width: 25,
        }
      },
     
    colors: colorPalette3,
    xaxis: {
      categories: ["Pre Order Stage", "Post Order STage"],
    },
    };

    
  
    

    // Create charts using ApexCharts
    var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
    var chartDonut = new ApexCharts(document.querySelector('#donut'), optionsDonut);
    var chartDonut2 = new ApexCharts(document.querySelector('#donut2'), optionsDonut2);
    var chartbar2 = new ApexCharts(document.querySelector("#bar2"), bar2options);
    

    chartBar.render();
    chartDonut.render();
    chartDonut2.render();
    chartbar2.render();
  })
  .catch(error => console.error('Error fetching data:', error));
