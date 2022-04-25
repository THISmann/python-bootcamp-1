let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

// question  2

let shoppingList = ["banana", "orange", "apple" ];

// question 3

function myBill(){
    let totalPrice = [prices.banana, prices.orange, prices.apple];
    let sum = totalPrice.reduce((previousValue, currentValue ) => {
        previousValue + currentValue;
    })
    console.log(sum);
    return sum;
}

myBill(); 