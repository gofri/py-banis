$(function() {

    window.setInterval(function(){
        $.ajax({
            url: '/api/getJsonData',
            success: function(data) {
                tb = $("#devices_tb");
                tb.html('');
                for (index = 0; index < data.length; index++)
                {
                    obj = data[index];
                    new_row = $("<tr>");
                    new_row.append($("<td>" + (index + 1).toString() +  "</td>"));
                    for (valIndex = 0; valIndex < obj.length; valIndex++) {
                        new_row.append('<td class="' + obj[valIndex].toLowerCase() + '">' + obj[valIndex].toString()  + '</td>')
                    }
                    tb.append(new_row);
                }

            }
        });
    }, 2000);
})
