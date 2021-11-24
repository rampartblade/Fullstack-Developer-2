import React, { useState } from 'react';
import logo from './logo.svg';
import fidget from './fidget.gif'
import test from './test.gif';
import './App.css';
import FetchComponent from './components/FetchComponent';
import ClassComponent from './components/ClassComponent';
import FunctionalComponent from './components/FunctionalComponent';
import Sound from 'react-sound';
import song from './Kingdom Hearts II.mp3'
import butterfly from './butterfly.mp3'
import Paradigm from './Paradigm.mp3'

function App() {
  const audio = ()=>{
    new Audio(butterfly).play();
  }
  return (
    <div className="App">
      <Sound
          url = {song}
          //url = {Paradigm}
          playStatus = {Sound.status.PLAYING}
          //onLoad={true}
          volume = {30}
          //autoLoad = {true}
          loop = {true}
      />
      <header className="App-header">
        <ClassComponent/>
        <img src={test} className="App-logo" alt="logo" />
        {/* <FetchComponent/> */}
        <FunctionalComponent/>
        <button onClick={audio}>test audio</button>
      </header>
    </div>
  );
}

export default App;
