import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [placeholder, setPlaceholder] = useState('');
  const [time, setTime] = useState(0);
  const [paragraphStyle, setparagraphStyle] = useState({
    backgroundColor: "#f00"
  })
  const [paragraphClass, setparagraphClass] = useState("Paragraph Red")

  useEffect(()=>{
    fetch('/hello').then(res => res.json()).then(data=>{
      setPlaceholder(data.result); //console.log(data)
    });
    fetch('/time').then(res => res.json()).then(data=>{
      setTime(data.time)
    })
  }, []);

  const changeStyle = () => setparagraphStyle({
    backgroundColor: "#00f"
  })

  const changeStyleClass= () => setparagraphClass("Paragraph Blue")

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p /* style={paragraphStyle} */ className={paragraphClass}>Flask says {placeholder}</p> <br/>
        <p>The current time is : {time}</p>
        <button onClick={changeStyleClass}>Change color</button>
      </header>
    </div>
  );
}

export default App;
