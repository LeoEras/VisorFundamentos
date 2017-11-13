$(function () {
    var group_id = parseInt($("#group_id").text());
    var term_id = parseInt($("#term_id").text());
	var student1 = ($("#student1").text());
	var student2 = ($("#student2").text());
	var student3 = ($("#student3").text());
	var student4 = ($("#student4").text());
    var names = [student1, student2, student3, student4];
    var values_1 = $(".ul1").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_1.length; i++) { 
        values_1[i] = parseFloat(values_1[i]);
    }
    var total_1 = values_1.reduce(function(a, b) { return a + b; }, 0);
    var values_2 = $(".ul2").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_2.length; i++) { 
        values_2[i] = parseFloat(values_2[i]);
    }
    var total_2 = values_2.reduce(function(a, b) { return a + b; }, 0);
    var values_3 = $(".ul3").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_3.length; i++) { 
        values_3[i] = parseFloat(values_3[i]);
    }
    var total_3 = values_3.reduce(function(a, b) { return a + b; }, 0);
    var values_4 = $(".ul4").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_4.length; i++) { 
        values_4[i] = parseFloat(values_4[i]);
    }
    var total_4 = values_4.reduce(function(a, b) { return a + b; }, 0);
    
    function toDate(value){
        var hour = Math.floor(value/3600);
        var minute = Math.floor((value - hour*3600)/60);
        var seconds = value - hour*3600 - minute*60;
        if (minute < 10) {
            minute = "0" + minute;
        } 
		if (seconds < 10) {
            seconds = "0" + seconds;
        }
        return hour + ':' + minute + ':' + seconds
    }
	
	function parseTerm(term_id){
		var str = "";
		if (term_id == 1){
			str = "2016-1T";
		} else if (term_id == 2){
			str = "2016-2T";
		} else if (term_id == 3){
			str = "2017-1T";
		}
		
		return str;
	}
	   
    if(student4 == "-" && student3 == "-" && student2 == "-"){
		$('#container').highcharts({
			chart: {
				zoomType: 'x'
			},
			title: {
				text: parseTerm(term_id),//$( "li" ).text(),
				x: -20
			},
			subtitle: {
				text: 'Grupo # ' + group_id + ': Análisis Comparativo',
				x: -20
			},
			xAxis: {
				categories: $(".alldates").map(function() {
					 return $(this).text();
				}).get()
			},
			yAxis: {
				min: 0,
				tickInterval: 3600,
				title: {
					text: 'Horas Trabajadas'
				},          
				labels: {
					formatter: function () {
						return toDate(this.value)
					}            
				},
				plotLines: [{
					value: 0,
					width: 1,
					color: '#808080'
				}]
			},
			tooltip: { formatter: function() {
					return '<b>'+ this.series.name[0] +':</b> ' + toDate(this.point.y)
				}
			},
			legend: {
				layout: 'vertical',
				align: 'right',
				verticalAlign: 'middle',
				borderWidth: 0
			},
			series: [{
				name: [names[0], ' ' + toDate(total_1)],
				data: values_1
			}]
		});		
	} else if (student4 == "-"){
		$('#container').highcharts({
			chart: {
				zoomType: 'x'
			},
			title: {
				text: parseTerm(term_id),//$( "li" ).text(),
				x: -20
			},
			subtitle: {
				text: 'Grupo # ' + group_id + ': Análisis Comparativo',
				x: -20
			},
			xAxis: {
				categories: $(".alldates").map(function() {
					 return $(this).text();
				}).get()
			},
			yAxis: {
				min: 0,
				tickInterval: 3600,
				title: {
					text: 'Horas Trabajadas'
				},          
				labels: {
					formatter: function () {
						return toDate(this.value)
					}            
				},
				plotLines: [{
					value: 0,
					width: 1,
					color: '#808080'
				}]
			},
			tooltip: { formatter: function() {
					return '<b>'+ this.series.name[0] +':</b> ' + toDate(this.point.y)
				}
			},
			legend: {
				layout: 'vertical',
				align: 'right',
				verticalAlign: 'middle',
				borderWidth: 0
			},
			series: [{
				name: [names[0], ' ' + toDate(total_1)],
				data: values_1
			}, {
				name: [names[1], ' ' + toDate(total_2)],
				data: values_2
			},  {
				name: [names[2], ' ' + toDate(total_3)],
				data: values_3
			}]
		});
	} else if (student3 == "-"){
		$('#container').highcharts({
			chart: {
				zoomType: 'x'
			},
			title: {
				text: parseTerm(term_id),//$( "li" ).text(),
				x: -20
			},
			subtitle: {
				text: 'Grupo # ' + group_id + ': Análisis Comparativo',
				x: -20
			},
			xAxis: {
				categories: $(".alldates").map(function() {
					 return $(this).text();
				}).get(),
				minRange: 3
			},
			yAxis: {
				min: 0,
				tickInterval: 3600,
				title: {
					text: 'Horas Trabajadas'
				},          
				labels: {
					formatter: function () {
						return toDate(this.value)
					}            
				},
				plotLines: [{
					value: 0,
					width: 1,
					color: '#808080'
				}]
			},
			tooltip: { formatter: function() {
					return '<b>'+ this.series.name[0] +':</b> ' + toDate(this.point.y)
				}
			},
			legend: {
				layout: 'vertical',
				align: 'right',
				verticalAlign: 'middle',
				borderWidth: 0
			},
			series: [{
				name: [names[0], ' ' + toDate(total_1)],
				data: values_1
			}, {
				name: [names[1], ' ' + toDate(total_2)],
				data: values_2
			}]
		});
	} else {
		$('#container').highcharts({
			chart: {
				zoomType: 'x'
			},
			title: {
				text: parseTerm(term_id),//$( "li" ).text(),
				x: -20
			},
			subtitle: {
				text: 'Grupo # ' + group_id + ': Análisis Comparativo',
				x: -20
			},
			xAxis: {
				categories: $(".alldates").map(function() {
					 return $(this).text();
				}).get()
			},
			yAxis: {
				min: 0,
				tickInterval: 3600,
				title: {
					text: 'Horas Trabajadas'
				},          
				labels: {
					formatter: function () {
						return toDate(this.value)
					}            
				},
				plotLines: [{
					value: 0,
					width: 1,
					color: '#808080'
				}]
			},
			tooltip: { formatter: function() {
					return '<b>'+ this.series.name[0] +':</b> ' + toDate(this.point.y)
				}
			},
			legend: {
				layout: 'vertical',
				align: 'right',
				verticalAlign: 'middle',
				borderWidth: 0
			},
			series: [{
				name: [names[0], ' ' + toDate(total_1)],
				data: values_1
			}, {
				name: [names[1], ' ' + toDate(total_2)],
				data: values_2
			}, {
				name: [names[2], ' ' + toDate(total_3)],
				data: values_3
			}, {
				name: [names[3], ' ' + toDate(total_4)],
				data: values_4
			}]
		});
	}
});