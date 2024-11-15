<?php
// URL de la página a scrapear
$url = "https://www.afa.com.ar/es/posts/clubes-afiliados-2024";

// Obtener el contenido HTML de la página
$html = file_get_contents($url);

// Crear un objeto DOMDocument
$dom = new DOMDocument();

// Evitar errores de HTML mal formado (por ejemplo, etiquetas no cerradas)
libxml_use_internal_errors(true);

// Cargar el HTML en el DOMDocument
$dom->loadHTML($html);

// Limpiar los errores después de cargar el HTML
libxml_clear_errors();

// Array para almacenar los nombres de los clubes
$clubes = [];

// Buscar todos los <span> con un estilo específico (font-size: 13.5pt)
$spans = $dom->getElementsByTagName('span');

// Recorrer todos los <span> y extraer los nombres de los clubes
foreach ($spans as $span) {
    // Obtener el atributo de estilo del <span>
    $style = $span->getAttribute('style');

    // Verificar si el atributo style contiene "font-size: 13.5pt"
    if (strpos($style, 'font-size:13.5pt') !== false) {
        // Obtener el contenido de cada <span> y eliminar espacios en blanco innecesarios
        $span_text = trim($span->nodeValue);

        // Verificamos que el texto no sea vacío
        if (strlen($span_text) > 0) {
            // Agregar el nombre del club al array
            $clubes[] = $span_text;
        }
    }
}

// Establecer el encabezado de la respuesta para indicar que es JSON
header('Content-Type: application/json; charset=UTF-8');

// Devolver la respuesta JSON en UTF-8 y evitar la conversión de caracteres especiales
echo json_encode($clubes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
