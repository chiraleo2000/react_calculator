import React, { useState } from 'react';

function ParabolicCalculator() {
  const [vertex, setVertex] = useState('');
  const [point, setPoint] = useState('');
  const [result, setResult] = useState('');

  const calculateParabola = () => {
    const [h, k] = vertex.split(',').map(Number);
    const [x, y] = point.split(',').map(Number);
    const a = (y - k) / Math.pow((x - h), 2);
    setResult(`Parabolic equation: y = ${a}(x - ${h})^2 + ${k}`);
  };

  return (
    <div>
      <h2>Parabolic Calculator</h2>
      <input type="text" value={vertex} onChange={(e) => setVertex(e.target.value)} placeholder="Enter vertex (h,k)" />
      <input type="text" value={point} onChange={(e) => setPoint(e.target.value)} placeholder="Enter a point (x,y)" />
      <button onClick={calculateParabola}>Calculate</button>
      {result && <p>{result}</p>}
    </div>
  );
}

export default ParabolicCalculator;
