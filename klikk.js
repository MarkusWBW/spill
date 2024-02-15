// Velg HTML-elementer
const clickButton = document.getElementById("klikk-knapp");
const time = document.getElementById("tid");
const count = document.getElementById("tall");
const resetButton = document.getElementById("restart-knapp");
const counter = document.getElementById("teller");

// Sett variabler
let remainingTime = 10;
let clickCount = 0;
let timer;
let gameEnded = false; 

// Les antall klikk fra localStorage hvis det finnes
if(!localStorage.getItem("clickCount")){
  clickCount = localStorage.getItem("clickCount");
  count.textContent = clickCount;
  counter.textContent = "Du har klikket " + clickCount + " ganger!";
}

// Lytt etter klikk på knappen
clickButton.addEventListener("click", () => {
  if (!gameEnded) {
    clickCount++;
    count.textContent = clickCount;
    counter.textContent = "Du har klikket " + clickCount + " ganger";
    localStorage.setItem("clickCount", clickCount);
  }
});

// Lytt etter klikk på reset-knappen
resetButton.addEventListener("click", () => {
  resetGame();
});

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
  clickButton.style.disabled = "none";
  resetButton.style.display = "block";
  counter.textContent = "Du klarte å klikke " + clickCount + " ganger!";
}

// Tilbakestill spillet
function resetGame() {
  gameEnded = false;
  remainingTime = 10;
  clickCount = 0;
  time.textContent = remainingTime;
  count.textContent = clickCount;
  clickButton.style.display = "block";
  resetButton.style.display = "none";
  counter.textContent = "Du har klikket " + clickCount + " ganger";
  localStorage.removeItem("clickCount");
  startTimer();
}

// Start spillet
startTimer();
