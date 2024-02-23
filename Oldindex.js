import "./styles.css";

const button = document.querySelector("button")
const level = document.querySelector("#level")
  
button.addEventListener("click" , () => {
  level.innerText++
})
