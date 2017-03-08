// http://stackoverflow.com/questions/38453792/d3-passing-object-in-style-method-is-not-working

function start() 
{
  var height = 400,
      width = 600;
  
  var num_cols = 8;
  var num_rows = 8;
  
  
      
  var heat_data = [[10, 9, 8, 0, 0, 0, 0, 0],
                   [9, 10, 9, 8, 0, 0, 0, 0],
                   [8, 9, 10, 9, 8, 0, 0, 0],
                   [0, 8, 9, 10, 9, 8, 0, 0],
                   [0, 0, 8, 9, 10, 9, 8, 0],
                   [0, 0, 0, 8, 9, 10, 9, 8],
                   [0, 0, 0, 0, 8, 9, 10, 9],
                   [0, 0, 0, 0, 0, 8, 9, 10]];
                  
      
  var heat_data_1 = [[10], [9], [8], [0], [0], [0], [0], [0],
                   [9], [10], [9], [8], [0], [0], [0], [0],
                   [8], [9], [10], [9], [8], [0], [0], [0],
                   [0], [8], [9], [10], [9], [8], [0], [0],
                   [0], [0], [8], [9], [10], [9], [8], [0],
                   [0], [0], [0], [8], [9], [10], [9], [8],
                   [0], [0], [0], [0], [8], [9], [10], [9],
                   [0], [0], [0], [0], [0], [8], [9], [10]];
  
  
  
  var pixel_height = 200 / num_rows;
  var pixel_width = pixel_height;

  var yy = 100;
  var SVGContainer = d3.select("#chart")
                    .append("svg")
                    .style("background", "#C9D7D6")
                    .attr("width", width)
                    .attr("height", height);
  
  var xScale = d3.scale.ordinal()
                .domain(d3.range(0, num_cols))
                .rangeBands([0, 200]);
  
  var yScale = d3.scale.ordinal()
                .domain(d3.range(0, num_rows))
                .rangeBands([0, 200]);
  
  var colors = d3.scale.linear()
                .domain([0, 10])
                .range(["#000", "#FFB832"]);
  
  SVGContainer.selectAll("g")
                .data(heat_data)
                .enter()
                .append("g")
        
          .selectAll("rect")
            .data( function(d, row) { 
                console.log("row: " + row + " -- data: " + d);
                return d; 
            })
            .enter()
          .append("rect")
            .attr("id", function(d, i) { return "col_" + i; } )
            .style("fill", function(d, i) {
              return colors(d);
            })
            .attr("width", pixel_width)
            .attr("height", pixel_height)
            .attr("x", function(d, row)
            {
              var new_x = xScale(row%num_cols);
              return 200 - new_x;
            })
            .attr("y", function(d, i)
            {
              var j = Math.floor(i / num_cols);
              var new_y = yScale(j);

              return 200 - new_y;
            })

        .attr("width", pixel_width*num_cols)
        .attr("height", pixel_height)
        .attr("x", function() { return (width - (num_cols*pixel_width)) / 2;})
        .attr("y", function(d, i) { 
              var starting_point = (height - (num_rows*pixel_height)) / 2;
              var row_y = starting_point + pixel_height*i;
              return row_y;
        });
      
}