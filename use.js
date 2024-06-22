const ratingEls = document.querySelectorAll(".rating");

const btnEl = document.querySelector(".btn")
const containerEl = document.querySelector(".container")
let selectedRating = "";
ratingEls.forEach((ratingEl) => {
    ratingEl.addEventListener("click",(event)=>{
        removeActive();
        selectedRating = 
        event.target.innerText || event.target.parentNode.innerText;
        event.target.classList.add("active")
         event.target.parentNode.classList.add("active")  

    
    });
});

btnEl.addEventListener("click", () => {
if(selectedRating !== ""){
containerEl.innerHTML = `<strong> thankyou </strong>
<br>
<br>
<strong>Feedback:${selectedRating}</strong>
<p>we will use your feedback to improve pur customer support</p>`;
}

}); 
function removeActive() {
ratingEls.forEach((ratingEl) => {
ratingEl.classList.remove("active")


});

}