const input = document.getElementById("inputText");

if (input){

    input.addEventListener("input", function(){

        const text = input.value;

        const characters = text.length;

        const bytes = new TextEncoder().encode(text).length;

        document.getElementById("counter").innerHTML =
            `Characters : ${characters} | Bytes : ${bytes}`;

    });

}

function copyHash(){

    const hash = document.getElementById("generatedHash");

    hash.select();

    document.execCommand("copy");

    alert("Hash Copied!");

}

function clearGenerator(){

    document.getElementById("inputText").value="";

    if(document.getElementById("generatedHash")){

        document.getElementById("generatedHash").value="";

    }

    document.getElementById("counter").innerHTML =
        "Characters : 0 | Bytes : 0";

}