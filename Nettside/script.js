
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




  var bannerstatus = 1;
var bannertimer = 4000;

var timeplan = 1

window.onunload = function(){
    bannerloop();
}

var startbannerloop = setInterval(function(){
    bannerloop();
}, bannertimer);

document.getElementById("main-banner").onmouseenter = function(){
    clearInterval(startbannerloop);
}

document.getElementById("main-banner").onmouseleave = function(){
    startbannerloop = setInterval(function(){
        bannerloop1();
    }, bannertimer);    
}


function bannerloop1() {
    if (bannerstatus === 1){
        document.getElementById("imgban2").style.opacity = "0";
        setTimeout(function(){
            document.getElementById("imgban1").style.right = "0px";
            document.getElementById("imgban1").style.zIndex = "10";
            document.getElementById("imgban2").style.right = "-1200px";
            document.getElementById("imgban2").style.zIndex = "15";
            document.getElementById("imgban3").style.right = "1200px";
            document.getElementById("imgban3").style.zIndex = "5";
        }, 500);
        setTimeout(function(){
            document.getElementById("imgban2").style.opacity = "1";
        }, 1000);
        bannerstatus = 2;
    }
    else if (bannerstatus === 2){
        document.getElementById("imgban3").style.opacity = "0";
        setTimeout(function(){
            document.getElementById("imgban2").style.right = "0px";
            document.getElementById("imgban2").style.zIndex = "10";
            document.getElementById("imgban3").style.right = "-1200px";
            document.getElementById("imgban3").style.zIndex = "15";
            document.getElementById("imgban1").style.right = "1200px";
            document.getElementById("imgban1").style.zIndex = "5";
        }, 50);
        setTimeout(function(){
            document.getElementById("imgban3").style.opacity = "1";
        }, 1000);
        bannerstatus = 3;
    }
    else if (bannerstatus === 3){
        document.getElementById("imgban1").style.opacity = "0";
        setTimeout(function(){
            document.getElementById("imgban3").style.right = "0px";
            document.getElementById("imgban3").style.zIndex = "10";
            document.getElementById("imgban1").style.right = "-1200px";
            document.getElementById("imgban1").style.zIndex = "15";
            document.getElementById("imgban2").style.right = "1200px";
            document.getElementById("imgban2").style.zIndex = "5";
        }, 500);
        setTimeout(function(){
            document.getElementById("imgban1").style.opacity = "1";
        }, 1000);
        bannerstatus = 1;
    }
}



let toggle = document.getElementById("mode");

toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
})





