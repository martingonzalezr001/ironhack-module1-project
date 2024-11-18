# Proyecto: Encuentra la estación de BiciMAD más cercana a un centro deportivo

Este proyecto busca la estación de BiciMAD más cercana a uno o varios centros deportivos en Madrid. Los datos utilizados para identificar los centros deportivos provienen del catálogo oficial de datos abiertos del Ayuntamiento de Madrid. Puedes acceder a la fuente de los datos desde este enlace:  
[/catalogo/212808-0-espacio-deporte.json](/catalogo/212808-0-espacio-deporte.json).

---

## ESTRUCTURA DE FICHEROS

<!-- Completa esta sección con la estructura específica de tu proyecto -->

---

## COSAS A MEJORAR

- **Mayor parametrización de funciones**: Hacer que las funciones sean más genéricas para soportar distintos tipos de consultas.
- **Interfaz de usuario**: Incluir una interfaz gráfica o un sistema interactivo en la línea de comandos para facilitar su uso.
- **Documentación**: Ampliar la documentación técnica para desarrolladores y usuarios.

---

## MANUAL DE USO

### 1. Introducción
El programa permite realizar dos tipos de búsqueda:
1. Encontrar la estación de BiciMAD más cercana a **todos** los centros deportivos disponibles.
2. Encontrar la estación de BiciMAD más cercana a un centro deportivo **específico**, elegido por el usuario.

### 2. Ejecución
1. Asegúrate de haber instalado todas las librerías necesarias (ver sección "Instalación de Librerías Necesarias").
2. Ejecuta el script principal del proyecto.
3. Selecciona el tipo de búsqueda que deseas realizar:
   - Si eliges la búsqueda global, el programa calculará las distancias para todos los centros deportivos.
   - Si eliges un centro deportivo específico, el programa te permitirá seleccionarlo de una lista.
4. Obtendrás como resultado la estación de BiciMAD más cercana, junto con información adicional sobre la distancia.

### 3. Ejemplo de Uso
1. El programa se ejecuta por consola, hay dos opciones, o introducir la palabra Todos, o introducir el centro especifico
2. Si elegiste buscar un centro específico, el programa te mostrará una lista de nombres de centros deportivos disponibles. Introduce el nombre o número correspondiente al centro deseado.
3. Recibe como salida la estación más cercana con la distancia en metros.

---

## INSTALACIÓN DE LIBRERÍAS NECESARIAS

Antes de ejecutar el proyecto, asegúrate de instalar las siguientes librerías de Python:
```bash
pip install pandas geopandas shapely requests
