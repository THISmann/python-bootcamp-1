// exercise 1 

let fruits = ["bannana", "apples" , "oranges" , "BLeuberries"];

// question 1
fruits.shift();

// question 2 
fruits.sort();

// question 3
fruits.push("wiki");

// question 4 
fruits.splice(0,1);

//question 5
fruits.reverse();



// exercise 2 
let moreFruits = ["Banana" , ["Apples", ["Oranges"], "Bleuberries"]];
console.log(moreFruits[1][1])

 

// Dayli challenge 2
// question 1 

let array = ["*", "*" , "*", "*" , "*"];

for (let index = 0; index < array.length; index++) {
    console.log("*");
}

// temperature exercise

let temperature = prompt();

if(temperature < 0 ){
    console.log("etat solide");
} else if(temperature >= 0 && temperature < 100){
    console.log("etat liquide");
} else if(temperature >= 100) {
    console.log("etat gazeuz");
}

// Make a keyless car!

driver = prompt();
if(driver < 18){
    console.log("sorry , you are to young to drive this car powering off");
} else if (driver = 18){
    console.log("congratulations on your first year of driving, Enjoy the ride !");
} else if(driver > 18){
    console.log("powering On. Enjoy the ride!");
}

    //exercise 1
    
    // question 1 
    let data = {
        username: "",
        password: ""
    }   

    // question 2
    let database = [data] 

    // question 3 

    let obj = {
        username: "",
        timeline: 0 
    } 

    let obj2 = {
        username: "",
        timeline: 0 
    } 

    let obj3 = {
        username: "",
        timeline: 0 
    } 

    let newfeed = [data, obj1, obj2 , obj3 ]

