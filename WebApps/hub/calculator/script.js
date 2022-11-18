var currentNumber = 0;
var hasComma = false;
var firstNumber= true;
var currentFunction = 0;

//reg functions
function addNumber(n){
    if(gaveAnswer === true){
        ac();
    }
    if(currentNumber[0] == 0){
        currentNumber = n;
    }
    else{
        currentNumber = (currentNumber*10) + n;
    }
    updateNumber();
}


//CLEAR FUNCTIONS
function ac(){
    currentNumber = 0;
    lastNumber = 0;
    gaveAnswer = false;
    firstNumber = true;
    updateNumber();
}
function c(){
    currentNumber = 0;
    updateNumber();
}
function back(){
    if(currentNumber !== 0){
        currentNumber = (currentNumber - (currentNumber % 10)) / 10;
    }
    updateNumber();
}


//CALC FUNCTIONS
var lastNumber = 0;
function add(){
    if(firstNumber === true){
        firstNumber = false;
        lastNumber = currentNumber;
        currentNumber = 0;
    }
    else{
        lastNumber = lastNumber + currentNumber;
        currentNumber = 0;
    }
    updateNumber();
    currentFunction = 1;
}
function sub(){
    if(firstNumber === true){
        firstNumber = false;
        lastNumber = currentNumber;
        currentNumber = 0;
    }
    else{
        lastNumber = lastNumber - currentNumber;
        currentNumber = 0;
    }
    updateNumber();
    currentFunction = 2;
}
function multiply(){
    if(firstNumber === true){
        firstNumber = false;
        lastNumber = currentNumber;
        currentNumber = 0;
    }
    else{
        lastNumber = lastNumber * currentNumber;
        currentNumber = 0;
    }
    updateNumber();
    currentFunction = 3;
}
function divide(){
    if(firstNumber === true){
        firstNumber = false;
        lastNumber = currentNumber;
        currentNumber = 0;
    }
    else{
        lastNumber = lastNumber / currentNumber;
        currentNumber = 0;
    }
    updateNumber();
    currentFunction = 4;
}


//ANSWER FUNCTION
var gaveAnswer = false;
var answer = 0;
function giveAnswer(){
    switch(currentFunction){
        //add
        case 1:
            add();
            break;
        
        //sub
        case 2: 
            sub();
            break;

        //multiply
        case 3:
            multiply();
            break;
        
        //divide
        case 4:
            divide();
            break;
    }

    document.getElementById("answer").innerHTML = lastNumber;
    console.log(lastNumber);
    gaveAnswer = true;
}


//REPEATING FUNCTIONS
function updateNumber(){
    document.getElementById("answer").innerHTML = currentNumber;
    console.log(currentNumber);
}