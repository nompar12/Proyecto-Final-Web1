  // Función para mostrar u ocultar el botón según la posición del usuario en la página
  window.onscroll = function() {
    mostrarBotonVolverArriba();
  };

  function mostrarBotonVolverArriba() {
    var boton = document.getElementById("volverArriba");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      boton.style.display = "block";
    } else {
      boton.style.display = "none";
    }
  }

  // Función para desplazar la página hacia arriba
  function scrollToTop() {
    document.documentElement.scrollTop = 0; // Para navegadores Chrome, Firefox, IE y Opera
    document.body.scrollTop = 0; // Para navegadores Safari
  }