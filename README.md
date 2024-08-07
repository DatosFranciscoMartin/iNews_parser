# iNews_parser

## Introducción

El iNews Parser es un script de Python que lee datos de un archivo CSV y genera archivos XML para cada fila del CSV. Esto es particularmente útil para convertir datos estructurados en un formato XML estandarizado para sistemas de gestión de noticias.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Dependencias](#dependencias)
- [Configuración](#configuración)
- [Documentación](#documentación)
- [Ejemplos](#ejemplos)
- [Solución de Problemas](#solución-de-problemas)
- [Colaboradores](#colaboradores)
- [Licencia](#licencia)

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <repository_url>
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd iNews_parser
    ```
3. Asegúrate de tener Python 3 instalado.

## Uso

1. Coloca el archivo CSV que deseas analizar en el directorio apropiado (por ejemplo, `Documents/iNews_parser/`).
2. Actualiza la variable `csv_file_path` en el script con la ruta de tu archivo CSV al igual que la variable `output_file_path` para el fichero XML de salida.
3. Ejecuta el script:
    ```sh
    python iNews_parser.py
    ```
4. El script generará un archivo XML por cada fila en el CSV y lo guardará en el mismo directorio.

## Características

- Lee datos de un archivo CSV.
- Genera archivos XML con una estructura predefinida para cada fila del CSV.
- Incluye comentarios y sugerencias para desarrolladores dentro de los archivos XML generados.

## Dependencias

- `csv` (biblioteca estándar)
- `xml.etree.ElementTree` (biblioteca estándar)
- `xml.dom.minidom` (biblioteca estándar)
- `os` (biblioteca estándar)
- `codecs` (biblioteca estándar)

## Configuración

- Actualiza la variable `csv_file_path` para que apunte a tu archivo CSV.
- Actualiza la variable `output_file_path` para que guarde tu fichero XML.

## Documentación

El script lee un archivo CSV donde cada fila representa un elemento de noticia. Luego, crea un archivo XML con una estructura específica para cada elemento de noticia.

### Ejemplo de Estructura de CSV

El CSV debe tener las siguientes columnas:

- `Noticia`
- `Presentador`
- `Ubicación`
- `camara`
- `Texto`
- ...

## Ejemplos

Una fila de ejemplo del CSV y su archivo XML correspondiente:

**CSV:**
```csv
Noticia;Presentador;Ubicación;camara;Texto
1;Fran;Sevilla;camara 1;Las temperaturas máximas...
```