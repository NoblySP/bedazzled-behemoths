const health = document.getElementById("health")
const slotEls = document.querySelectorAll(".slot")

health.addEventListener("click", subtractHealth)
let highlightedId;
slotEls.forEach(slotEl => {
    slotEl.addEventListener("click", () => {
        highlightedId = slotEl.id
        for(let i = 0; i < slotEls.length; i++){
            slotEls[i].classList.remove("highlighted")
        }
        slotEl.classList.add("highlighted")
    })
})

const socket = new WebSocket("ws://localhost:8000")
socket.addEventListener("open", () => console.log("connected"))

function subtractHealth() {
    if (health.value > 0) {
      health.value -= 10;
      console.log(health.value)
    } else {
      health.value = 0;
    }
}
