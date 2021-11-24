import React from "react";
import './test.css'
class ClassComponent extends React.Component {

    constructor(){
        super()
        this.state = {
            date: new Date()
        }
    }
    
    tick(){
        this.setState({
            date: new Date()
        })
    }

    componentDidMount(){
        //this.timerID = setInterval(() => this.tick(), 1000)
        this.timerID = setInterval(this.tick.bind(this), 1000)
    }

    componentWillUnmount(){
        clearInterval(this.timerID)
    }

    render(){
        return(
            <div>
                <h1>Jam Nyala</h1>
                <hr/>
                <h1 className="clock">{this.state.date.toLocaleTimeString()}</h1>
            </div>
        );
    }
}

export default ClassComponent;