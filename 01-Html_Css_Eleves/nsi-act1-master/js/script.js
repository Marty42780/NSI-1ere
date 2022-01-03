// Menu Div
const menuDiv = document.querySelector('#menuDiv');
const menuButton = document.querySelector('#menuButton');

menuDiv.style.display = "block"; // Securité si le js ne se charge pas

function showMenu() {
    if (menuDiv.classList.contains('showed')) {
        menuDiv.classList.remove('showed');
        menuButton.innerHTML = "Tout voir";
        menuButton.classList.remove('showed');
        
    } else {
        // menuDiv.style.display = "block";
        menuDiv.classList.add('showed');
        menuButton.innerHTML = "Cacher";
        menuButton.classList.add('showed');
    }
}

// Carousel
let slides = document.querySelectorAll('.slide');

console.log(slides)
console.log(slides.length)

var currentSlide = 0

function showSlide(slideNb){
    slides[0].style.display = "none";
    slides[1].style.display = "none";
    slides[slideNb].style.display = "flex";
}
function changeSlideWithButon(nb){
    currentSlide += nb
    correctCurrentSlide()
    showSlide(currentSlide)
}

function correctCurrentSlide(){
    if (currentSlide > slides.length-1){
        currentSlide = 0
        console.log("correcting : " + currentSlide)
    }
    if (currentSlide < 0){
        currentSlide = slides.length-1
        console.log("correcting : " + currentSlide)
    }
}

// Lion
const lion = document.querySelector("#lion");
const sec1 = document.querySelector(".sec1");
sec1.style.display = "none";
function lion_clic(){
    lion.style.display = "none";
    sec1.style.display = "flex";    
}