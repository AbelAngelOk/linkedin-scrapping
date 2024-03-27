/*
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("ejecutar").addEventListener("click", function(event) {
        event.preventDefault(); // Evita que el formulario se envíe automáticamente

        // Obtiene los valores de correo electrónico y contraseña del formulario
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;

        // Realiza una solicitud POST al servidor Flask con los datos del formulario
        axios.post('/', { email: email, password: password })
            .then(function (response) {
                // Maneja la respuesta del servidor (p. ej., descarga el archivo Excel)
                console.log(response.data);
            })
            .catch(function (error) {
                // Maneja cualquier error que ocurra durante la solicitud
                console.error(error);
            });
    });
}); 
*/