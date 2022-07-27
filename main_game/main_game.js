let health = document.getElementById("health")

function slot1() {
  
  
    if (health.value > 0) {
      health.value -= 10;
      console.log("-10")
    } else {
      health.value = 0;
    } 
}