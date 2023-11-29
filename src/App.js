import React, { useState } from 'react';
import BasicCalculator from './components/BasicCalculator';
import ParabolicCalculator from './components/ParabolicCalculator';
import AreaCalculator from './components/AreaCalculator';
import VolumeCalculator from './components/VolumeCalculator';

function App() {
  const [activeTab, setActiveTab] = useState('basic');

  const renderCalculator = () => {
    switch (activeTab) {
      case 'basic':
        return <BasicCalculator />;
      case 'parabolic':
        return <ParabolicCalculator />;
      case 'area':
        return <AreaCalculator />;
      case 'volume':
        return <VolumeCalculator />;
      default:
        return null;
    }
  };

  return (
    <div className="App">
      <h1>Calculator App</h1>
      <div className="tabs">
        <button onClick={() => setActiveTab('basic')}>Basic Calculator</button>
        <button onClick={() => setActiveTab('parabolic')}>Parabolic Calculator</button>
        <button onClick={() => setActiveTab('area')}>Area Calculator</button>
        <button onClick={() => setActiveTab('volume')}>Volume Calculator</button>
      </div>
      <div className="calculator-content">
        {renderCalculator()}
      </div>
    </div>
  );
}

export default App;
