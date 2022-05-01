function getvalue(){
    let val1 = document.forms['form1'][0].value;
    let val2 = document.forms['form1'][1].value;
    console.log(val1, val2);
    return val1, val2;
}

 //get the select form
 let dropdown = document.getElementById('A')

 // all three lines do the same thing
 dropdown.options[2].selected = true; //Banana selected
 dropdown.value = 'banana'; //Banana selected
 dropdown.selectedIndex = 2; //Banana selected

 // To check which option is selected
   console.log(dropdown.selectedIndex) // "2"
   console.log(dropdown.value) // "Banana"

function test(){
    let sel = document.getElementById("select1");
    let val2 = sel.options[1].value;
    console.log(val2);
}   

let inputs = table.getElementsByTagName('input');

for (let input of inputs) {
  alert( input.value + ': ' + input.checked );
}


let form = document.forms.my;

            form.addEventListener("submit", test)

            function test(e){
              alert('submit ! ')
              e.preventDefault()
            }