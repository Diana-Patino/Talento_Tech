$(document).ready(function(){
    $('.carousel').slick({
        autoplay: true,
        autoplaySpeed: 1000,
        dots: true,
        arrows: true // Ocultar los botones de navegación
    });

    // Añadir efecto de desplazamiento suave
    $('a').on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function(){
                window.location.hash = hash;
            });
        }   
    });
});
