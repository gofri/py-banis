
    function Get(yourUrl){

            
        var Httpreq = new XMLHttpRequest(); // a new request
        Httpreq.open("GET", yourUrl, false);
        Httpreq.send(null);
        return Httpreq.responseText;          
}

function CreateTableFromJSON() {
    
    var url = 'http://127.0.0.1:5000/api/getJsonData'
    var json_data = JSON.parse(Get(url))
    console.log(json_data)

    // $(document).ready(function(){

    //     var url = 'http://localhost:5000/api/getJsonData'
    //     $.getJSON(url, function(data){
    //     console.log(data);
    //     })

    // })

    var myBooks = json_data



    // var myBooks = [
    //     {
    //         "Book ID": "1",
    //         "Book Name": "Computer Architecture",
    //         "Category": "Computers",
    //         "Price": "125.60"
    //     },
    //     {
    //         "Book ID": "2",
    //         "Book Name": "Asp.Net 4 Blue Book",
    //         "Category": "Programming",
    //         "Price": "56.00"
    //     },
    //     {
    //         "Book ID": "3",
    //         "Book Name": "Popular Science",
    //         "Category": "Science",
    //         "Price": "210.40"
    //     }
    // ]

    // EXTRACT VALUE FOR HTML HEADER. 
    // ('Book ID', 'Book Name', 'Category' and 'Price')
    var col = [];
    for (var i = 0; i < myBooks.length; i++) {
        for (var key in myBooks[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key);
            }
        }
    }

    // var device_keys = [];
    // for (var i=0; i<myBooks.length)

    // Create dynamic table
    var table = document.createElement("table");

    // Create and populate table header

    var header = table.createTHead();
    var th = header.insertRow(0);                   

    var deviceID = th.insertCell(-1); deviceID.innerHTML = "Device ID";
    var connected = th.insertCell(-1); connected.innerHTML = "Connected";
    var good = th.insertCell(-1); good.innerHTML = "Good";
    var threshold = th.insertCell(-1); threshold.innerHTML = "Threshold";



    // for (var i = 0; i < col.length; i++) {
    //     var th = document.createElement("th");      // TABLE HEADER.
    //     th.innerHTML = col[i];
    //     tr.appendChild(th);
    // }

  


        // jsonString = JSON.stringify(myBooks);
        // console.log(jsonString);


    // Get JSON keys to iterate through devices
    var devicesKeys = Object.keys(myBooks['0']);

    console.log("devices: " + devicesKeys.length)
    console.log("second: " + devicesKeys['1'])

    // ADD JSON DATA TO THE TABLE AS ROWS.
    for (var i = 0; i < devicesKeys.length; i++) {

        tr = table.insertRow(-1);

        for (var j = 0; j < devicesKeys.length -1 ; j++) {
            var deviceCell = tr.insertCell(-1);
            deviceCell.innerHTML = devicesKeys[i];

            var connectedCell = tr.insertCell(-1);   
            connectedCell.innerHTML = myBooks[0][devicesKeys[i]]['is_connected'];

            var goodCell = tr.insertCell(-1);
            goodCell.innerHTML = myBooks[0][devicesKeys[i]]['is_good'];

            var thresholdCell = tr.insertCell(-1);
            thresholdCell.innerHTML = myBooks[0][devicesKeys[i]]['threshold'];

        }
    }

    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById("showData");
    divContainer.innerHTML = "";
    divContainer.appendChild(table);

}