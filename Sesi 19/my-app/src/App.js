import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
//import Proptypes from 'prop-types';

class App extends Component {

  constructor(){
    super()
    this.state = {
      title: 'sesi 19',
      name: 'asdawd',
      scope:{
        project: "Ei",
        founded: "1970"
      }
    }
  }

  getScope(){
    return this.state.scope
  }

/*   changeTitle = (event) => {
    console.log(event)
    this.setState({
      title: "Final Project - React JS"
    })
  } */


  changeTitle(){
    this.setState ({
      title: 'final project'
    })
  }

  render(){
    return  (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <h3>Project Name: {this.getScope().project} | Founded: {this.getScope().founded} | Score: {this.props.score}</h3>
          <h1> {this.state.name} by {this.state.title}</h1>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <button onClick={this.changeTitle.bind(this)}>change title</button>
        </header>
      </div>
    );
  }
}

export default App;
