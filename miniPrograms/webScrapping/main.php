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

$clubes = [];

$spans = $dom->getElementsByTagName('span');

$id = 1;

foreach ($spans as $span) {
    $style = $span->getAttribute('style');

    if (strpos($style, 'font-size:13.5pt') !== false) {
        $span_text = trim($span->nodeValue);

        if (strlen($span_text) > 0) {
            $clubes[] = [
                'id' => $id,            
                'nombre' => $span_text  
            ];
            $id++;
        }
    }
}

header('Content-Type: application/json; charset=UTF-8');

echo json_encode($clubes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
