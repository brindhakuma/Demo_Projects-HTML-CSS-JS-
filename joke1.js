const btnEl = document.getElementById("btn")
const jokeEl = document.getElementById("joke")
const apiKey = "ODA6WYoONfGQMLN/L5jZOw==vfemaWmVBtmBfHLE";




const options = {
    method: "GET",
    headers: {
        "X-Api-Key": apiKey,
    },
};
const apiURL = "https://api.api-ninjas.com/v1/dadjokes?limit=1";

async function getJoke(){
    try{jokeEl.innerText = "updating";
    btnEl.disabled = true;
    btnEl.innerText="loading.....";
const response = await fetch(apiURL,options);
const data = await response.json();
console.log(data);
jokeEl.innerText= (data[2].joke);

btnEl.disabled=false;
btnEl.innerText="tell me a joke"

}  catch(error){
    jokeEl.innerText="an error happened try again later";
    btnEl.disabled=false;
btnEl.innerText="tell me a joke";
}

}


btnEl.addEventListener('click',getJoke)