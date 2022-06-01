// Carousel
let slides = document.querySelectorAll('.slide');

// console.log(slides)
// console.log(slides.length)

var currentSlide = 0

function showSlide(slideNb){
    slides[0].style.display = "none";
    slides[1].style.display = "none";
    slides[2].style.display = "none";
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
        // console.log("correcting : " + currentSlide)
    }
    if (currentSlide < 0){
        currentSlide = slides.length-1
        // console.log("correcting : " + currentSlide)
    }
}