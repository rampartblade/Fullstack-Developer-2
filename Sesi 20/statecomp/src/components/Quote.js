import React, { useState } from "react";

/* const Quote = (props) => {   //ini merupakan arrow function dari Quote
    //membuat stateless component
    //menjadi stateful component
    //dengan menggunakan hok useState()

    //pengggunaannya :
    //const [state, setState] = useState()
    const [quote] = useState(props.quote)
} */

function Quote(props) {
    const [quote] = useState(props.quote)

    return(
        <>
            <blockquote>
                {/* {props.quote} */}
                {quote}
            </blockquote>
        </>
    )
}

export default Quote