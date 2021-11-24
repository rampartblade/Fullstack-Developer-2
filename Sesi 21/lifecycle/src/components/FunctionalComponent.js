import React, { useState, useEffect } from "react";

function FunctionalComponent(){

    const [date, setDate] = useState(new Date())
    const [timecolor, setTimecolor] = useState("Clock")

    function tick(){
        setDate(new Date())
    }

    useEffect(()=>{
        const interval = setInterval(tick, 1000)
        return function(){
            clearInterval(interval)
        }
    })

    const changeColor=() => setTimecolor("clock")

    return(
        <div >
            <h1>Jam nyala dengan button</h1>
            <hr/>
            <h1 className = {timecolor}>{date.toLocaleTimeString()}</h1>
            <button onClick={changeColor}>Change Color</button>
        </div>
    )
}

export default FunctionalComponent