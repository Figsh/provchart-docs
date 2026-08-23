/**
 * React component for ProvChart.
 *
 * Note: ProvChart is a CSS technology. This component
 * provides a convenient React wrapper.
 */

import { useEffect, useRef } from 'react';
import './Chart.css';

export function Chart({ points, className = '' }) {
  const chartRef = useRef(null);

  useEffect(() => {
    if (!chartRef.current || !points) return;

    const vars = points
      .map((v, i) => `--st-p${i + 1}: ${100 - v}%`)
      .join('; ');

    chartRef.current.style.cssText = vars;
  }, [points]);

  return (
    <div className={`chart ${className}`} ref={chartRef}>
      <div className="chart-fill"></div>
      <div className="chart-line"></div>
    </div>
  );
}

export default Chart;
