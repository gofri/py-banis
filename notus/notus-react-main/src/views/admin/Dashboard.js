import React from "react";

// components

import CardLineChart from "components/Cards/CardLineChart.js";
import CardBarChart from "components/Cards/CardBarChart.js";
import CardPageVisits from "components/Cards/CardPageVisits.js";
import CardSocialTraffic from "components/Cards/CardSocialTraffic.js";
import axios from 'axios';
import APIClient from "api/client.js";

export default function Dashboard() {
	/*
axios
.get("http://localhost:5000/backend")
.then(response => {
    // manipulate the response here
console.log(response)
})
.catch(function(error) {
    // manipulate the error response here
});
	*/
	const items = new APIClient().backend().then(function(items) { console.log(items.a); });
	new APIClient().customers().then(function(items) { console.log(items); });

  return (
    <>
	  items
    </>
  );
}
