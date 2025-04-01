import { Line } from "react-chartjs-2";
import { useState, useEffect } from "react";
import axios from "axios";

export default function TrendChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("https://backend-url/trend").then((res) => setData(res.data));
  }, []);

  return (
    <Line data={{
      labels: data.map(d => d.date),
      datasets: [{ label: "House Price Trend", data: data.map(d => d.price), borderColor: "blue" }]
    }} />
  );
}