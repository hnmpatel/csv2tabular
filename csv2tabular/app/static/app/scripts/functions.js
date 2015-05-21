function csv2tabular(csv_file, option1, option2, target) {
    $.get(csv_file, function (data) {

        // start the table
        var html = "<table class='table'>";

        // split into lines
        var rows = data.split("\n");
        var len = rows[0].split(",").length;
        var options = ""

        // parse lines
        for (var i = 0; i < rows.length - 1 ; i++) {
            html += "<tr>";

            var columns = rows[i].split(",");
            if (i==0){
                for (var j = 0; j < len; j++){
                    html += "<th>" + columns[j] + "</th>";
                    options += "<option value='" + j + "'>" + columns[j] + "</option>"
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
        target.append(html);
        option1.append(options);
        option2.append(options);

    });
}

function crossTabular(csv_file, c1, c2, target) {
    $.get(csv_file, function (data) {

        // start the table
        var html = "<table class='table'>";

        // split into lines
        var rows = data.split("\n");
        var len = rows[0].split(",").length;
        var c_list = [];
        var r_list = [];
        var result = {};
        var temp = {}

        // parse lines
        for (var i = 1; i < rows.length - 1; i++) {
            
            var columns = rows[i].split(",");
            
            if (!temp.hasOwnProperty(columns[c2])) {
                c_list.push(columns[c2]);
                temp[columns[c2]] = [];
            }
            
            if (result.hasOwnProperty(columns[c1])) {
                result[columns[c1]].push(columns[c2]);
            }
            else {
                r_list.push(columns[c1]);
                result[columns[c1]] = [];
                result[columns[c1]].push(columns[c2]);
            }
        }       
        
        html = "<table class='table'><thead><tr><th></th>";
        for (var c in c_list) {
            html += "<th>"+ c_list[c] +"</th>";
        }
        var count = 0;
        for (var key in result) {
            html += "</thead><tbody></tr><tr><th scope='row'>"+ key +"</th>";
            for (var c in c_list) {
                count = 0;
                for (var ele in result[key]) {
                    if (result[key][ele] == c_list[c]) {
                        count += 1;
                    }
                }
                html += "<td>" + count + "</td>";
            }
        }
        html += "</tr></tbody></table>";

        target.html(html);
    });
}