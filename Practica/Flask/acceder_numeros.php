
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <title>Lista de Números</title>
</head>
<body>


<?php
// URL del servidor Flask
$url = "http://localhost:5000/numeros";

// Inicializar cURL
$ch = curl_init();

// Configurar cURL para hacer una solicitud GET a la URL del servidor Flask
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);  // Para obtener el resultado como una cadena

// Ejecutar la solicitud
$response = curl_exec($ch);

// Verificar si ocurrió algún error
if ($response === false) {
    echo "Error en la solicitud: " . curl_error($ch);
} else {
    // Decodificar el JSON recibido en un array de PHP
    $numeros = json_decode($response, true);
    
    // Mostrar la lista de números en una tabla de Bootstrap
    echo '<div class="container mt-5">';
    echo '<h2>Lista de Números Obtenida desde Flask</h2>';
    echo '<table class="table table-bordered">';
    echo '<thead>';
    echo '<tr>';
    echo '<th>Número</th>';  // Encabezado de la columna
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';

    foreach ($numeros as $numero) {
        echo '<tr>';
        echo '<td>' . $numero . '</td>';  // Mostrar cada número en una fila
        echo '</tr>';
    }

    echo '</tbody>';
    echo '</table>';
    echo '</div>';
}

// Cerrar la conexión cURL
curl_close($ch);
?>

