    //exercise 1
    
    // question 1 
    let data = {
        username: "",
        password: ""
    }   

    // question 2 

    let newfeed = [data, username , timeline]
 
    for (let index = 0; index < 15; index++) {
          if( index%2 === 0){
              console.log(index + "le nombre est paire");
          } else if (index %2 !== 0 ) { 
              console.log(index + "le nombre est impair"); 
            }
       }




       let names= ["john", "sarah", 23, "Rudolf",34];

       for (let index = 0; index < names.length; index++) {
           if(typeof(index) !== "string"){
               continue;
               console.log(index);
           } else if (typeof(names) === "string"){
               if (index[0] !== index[0].toLowerCase()) {
                   index[0].toUpperCase();
                   console.log(index);
               }
           }
       }

       // question


       for (let index = 0; index < names.length; index++) {
           if (typeof(index) !== 'string' ) {m
               break; 
           } else if (typeof(index) === 'string') {
               console.log(index);
           }
       }


       // Learning Loop exercise 

       // exercise 1 list of people 

       let people = ["Greg", "Mary", "Devon" , "James"];

       // question 1 

       people.shift();

       // question 2

       people.splice(people.length -1 , 1 , "Jason");

       // Question 3

       people.push("etienne");

       // Question 4

       console.log(people.indexOf("Mary"));

       // question 5 

       let copyPeople = people.slice(people.indexOf("Mary") , 1 )

       // question 
        
       people.indexOf("Foo");

       // question 7

       let last = people.length - 1

       //


       // exercise 5

       let famillies = {
           
       }
