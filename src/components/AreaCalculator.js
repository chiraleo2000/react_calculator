import React, { useState } from 'react';

function AreaCalculator() {
  const [shape, setShape] = useState('Circle');
  const [dimensions, setDimensions] = useState('');
  const [result, setResult] = useState('');

  const calculateArea = () => {
    const dimensionArray = dimensions.split(',').map(Number);
    let area;

    switch (shape) {
      case 'Circle':
        const radius = dimensionArray[0];
        area = Math.PI * radius * radius;
        break;
      case 'Square':
        const side = dimensionArray[0];
        area = side * side;
        break;
      case 'Rectangle':
        const [length, width] = dimensionArray;
        area = length * width;
        break;
      default:
        area = 0;
    }

    setResult(`Area of ${shape}: ${area.toFixed(2)}`);
  };

  return (
    <div>
      <h2>Area Calculator</h2>
      <select value={shape} onChange={(e) => setShape(e.target.value)}>
        <option value="Circle">Circle</option>
        <option value="Square">Square</option>
        <option value="Rectangle">Rectangle</option>
      </select>
      <input type="text" value={dimensions} onChange={(e) => setDimensions(e.target.value)} placeholder="Enter dimensions" />
      <button onClick={calculateArea}>Calculate</button>
      {result && <p>{result}</p>}
    </div>
  );
}

export default AreaCalculator;
