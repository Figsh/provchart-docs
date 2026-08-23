/**
 * Example React app using ProvChart.
 */

import { useState, useEffect } from 'react';
import { Chart } from './Chart';

export default function App() {
  const [points, setPoints] = useState([20, 25, 21, 37, 30, 60, 27, 50]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch('/api/chart-data');
      const data = await res.json();
      setPoints(data.points);
    }

    fetchData();
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <Chart points={points} />
    </div>
  );
}
