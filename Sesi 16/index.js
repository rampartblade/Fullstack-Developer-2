let arr = [
    [1, 2, 3],
    [4, 5],
    [91, 8, 10, 30]
]
console.log(arr)

arr[0].shift()
console.log(arr)

arr[1].unshift(4,5)
console.log(arr)
console.log(arr[0])

console.log(this)

function whatever(){
    abilites = [1 , 2, 3]
    console.log(this)
}

whatever()

//function di dalam function
function currryFunction(a,b){
    const c = a + b
    return function (d){
        console.log(c + d)
    }
}

const obj = {
    name: "asdawd",
    role: "fullstack",
    age: 62
}

const{name: fullName, role: job} = obj
console.log(fullName, job)
console.log(obj.name, obj.role)

const{name, ...another} = obj
console.log(name, another)

const anotherCurryFunction = (a, b) => (c, d) => (a + b) - (c + d)
const anotherCurryFunction2 = (a,b) => ({a, b})

currryFunction(10,20)(30)
console.log(anotherCurryFunction(10,20)(30,40))

const addNumbers = anotherCurryFunction(10, 20)
console.log(addNumbers(30,40))
console.log(anotherCurryFunction2(30,40))