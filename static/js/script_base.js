
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
