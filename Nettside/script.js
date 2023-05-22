

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


var eefe = true;

function signin() {
  const signinHeaderEl = document.querySelector(".LoginHeader");
  const parentElement = document.querySelector(".lgsignin");
  const signInEl = document.getElementById("signin");

  const removeInput = document.getElementById("epostinput");
  const removeSelect = document.getElementById("select");

  const removeLabel = document.getElementById("epostlable");
  const removeButton = document.getElementById("Forgotpasswd");

  const removeBreak = document.getElementById("brbrake");
  const removeBreak1 = document.getElementById("brbrake1");
  const removeBreak2 = document.getElementById("brbrake2");

  signinHeaderEl.innerHTML = "Sign in";
  signInEl.innerHTML = "Sign in";

  if (!removeInput) {
    const addInput = document.createElement("input");
    addInput.setAttribute("type", "text");
    addInput.setAttribute("id", "epostinput");
    addInput.setAttribute("name", "fname");

    const addLabel = document.createElement("label");
    addLabel.setAttribute("id", "epostlable");
    addLabel.textContent = "E-post";

    const addSelect = document.createElement("select");
    addSelect.id = "select";
    const option1 = document.createElement("option");
    option1.value = "option1";
    option1.text = "Gutt";
    const option2 = document.createElement("option");
    option2.value = "option2";
    option2.text = "Jente";
    const option3 = document.createElement("option");
    option3.value = "option3";
    option3.text = "Annet";

    const addButton = document.createElement("button");
    addButton.textContent = "Forgot Password";
    addButton.setAttribute("id", "Forgotpasswd");

    const lineBreak = document.createElement("br");
    lineBreak.setAttribute("id", "brbrake");
    const lineBreak1 = document.createElement("br");
    lineBreak1.setAttribute("id", "brbrake1");
    const lineBreak2 = document.createElement("br");
    lineBreak2.setAttribute("id", "brbrake2");

    addSelect.appendChild(option1);
    addSelect.appendChild(option2);
    addSelect.appendChild(option3);

    parentElement.appendChild(addLabel);
    parentElement.appendChild(lineBreak);
    parentElement.appendChild(addInput);
    parentElement.appendChild(lineBreak1);
    parentElement.appendChild(lineBreak2);
    parentElement.appendChild(addSelect);
    parentElement.appendChild(addButton);

    console.log("added");
  } else {
    signinHeaderEl.innerHTML = "Log in";
    signInEl.innerHTML = "Log in";
    removeInput.remove();
    removeLabel.remove();
    removeSelect.remove();
    removeButton.remove();
    removeBreak.remove();
    removeBreak1.remove();
    removeBreak2.remove();
    
    console.log("removed");
  }
}


function gender(){
  var gender = document.getElementById("gender").value
  if (gender = Annet) {
  }
}


