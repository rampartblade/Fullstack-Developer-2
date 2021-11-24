import { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import PersonInformation from './components/PersonInformation';

function Header(){
  return(
    <header className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      <PersonInformation />
    </header>
  )
}

function Content(){
  return(
    <div className="Content">
      <p>
        Silahkan isikan dengan paragraf yang kamu kehendaki
      </p>
    </div>
  )
}

function Footer(){
  return(
    <div className="Footer">
      <p>&copy; My Self- 2021</p>
    </div>
  )
}

function App() {
  //const [ quote ] = useState(props.quote) 
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <PersonInformation />
      </header> */}
      <Header/>
      <hr/>
      <Content/>
      <hr/>
      <Footer/>
      <hr/>
    </div>
  );
}

export default App;
