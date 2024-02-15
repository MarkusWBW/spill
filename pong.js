// Finn canvas fra html
const cvs = document.getElementById("pong");
const ctx = cvs.getContext("2d");

// lag brukeren sin rekkert
const user = {
    x : 0,
    y : cvs.height/2 - 100/2,
    width : 10,
    height : 100, 
    color : "BLACK", 
    score : 0
}

// lag maskin sin rekkert
const com = {
    x : cvs.width - 10,
    y : cvs.height/2 - 100/2,
    width : 10,
    height : 100, 
    color : "BLACK", 
    score : 0
}

// Lag ballen 
const ball = {
    x : cvs.width/2,
    y : cvs.height/2,
    radius : 10, 
    speed : 5, 
    velocityX : 5, 
    velocityY : 5, 
    color : "DARKORANGE"
}

// tegn rektangel funksjonen 

function drawRect(x,y,w,h,color){
    ctx.fillStyle = color;
    ctx.fillRect(x,y,w,h);
}

// lag nettet 
const net = {
    x : cvs.width/2 - 1,
    y : 0,
    width : 2, 
    height : 10, 
    color : "BLACK"
}

// tegn nettet
function drawNet(){
    for(let i = 0; i <= cvs.height; i+=15){
        drawRect(net.x, net.y + i, net.width, net.height, net.color);
    }
}
// Tegn sirkel 
function drawCircle(x,y,r,color){
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x,y,r,0,Math.PI*2,false);
    ctx.closePath();
    ctx.fill();
}

// tegn tekst 
function drawText(text,x,y,color){
    ctx.fillStyle = color; 
    ctx.font = "45px fantasy";
    ctx.fillText(text,x,y);
}

// render spillet
function render(){
    // rydd canvas
    drawRect(0, 0, cvs.width, cvs.height, "WHITE");

    // tegn nettet
    drawNet();

    // tegn stillingen 
    drawText(user.score,cvs.width/4,cvs.height/5,"BLACK");
    drawText(com.score,3*cvs.width/4,cvs.height/5,"BLACK");

    // tegn rekkertene for begge lag
    drawRect(user.x, user.y, user.width, user.height, user.color);
    drawRect(com.x, com.y, com.width, com.height, com.color);

    // tegn ballen 
    drawCircle(ball.x, ball.y, ball.radius, ball.color);
}

// kontroller rekerten 

cvs.addEventListener("mousemove",movePaddle);

function movePaddle(evt){
    let rect = cvs.getBoundingClientRect();

    user.y = evt.clientY - rect.top - user.height/2;
}

// kollisjon oppfanger 
function collision(b,p){
    b.top = b.y - b.radius;
    b.bottom = b.y + b.radius;
    b.left = b.x - b.radius; 
    b.right = b.x + b.radius; 

    p.top = p.y;
    p.bottom = p.y + p.height;
    p.left = p.x;
    p.right = p.x + p.width;
    
    return b.right > p.left && b.bottom >p.top && b.left < p.right && b.top < p.bottom;
}

// nullstill ballen 
function resetBall(){
    ball.x = cvs.width/2;
    ball.y = cvs.height/2;

    ball.speed = 5;
    ball.velocityX = -ball.velocityX;
}

// Oppdatering : posisjon, bevegelse, stillingen ...
function update(){ 
    ball.x += ball.velocityX;
    ball.y += ball.velocityY;

    let difficulty = 0.1

    // Endre KI-bevegelsen av rekkerten til datamaskinen avhengig av vanskelighetsgraden
    com.y += (ball.y - (com.y + com.height/2)) * difficulty;

    if(ball.y + ball.radius > cvs.height || ball.y - ball.radius < 0){
        ball.velocityY = -ball.velocityY
    }

    let player = (ball.x < cvs.width/2) ? user : com;

    if(collision(ball,player)){
        // Hvor ballen treffer spilleren
        let collidePoint = ball.y -(player.y + player.height/2);

        // normalisering
        collidePoint = collidePoint/(player.height/2);

        // regn ut vinkelen i radiusen 
        let angleRad = collidePoint * Math.PI/4;

        // X retningen til ballen når den treffer 
        let direction = (ball.x < cvs.width/2) ? 1 : -1;

        // bytt vel X og Y 
        ball.velocityX = direction * ball.speed * Math.cos(angleRad);
        ball.velocityY =             ball.speed * Math.sin(angleRad);

        // hver gang ballen treffer en rekert vil farten øke
        ball.speed += 0.2;
    }

    // oppdater stillingen 
    if(ball.x - ball.radius < 0){
        // maskinen vinner
        com.score++;
        resetBall();
    }else if(ball.x + ball.radius > cvs.width){
        // Spilleren vinner
        user.score++;
        resetBall();
    }
}

// spill funksjon
function game(){
    update();
    render();
}

// loop 
const framePerSecond = 50;
setInterval(game,1000/framePerSecond);