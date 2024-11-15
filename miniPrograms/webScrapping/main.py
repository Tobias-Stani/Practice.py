import requests
from bs4 import BeautifulSoup
import json

# URL de la página a scrapear
url = "https://www.afa.com.ar/es/posts/clubes-afiliados-2024"

# Realizar la solicitud HTTP para obtener el HTML de la página
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Array para almacenar los nombres de los clubes
    clubes = []

    # Buscar todos los <span> con el estilo específico
    spans = soup.find_all('span', style='font-size:13.5pt')

    # Recorrer todos los <span> encontrados y extraer el texto
    for span in spans:
        span_text = span.get_text(strip=True)
        
        # Verificar que el texto no esté vacío
        if span_text:
            clubes.append(span_text)

    # Convertir la lista de clubes a formato JSON con codificación UTF-8
    json_output = json.dumps(clubes, ensure_ascii=False, indent=4)

    # Imprimir el JSON en consola o devolverlo en algún endpoint
    print(json_output)

    # Si quieres guardar el JSON en un archivo con codificación UTF-8
    with open('clubes_utf8.json', 'w', encoding='utf-8') as f:
        f.write(json_output)

else:
    print(f"Error: {response.status_code}")
