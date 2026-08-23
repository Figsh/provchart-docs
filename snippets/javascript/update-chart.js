/**
 * Update a ProvChart chart with new data points.
 *
 * @param {HTMLElement} element - The chart container element
 * @param {number[]} points - Array of 8 values (0-100)
 */
function updateChart(element, points) {
  const vars = points
    .map((v, i) => `--st-p${i + 1}: ${100 - v}%`)
    .join('; ');
  element.style.cssText = vars;
}

/**
 * Normalize raw data to 0-100 scale.
 *
 * @param {number} value - Raw data value
 * @param {number} min - Minimum value in dataset
 * @param {number} max - Maximum value in dataset
 * @returns {string} CSS percentage string
 */
function normalizePoint(value, min, max) {
  const normalized = ((value - min) / (max - min)) * 100;
  return `${normalized.toFixed(2)}%`;
}

/**
 * Update chart from raw data.
 *
 * @param {HTMLElement} element - The chart container element
 * @param {number[]} rawData - Array of raw data values
 */
function updateFromRawData(element, rawData) {
  const min = Math.min(...rawData);
  const max = Math.max(...rawData);
  const vars = rawData
    .map((v, i) => `--st-p${i + 1}: ${normalizePoint(v, min, max)}`)
    .join('; ');
  element.style.cssText = vars;
}
