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

 
  function scrollToTop() {
    document.documentElement.scrollTop = 0; 
    document.body.scrollTop = 0; 
  }
  function reproducirSonido() {
    document.getElementById('audio').play();
}