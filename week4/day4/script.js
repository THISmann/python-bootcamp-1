function myFunction(myAge){
    let mum = myAge * 2;
    let dad = mum*1.2;
    console.log("the age of my mum and my dad " + mum + " " + dad);
}

function secondFunction(myAge){
    let mum = myAge * 2;
    return mum;
}

console.log(secondFunction(12));

var funcName = function(parameter){

}

const calculorTip = () => {
    let billPrice = parseInt(prompt(" what amount the bill"));
    let tip = 0;
    switch (billPrice){

        case billPrice < 50 :
             tip = billPrice*0.2;
            break;

            // case billPrice > 50 && billPrice < 200:
            //     tip = billPrice*0.15;
            //     break;

            //     case billPrice > 200 :
            //         tip = billPrice*0.1;
            //         break;  

    }

    console.log(typeof(tip)) ;
    console.log("tip value"+ billPrice);
    return tip;
}

calculorTip();