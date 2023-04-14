
const tl = gsap.timeline({defaults: {ease: "power1.out"}});

tl.to(".text", {y: "0%", duration: 1, stagger: 0.5 });
tl.to(".intro", {y: "-100%", duration: 1});





///////////////////////nav////////////////////

const navSlide = () => { 
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
  
    burger.addEventListener('click', () => {
        //Toggle Lav
        nav.classList.toggle('nav-active');
        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        })
        //Burger Animation
        burger.classList.toggle('toggle');
    })
  }
  
  navSlide(); 
  
  


  // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
  window.onscroll = function() {scrollFunction()};
  
  function scrollFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {;
      document.querySelector("nav").style.backgroundColor = "rgba(10, 10, 10, .9)";
    } else {
      document.querySelector("nav").style.backgroundColor = "transparent";
    }
  }