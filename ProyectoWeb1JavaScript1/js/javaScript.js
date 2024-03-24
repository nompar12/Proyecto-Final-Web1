function toggleForm(formType) {
    if (formType === 'login') {
      document.getElementById('login-form').style.display = 'block';
      document.getElementById('register-form').style.display = 'none';
    } else {
      document.getElementById('login-form').style.display = 'none';
      document.getElementById('register-form').style.display = 'block';
    }
  }

  function loginUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "usuario" && password === "contraseña") {
      document.getElementById("loginMessage").textContent = "¡Inicio de sesión exitoso!";
      document.getElementById("loginMessage").classList.remove("hidden");
      
      
      window.location.href = "PG.html";
      
      return false; 
    } else {
      document.getElementById("loginMessage").textContent = "Nombre de usuario o contraseña incorrectos.";
      document.getElementById("loginMessage").classList.remove("hidden");
      return false; 
    }
  }

  let currentImageIndex = 0;
  const images = document.querySelectorAll('.image');
  const totalImages = images.length;

  function showImage(index) {
    if (index < 0) {
      index = totalImages - 1;
    } else if (index >= totalImages) {
      index = 0;
    }

    images.forEach(image => {
      image.style.display = 'none';
    });

    images[index].style.display = 'block';
    currentImageIndex = index;
  }

  function changeImage(direction) {
    currentImageIndex += direction;
    showImage(currentImageIndex);
  }
  document.addEventListener("DOMContentLoaded", function() {
    showImage(0);
  });
