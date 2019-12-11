function map(Data, Map) {
  console.log(Object.keys(Data));
  // Mike Bostock's bl.ock updated for D3 v4 https://bl.ocks.org/mbostock/1073373
  var width = 960,
      height = 700;

  var div = d3.select("body").append("div")
     .attr("class", "tooltip-donut")
     .style("opacity", 0);

  var path = d3.geoPath();
  var simulation = d3.forceSimulation();

  // Define linear scale for output
  var color = d3.scaleLinear().domain([15,28])
      .range(["#fcfafc", "#720787"]);

  var svg = d3.select("#svg_map")
      .attr("width", width)
      .attr("height", height);

  d3.json("https://d3js.org/us-10m.v1.json", function (error, us) {
    if (error) throw error;

    var states = topojson.feature(us, us.objects.states),
        nodes = [],
        links = [];

    states.features.forEach(function (d, i) {
      if (d.id === "02" || d.id === "15" || d.id === "72") return; // lower 48
      var centroid = path.centroid(d);
      if (centroid.some(isNaN)) return;
      centroid.x = centroid[0];
      centroid.y = centroid[1];
      centroid.feature = d;
      nodes.push(centroid);
    });

    d3.voronoi().links(nodes).forEach(function (link) {
      var dx = link.source.x - link.target.x,
          dy = link.source.y - link.target.y;
      link.distance = Math.sqrt(dx * dx + dy * dy);
      links.push(link);
    });

    var link = svg.selectAll("line")
        .data(links)
        .enter().append("line")
        .attr("x1", function (d) {
          return d.source.x;
        })
        .attr("y1", function (d) {
          return d.source.y;
        })
        .attr("x2", function (d) {
          return d.target.x;
        })
        .attr("y2", function (d) {
          return d.target.y;
        });

    var node = svg.selectAll("g")
        .data(nodes)
        .enter().append("g")
        .attr("transform", function (d) {
          return "translate(" + -d.x + "," + -d.y + ")";
        })
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended))
        .append("path")
        .attr("transform", function (d) {
          return "translate(" + d.x + "," + d.y + ")";
        })
        .attr("d", function (d) {
          return path(d.feature);
        })
        .attr("fill", function (d, i) {
          if (!Data[d.feature.id] || Math.round(Data[d.feature.id]) == 0)
            return "#ddd";
          else
            return color(Math.round(Data[d.feature.id]));
        })
        .on("mouseover", function (d, i) {
          d3.select(this).transition()
               .duration('50')
               .attr('opacity', '.5');
          div.transition()
               .duration(50)
               .style("opacity", 1);})
        .on('mouseout', function (d, i) {
          d3.select(this).transition()
              .duration('50')
              .attr('opacity', '0.9');
          div.transition()
              .duration('50')
              .style("opacity", 0);
     });
    //.attr("fill", "rgb(217,91,67)");


    usCentroid = [d3.mean(nodes, function (d) {
      return d.x;
    }),
      d3.mean(nodes, function (d) {
        return d.y;
      })];

    simulation.nodes(nodes)
        .force("charge", d3.forceManyBody().strength(-5))
        .force("link", d3.forceLink(links).distance(function (d) {
          return d.distance;
        }))
        .force("center", d3.forceCenter(usCentroid[0], usCentroid[1]))
        .on("tick", ticked);

    function ticked() {
      link.attr("x1", function (d) {
        return d.source.x;
      })
          .attr("y1", function (d) {
            return d.source.y;
          })
          .attr("x2", function (d) {
            return d.target.x;
          })
          .attr("y2", function (d) {
            return d.target.y;
          });
      node.attr("transform", function (d) {
        return "translate(" + d.x + "," + d.y + ")";
      });
    }
  });

  function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
  }

  function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
}