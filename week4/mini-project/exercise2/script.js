let num1 = "";
let num2 = "";
let result = 0;
let op = "";

function number(num){  

    if(op.length !== 1){
        num1 = num1.concat(num);
    } else {
        num2 = num2.concat(num);
    }

    console.log(num1 , num2);  
}



function operator(operator){
    console.log(operator);
    op = operator; 
}
 

function equal(num1 , num2 , result ){
    switch (op){
        case "+":
            result =  parseInt(num1 + num2) ;
            break;

            case "-":
                result = parseInt(num1) - parseInt(num2);
                break;

                case "*":
                    result = parseInt(num1) * parseInt(num2);
                    break;

                    case "/":
                        result = parseInt(num1) / parseInt(num2);
                        break;

                        default:
                            console.log("error");

    }
    console.log(result);
    return result;
}

 