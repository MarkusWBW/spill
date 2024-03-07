// Velg HTML-elementer
const circle1 = document.getElementById("sirkel1");
const circle2 = document.getElementById("sirkel2");
const time = document.getElementById("tid");
const count = document.getElementById("tall");
const resetButton = document.getElementById("restart-knapp");
const startButton = document.getElementById("start-knapp")

// Sett variabler
let remainingTime = 10;
let clickCount1 = 0;
let clickCount2 = 0;
let timer;
let gameEnded = false; 



// Lytt etter klikk på sirkel 1
circle1.addEventListener("click", () => {
  if (!gameEnded) {
    clickCount1++;
    document.getElementById("score1").textContent = clickCount1;
    count.textContent = totalClickCount;
    
  }
});

// Lytt etter klikk på sirkel 2
circle2.addEventListener("click", () => {
  if (!gameEnded) {
    clickCount2++;
    document.getElementById("score2").textContent = clickCount2;
    count.textContent = totalClickCount;
  }
});

// Lytt etter tastetrykk
document.addEventListener("keydown", event => {
  const key = event.key.toLowerCase();
  if (key === "s") {
    circle1.click();
  } else if (key === "l") {
    circle2.click();
  }
});

// Lytt etter klikk på reset-knappen
resetButton.addEventListener("click", () => {
  resetGame();
  //window.location.reload()
});

/* resetButton.addEventListener("click", () => {
  startTimer();
}); */

// Start nedtelling av tid
function startTimer() {
  timer = setInterval(() => {
    remainingTime--;
    time.textContent = remainingTime;
    if (remainingTime === 0) {
      clearInterval(timer);
      endGame();
    }

  }, 1000);
}





// Avslutt spillet
function endGame() {
  gameEnded = true;
  circle1.style.disabled = "none";
  circle2.style.disabled = "none";
  resetButton.style.display = "block";
}

// Tilbakestill spillet
function resetGame() {
  gameEnded = false;
  startTimer()
  remainingTime = 10;
  clickCount1 = 0;
  clickCount2 = 0;
  
  document.getElementById("score1").textContent = clickCount1;
  document.getElementById("score2").textContent = clickCount2;
  count.textContent = totalClickCount;
  circle1.style.display = "block";
  circle2.style.display = "block";
  resetButton.style.display = "restart-knapp";

  
  
}

// Start spillet
startTimer();



