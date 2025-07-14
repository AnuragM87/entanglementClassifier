import React, { useState } from 'react';

function App() {
  const [generated, setGenerated] = useState(null);
  const [customFeatures, setCustomFeatures] = useState(['', '', '', '']);
  const [customResult, setCustomResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    setGenerated(null);
    const res = await fetch('http://localhost:8000/generate-state');
    const data = await res.json();
    setGenerated(data);
    setLoading(false);
  };

  const handleCustomChange = (idx, value) => {
    const arr = [...customFeatures];
    arr[idx] = value;
    setCustomFeatures(arr);
  };

  const handleClassify = async (e) => {
    e.preventDefault();
    setLoading(true);
    setCustomResult(null);
    const features = customFeatures.map(Number);
    const res = await fetch('http://localhost:8000/classify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ features }),
    });
    const data = await res.json();
    setCustomResult(data.prediction);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>Entanglement Classifier</h1>
      <section style={{ marginBottom: '2rem', padding: '1rem', border: '1px solid #ccc', borderRadius: 8 }}>
        <h2>Generate Random Quantum State</h2>
        <button onClick={handleGenerate} disabled={loading}>
          {loading ? 'Generating...' : 'Generate State'}
        </button>
        {generated && (
          <div style={{ marginTop: 16 }}>
            <div><b>Features:</b> {generated.features.map(f => f.toFixed(4)).join(', ')}</div>
            <div><b>Label:</b> {generated.label === 1 ? 'Entangled' : 'Separable'}</div>
          </div>
        )}
      </section>
      <section style={{ padding: '1rem', border: '1px solid #ccc', borderRadius: 8 }}>
        <h2>Classify Custom State</h2>
        <form onSubmit={handleClassify}>
          <div style={{ display: 'flex', gap: 8, marginBottom: 8 }}>
            {customFeatures.map((val, idx) => (
              <input
                key={idx}
                type="number"
                step="any"
                value={val}
                onChange={e => handleCustomChange(idx, e.target.value)}
                placeholder={`Feature ${idx + 1}`}
                required
                style={{ width: 100 }}
              />
            ))}
          </div>
          <button type="submit" disabled={loading}>
            {loading ? 'Classifying...' : 'Classify'}
          </button>
        </form>
        {customResult !== null && (
          <div style={{ marginTop: 16 }}>
            <b>Prediction:</b> {customResult === 1 ? 'Entangled' : 'Separable'}
          </div>
        )}
      </section>
    </div>
  );
}

export default App;
