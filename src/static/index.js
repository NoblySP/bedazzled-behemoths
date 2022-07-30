const health = document.getElementById("health")
const slotEls = document.querySelectorAll(".slot")
let protocol;
if (window.location.protocol == "http:") {
    protocol = "ws://"
} else {
    protocol = "wss://"
}

health.addEventListener("click", subtractHealth)
let highlightedId;
slotEls.forEach(slotEl => {
    slotEl.addEventListener("click", () => {
        highlightedId = slotEl.id
        for (let i = 0; i < slotEls.length; i++){
            slotEls[i].classList.remove("highlighted")
        }
        slotEl.classList.add("highlighted")
    })
})

// const socket = new WebSocket("ws://localhost:8000")
// socket.addEventListener("open", () => console.log("connected"))
// socket.addEventListener("message", (e) => console.log(e.data))
let id = Math.floor(Math.random() * 50000)
function connect(socketName){
    const socket = new WebSocket(socketName)
    socket.addEventListener("open", () => console.log("connected"))
    socket.addEventListener("message", (e) => {
        console.log(e.data)
        let data = JSON.parse(e.data)
        if (data?.rooms){
            const rooms = data.rooms
            rooms.map(room => {
                if (id === room){
                    id = Math.floor(Math.random() * 50000)
                    connect(`${protocol}${window.location.host}/${id}`)
                }
            })
        }
        console.log(data?.action)
        switch(data?.action) {
            case "reduce":
                health.value -= data.value
                break;
            case "add":
                health.value += data.value
                break;
            case "mult":
                health.value *= data.value
                break;
            case "divide":
                health.value /= data.value
                break
            default:
                console.error("Action is not valid")
        }
    })
}

connect(`${protocol}${window.location.host}/${id}`)
function subtractHealth() {
    if (health.value > 0) {
        health.value -= 1;
        console.log(health.value)
    } else {
        health.value = 0;
    }
}
