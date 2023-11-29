import React, { useState } from 'react';

function BasicCalculator() {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  const [operation, setOperation] = useState('Add');
  const [result, setResult] = useState('');

  const calculate = () => {
    let calculationResult;

    switch (operation) {
      case 'Add':
        calculationResult = num1 + num2;
        break;
      case 'Subtract':
        calculationResult = num1 - num2;
        break;
      case 'Multiply':
        calculationResult = num1 * num2;
        break;
      case 'Divide':
        calculationResult = num2 !== 0 ? num1 / num2 : 'Cannot divide by zero';
        break;
      default:
        calculationResult = 'Invalid operation';
    }

    setResult(calculationResult);
  };

  return (
    <div>
      <h2>Basic Calculator</h2>
      <input type="number" value={num1} onChange={e => setNum1(+e.target.value)} placeholder="First Number" />
      <input type="number" value={num2} onChange={e => setNum2(+e.target.value)} placeholder="Second Number" />
      <select value={operation} onChange={e => setOperation(e.target.value)}>
        <option value="Add">Add</option>
        <option value="Subtract">Subtract</option>
        <option value="Multiply">Multiply</option>
        <option value="Divide">Divide</option>
      </select>
      <button onClick={calculate}>Calculate</button>
      {result !== '' && <p>Result: {result}</p>}
    </div>
  );
}

export default BasicCalculator;