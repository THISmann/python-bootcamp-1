let num1 = "";
let num2 = "";
let result = "";
let op = "";

function number(num){
    num1 = num1.concat(num);

    console.log(num1); 
    return num;
}



function operator(operator){
    console.log(operator);
    op = operator;
    return true;
}

let Op = operator(operator);

function equal(num1 , num2 , result ){
    switch (op){
        case "+":
            result = num1 + num2;
            break;

            case "-":
                result = num1 - num2;
                break;

                case "*":
                    result = num1 * num2;
                    break;

                    case "/":
                        result = num1 / num2;
                        break;

                        default:
                            console.log("error");

    }

    return result;
}

 