function enviarWhatsapp(event) {
    event.preventDefault();

    const nombreCliente = document.getElementById('nombre_cliente').value;
    const telefonoCliente = document.getElementById('telefono_cliente').value;
    const servicio = document.getElementById('servicio').options[document.getElementById('servicio').selectedIndex].text;
    const fecha = document.getElementById('fecha').value;
    const hora = document.getElementById('hora').value;

    const mensaje = `Hola, me gustaría reservar el servicio ${servicio} para el día ${fecha} a las ${hora}. Mi nombre es: ${nombreCliente}, espero su confirmación`;
    const url = `https://api.whatsapp.com/send?phone=56998624527&text=${encodeURIComponent(mensaje)}`;

    window.open(url, '_blank');
}