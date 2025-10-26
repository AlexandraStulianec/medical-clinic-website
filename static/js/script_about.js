document.addEventListener('DOMContentLoaded', function() {
	var aboutImages = document.querySelectorAll('.about-image-left, .about-image-right');

  function revealImages() {
    for (var i = 0; i < aboutImages.length; i++) {
      var position = aboutImages[i].getBoundingClientRect().top;
      var windowHeight = window.innerHeight;

      if (position < windowHeight - 100) {
        aboutImages[i].classList.add('about-visible');
      }
    }
  }

  window.addEventListener('scroll', revealImages);
  revealImages();
});


document.addEventListener('DOMContentLoaded', function() {
    var teamMembers = document.querySelectorAll('.team-member');

  function revealTeamMembers() {
    for (var i = 0; i < teamMembers.length; i++) {
      var position = teamMembers[i].getBoundingClientRect().top;
      var windowHeight = window.innerHeight;

      if (position < windowHeight - 100) {
        teamMembers[i].classList.add('team-visible');
      }
    }
  }

  window.addEventListener('scroll', revealTeamMembers);
  revealTeamMembers();
});

	function reloadPage() {
  location.reload();
  window.scrollTo(0, 0);
}

document.addEventListener('keydown', function(event) {
	    // Check if the "enter" key is pressed (key code 84)
	    if (event.keyCode === 13) {
	      reloadPage();
	    }
	  });
	  

function openLoginPopup() {
	  document.getElementById("loginPopup").style.display = "block";
	}

function closeLoginPopup() {
	 document.getElementById("loginPopup").style.display = "none";
	}
	
function openSignupPopup() {
	  document.getElementById("signupPopup").style.display = "block";
	}

function closeSignupPopup() {
	 document.getElementById("signupPopup").style.display = "none";
	}


function toggleForms() {
  var loginPopup = document.getElementById("loginPopup");
  var signupPopup = document.getElementById("signupPopup");

  loginPopup.classList.toggle("hidden");
  signupPopup.classList.toggle("hidden");
  
  if(document.getElementById("signupPopup").style.display == "block") {
		openLoginPopup();
		closeSignupPopup();
  }
  else {
		openSignupPopup();
		closeLoginPopup();
  }
}

let hash = window.location.hash;
console.log(hash);
if(hash == "#login")
	openLoginPopup();
if(hash == "#signUp")
	openSignupPopup();