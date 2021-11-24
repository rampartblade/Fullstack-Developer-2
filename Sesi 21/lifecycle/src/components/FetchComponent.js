import { useState, useEffect } from 'react';

export default function FetchComponent () {
    const [ baseURL ] = useState('https://cat-fact.herokuapp.com')
    const [ facts, setFacts] = useState([])

    useEffect(() => {
        fetch(`${baseURL}/facts`)
        /* .then(response => console.log(response))
        .then(result => console.log(result)) */
        .then(response => response.json())
        .then(result => setFacts(result))
    }, [])

    return(
    <>
        {
            /* facts.map(fact => (
            <>{JSON.stringify(fact)}</>
            )) */
            facts.map(fact => (
                <div key={fact._id}>
                    <td>{fact.text}</td>
                </div>
            ))
        } 
    </>)
}