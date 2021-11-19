


function getAllData(){
fetch("newapi").then(data => data.json()).then(data => {
console.log("i am ",data)
console.log("type is ", typeof(data))
const myArr = JSON.St(data);

document.getElementById("employee_data")  = myArr[0]

})
}

