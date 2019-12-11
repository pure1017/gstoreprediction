function wordcloud(Data) {
    // List of words
    var myWords = Object.keys(Data);
    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 10, bottom: 10, left: 10},
        width = 1000 - margin.left - margin.right,
        height = 1000 - margin.top - margin.bottom;

    var color = d3.scaleOrdinal(d3.schemeCategory20);
    // append the svg object to the body of the page
    var svg = d3.select("#svg_word")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
    // Wordcloud features that are different from one word to the other must be here
    var layout = d3.layout.cloud()
        .size([width, height])
        .words(myWords.map(function (d) {
            return {text: d};
        }))
        .padding(20)        //space between words
        .rotate(-45)       // rotation angle in degrees
        .fontSize(20)      // font size of words
        .on("end", draw);
    layout.start();

    // This function takes the output of 'layout' above and draw the words
    // Wordcloud features that are THE SAME from one word to the other can be here
    function draw(words) {
        svg
            .append("g")
            .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
            .selectAll("text")
            .data(words)
            .enter().append("text")
            .style("font-size", function(d){
                if (Math.log(Data[d.text]) == 0)
                    return 8;
                else
                    return (85.38-2.69*Math.log(Data[d.text]));
                })
            .style("fill", function (d) {
                return color(Math.round(Math.log(Data[d.text])));
            })
            .style("opacity", function(d){
                if (Math.log(Data[d.text]) == 0)
                    return .3;
                else
                    return 0.03*Math.log(Data[d.text])+0.2;
            })
            .attr("text-anchor", "middle")
            .style("font-family", "Impact")
            .attr("transform", function (d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            })
            .text(function (d) {
                return d.text;
            });
    }
}