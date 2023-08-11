window.onload = function () {
  var isLoggedIn = sessionStorage.getItem("isLoggedIn");
  if (isLoggedIn === "true") {
    var loginPage = document.getElementById("login");
    loginPage.style.display = "none";
  }
};

function logout() {
  // Clear the sessionStorage flag
  sessionStorage.removeItem("isLoggedIn");

  // Redirect to the login page
  window.location.reload();
}

document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to the login button
    document.getElementById("login-btn").addEventListener("click", function() {
      // Get input values
      var username = document.getElementById("username").value;
      var password = document.getElementById("password").value;
  
      // Validate login credentials (Replace "your-correct-username" and "your-correct-password" with actual values)
      if (username === "admin" && password === "admin") {
        alert("Login successful!");
        sessionStorage.setItem("isLoggedIn", "true");
        window.location.href = "/dashboard";
        // Redirect to a different page after successful login
      } else {
        alert("Invalid credentials. Please try again.");
      }
    });
  });
  

  function checkEnter(event) {
    if (event.keyCode === 13) {
      login();
    }
  }
  
  function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    // Validate login credentials (Replace "your-correct-username" and "your-correct-password" with actual values)
    if (username === "admin" && password === "admin") {
      alert("Login successful!");
      // Redirect to a different page after successful login
      window.location.href = "/dashboard";
    } else {
      alert("Invalid credentials. Please try again.");
    }
  }