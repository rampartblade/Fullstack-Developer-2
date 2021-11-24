function showTerminal(message){
    console.log(message)
}

function greeting(name, callback){
    const value = `Halo! Nama saya ${name}. Senang bertemu dengan FSD Batch 1 OCBC`

    callback(value)
}

greeting("akward", showTerminal)

