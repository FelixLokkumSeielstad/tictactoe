

const navSlide = () => { 
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
  
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        })
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

setchanges = true

function haveaq() {
  changelopage = document.getElementById("changelopage")

  if (setchanges == true) {
    changelopage.remove() 
  } else {
    button  = document.createElement(button)
    button.setAttribute("id", "myButton");
    button.setAttribute("class", "btn");
    button.setAttribute("onclick", "myFunction()");
  }
}

function reviewcount() {
  var wordcounter = document.getElementById("reviewinput");
  var wordvalue = wordcounter.value;

  var reviewcount = wordvalue.length;

  document.getElementById("wordCount").innerHTML = reviewcount + "/100";
}

wdjfe = true  

function changeloginsite() {
  const username = document.getElementById("username")
  const password = document.getElementById("password")
  const epostlable = document.getElementById("epostlable")
  const epostinput = document.getElementById("epostinput")
  const placesment = document.getElementById("epostplacemen")
  const linjebytt = document.getElementById("linjebytt")

  if (wdjfe === true) {
    const epostlable = document.createElement("label")
    epostlable.setAttribute('for', 'username')
    epostlable.setAttribute('type', 'email')
    epostlable.setAttribute('id', 'epostlable')
    epostlable.innerText = "Epost";
    const epostinput = document.createElement("input");
    epostinput.setAttribute('id', 'epostinput')
    epostinput.setAttribute('name', 'makeepost');

    username.setAttribute('name', 'makeusername')
    password.setAttribute('name', 'makepassword')

    const linjebytt = document.createElement("br")
    linjebytt.setAttribute('id', 'linjebytt')

    placesment.appendChild(epostlable);
    placesment.appendChild(linjebytt);
    placesment.appendChild(epostinput);

    wdjfe = false
    console.log(wdjfe)
  }else {

    username.setAttribute('name', 'username')
    password.setAttribute('name', 'password')

    epostlable.remove();
    linjebytt.remove();
    epostinput.remove();

    wdjfe = true
    console.log(wdjfe)
  }
}