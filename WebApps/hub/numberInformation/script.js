function calc(){
    var ddl = document.getElementById("selector");
    var selectedValue = ddl.options[ddl.selectedIndex].value;

    if(selectedValue === "kgv"){
        kgv(document.getElementById("firstNumber").value, document.getElementById("secondNumber").value);
    }
    else{
        console.log(selectedValue);
        ggd(document.getElementById("firstNumber").value, document.getElementById("secondNumber").value);
    }
}

function kgv(fn, sn){
    var kgvn = 1;
    while(fn != sn){
        kgvn++;
        fn = fn*kgvn;
        sn = sn*kgvn;
    }
    console.log(kgvn);
    return kgv;
}