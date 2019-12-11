function revenue(Data) {
    var n = 3, // The number of series.
        m = Object.keys(Data).length; // The number of values per series.
    // The xz array has m elements, representing the x-values shared by all series.
    // The yz array has n elements, representing the y-values of each of the n series.
    // Each yz[i] is an array of m non-negative numbers representing a y-value for xz[i].
    // The y01z array has the same structure as yz, but with stacked [y₀, y₁] instead of y.
    var xz = d3.range(m),
        yz = d3.range(n).map(function (d) {
            return deal(Data, d);
        }),
        y01z = d3.stack().keys(d3.range(n))(d3.transpose(yz)),
        yMax = d3.max(yz, function (y) {
            return d3.max(y);
        }),
        y1Max = d3.max(y01z, function (y) {
            return d3.max(y, function (d) {
                return d[1];
            });
        });
    var svg = d3.select("#svg_revenue"),
        margin = {top: 40, right: 0, bottom: 50, left: 10},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    var x = d3.scaleBand()
        .domain(xz)
        .rangeRound([0, width])
        .padding(0.08);
    var y = d3.scaleLinear()
        .domain([0, y1Max])
        .range([height, 0]);
    var color = d3.scaleOrdinal()
        .domain(d3.range(n))
        .range(d3.schemeCategory20c);
    var series = g.selectAll(".series")
        .data(y01z)
        .enter().append("g")
        .attr("fill", function (d, i) {
            return color(i);
        });
    var rect = series.selectAll("rect")
        .data(function (d) {
            return d;
        })
        .enter().append("rect")
        .attr("x", function (d, i) {
            return x(i);
        })
        .attr("y", height)
        .attr("width", x.bandwidth())
        .attr("height", 0);
    rect.transition()
        .delay(function (d, i) {
            return i * 10;
        })
        .attr("y", function (d) {
            return y(d[1]);
        })
        .attr("height", function (d) {
            return y(d[0]) - y(d[1]);
        });
    g.append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x)
            .tickSize(0)
            .tickPadding(6));
    d3.selectAll("input")
        .on("change", changed);
    var timeout = d3.timeout(function () {
        d3.select("input[value=\"grouped\"]")
            .property("checked", true)
            .dispatch("change");
    }, 2000);

    // text label for the x axis
    svg.append("text")
      .attr("transform",
            "translate(" + (width/2) + " ," +
                           (height + margin.top + 30) + ")")
      .style("text-anchor", "middle")
      .text("Region");

    // text label for the y axis
    svg.append("text")
      .attr("transform", "rotate(90)")
      .attr("y", - width + 30)
      .attr("x", 250)
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text("Total Revenue (log)");

    function changed() {
        timeout.stop();
        if (this.value === "grouped") transitionGrouped();
        else transitionStacked();
    }

    function transitionGrouped() {
        y.domain([0, yMax]);
        rect.transition()
            .duration(500)
            .delay(function (d, i) {
                return i * 10;
            })
            .attr("x", function (d, i) {
                return x(i) + x.bandwidth() / n * this.parentNode.__data__.key;
            })
            .attr("width", x.bandwidth() / n)
            .transition()
            .attr("y", function (d) {
                return y(d[1] - d[0]);
            })
            .attr("height", function (d) {
                return y(0) - y(d[1] - d[0]);
            });
    }

    function transitionStacked() {
        y.domain([0, y1Max]);
        rect.transition()
            .duration(500)
            .delay(function (d, i) {
                return i * 10;
            })
            .attr("y", function (d) {
                return y(d[1]);
            })
            .attr("height", function (d) {
                return y(d[0]) - y(d[1]);
            })
            .transition()
            .attr("x", function (d, i) {
                return x(i);
            })
            .attr("width", x.bandwidth());
    }

    function deal(Data, n) {
        var value = [], i, j;
        j = -1;
        for (var prop in Data){
            i = 0;
            j += 1;
            for (var propin in Data[prop]) {
                if (i == n)
                    if (Data[prop][propin] > 0)
                        value[j] = Math.log(Data[prop][propin]);
                    else
                        value[j] = 0;
                i += 1;
            }
        }
        return value;
    }


}