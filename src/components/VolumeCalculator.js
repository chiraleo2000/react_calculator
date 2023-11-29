import React, { useState } from 'react';

function VolumeCalculator() {
  const [objectType, setObjectType] = useState('Sphere');
  const [dimensions, setDimensions] = useState('');
  const [result, setResult] = useState('');

  const calculateVolume = () => {
    const dimensionArray = dimensions.split(',').map(Number);
    let volume;

    switch (objectType) {
      case 'Sphere':
        const radius = dimensionArray[0];
        volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
        break;
      case 'Cube':
        const side = dimensionArray[0];
        volume = Math.pow(side, 3);
        break;
      default:
        volume = 0;
    }

    setResult(`Volume of ${objectType}: ${volume.toFixed(2)}`);
  };

  return (
    <div>
      <h2>Volume Calculator</h2>
      <select value={objectType} onChange={(e) => setObjectType(e.target.value)}>
        <option value="Sphere">Sphere</option>
        <option value="Cube">Cube</option>
      </select>
      <input type="text" value={dimensions} onChange={(e) => setDimensions(e.target.value)} placeholder="Enter dimensions" />
      <button onClick={calculateVolume}>Calculate</button>
      {result && <p>{result}</p>}
    </div>
  );
}

export default VolumeCalculator;
