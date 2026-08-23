/**
 * Next.js page with ProvChart integration.
 *
 * ProvChart is a CSS technology. This shows how to
 * use compiled CSS in a Next.js project.
 *
 * Steps:
 * 1. Compile .fscss to .css: fscss style.fscss style.css
 * 2. Import the compiled CSS
 * 3. Use CSS variables for dynamic data
 */

'use client';

import { useState, useEffect } from 'react';
import '../styles/chart.css';

export default function Dashboard() {
  const [points, setPoints] = useState<number[]>([20, 25, 21, 37, 30, 60, 27, 50]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch('/api/chart-data');
      const data = await res.json();
      setPoints(data.points);
    }

    fetchData();
  }, []);

  const chartStyle = points.reduce((acc, v, i) => {
    acc[`--st-p${i + 1}`] = `${100 - v}%`;
    return acc;
  }, {} as Record<string, string>);

  return (
    <div>
      <h1>Dashboard</h1>
      <div className="chart" style={chartStyle as React.CSSProperties}>
        <div className="chart-fill"></div>
        <div className="chart-line"></div>
      </div>
    </div>
  );
}
