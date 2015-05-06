function csv2tabular(csv_file) {
    console.log(csv_file);
    $.get(csv_file, function (data) {

        // start the table
        var html = "<table class='table'>";

        // split into lines
        var rows = data.split("\n");
        var len = rows[0].split(",").length;

        console.log(len);
        // parse lines
        for (var i = 0; i < rows.length; i++) {
            html += "<tr>";

            var columns = rows[i].split(",");
            if (i==0){
                for (var j = 0; j < len; j++){
                    html += "<th>" + columns[j] + "</th>";
                }
                html += "</tr>";
            }
            else{
                html += "<th>" + columns[0] + "</th>";
                for (var j = 1; j < len; j++){
                    html += "<td>" + columns[j] + "</td>";
                }
                html += "</tr>";
            }
        }
        // close table
        html += "</table>";

        // insert into div
        $('#csv_data').append(html);

    });
}