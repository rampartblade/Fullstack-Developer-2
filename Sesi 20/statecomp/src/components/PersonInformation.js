import React, { Component, useEffect, useState } from 'react';
import Quote from './Quote';

/* function PersonInformation() {
    const [name, setName] = useState("Jimmy")
    const [age, setAge] = useState(17)
    const [quote] = useState("Tiada hari tanpa ngoding React")
    
      const  [personData, setPersonData] = useState({
      name: "Jimmy",
      age : 17,
      quote: "Tiada hari tanpa ngoding react"
      })

    return (
            <>
            <h1>Person Information</h1>
            <div>
                <span>Name: {this.state.name}</span> <br/>
                <span>Age: {this.state.age}</span> <br/>
                <span>Quote: <Quote quote={this.state.quote}/></span>
            </div>
            </>
        );  
     
}

const changeName = () => {
    const newName = name + 5
    setName(newName)
    setPersonData({
        ...personData,
        name: newName
    })
}

const changeAge = () => {
    const newAge = age + 1
    setAge(newAge)
    //setAge(age + 1)
} */

class PersonInformation extends Component{

    //useState()
    /**
     * const  [personData, setPersonData] = useState({
     *  name: "Jimmy",
     *  age : 17,
     *  quote: "Tiada hari tanpa ngoding react"
     * })
     */
    constructor(){
        super()
        this.state = {
            name: "Jimmy",
            age: 17,
            quote: "Tiada hari tanpa ngoding React"
        }
    }

    changeName = () => {
        this.setState ({
            //name: "Jimbo" + 5
            name: this.state.name + 5
            
        })
    }

    changeAge() {
        this.setState ({
            age: this.state.age + 5
        })
    }

    render(){
        return (
            <>
            <h1>Person Information</h1>
            <div>
                <span>Name: {this.state.name}</span> <br/>
                <span>Age: {this.state.age}</span> <br/>
                <span>Quote: <Quote quote={this.state.quote}/></span>
            </div>
            {/**/}
            <button onClick={this.changeName.bind(this)}>Change Me</button><br/>
            <button onClick={this.changeAge.bind(this)}>Change Age</button>
            </>
        );
    }

}
export default PersonInformation;
