# Biblioteca de Economía (versión simplificada)

Versión reducida de la app original. Se eliminó la constelación de
estrellas, el panel de administrador/autor y el embebido de PDFs.
Ahora la app tiene solo dos secciones, accesibles desde un menú
lateral que se abre desde la izquierda (como en los chats de IA):

- **📚 Biblioteca**: los 64 libros originales, agrupados por
  categoría (Realidad Nacional, Economía Política, Estadística,
  Microeconomía, Macroeconomía), con botón para abrir cada uno en
  Google Drive.
- **🎓 Recursos Didácticos**: la sección que antes era "Catálogo de
  Recursos e Imágenes" (dentro del panel de sugerencias), ahora
  como su propia interfaz. Trae ya cargado el "Logo de economía"
  y queda lista para sumar más guías, plantillas o imágenes con la
  misma estructura que la biblioteca.

Ambas secciones muestran el contenido en **carrusel horizontal
estilo Netflix** (una fila por categoría, con flechas y scroll
lateral), no en grilla — igual que en la app original.

## Archivos

- `app.py` — código de la aplicación.
- `requirements.txt` — dependencias (solo `streamlit`).
- `README.md` — este archivo.

## Cómo correr la app

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Cómo agregar contenido nuevo

Todo el contenido vive en dos listas dentro de `app.py`:

```python
LIBROS = [ ... ]      # sección Biblioteca
RECURSOS = [ ... ]    # sección Recursos Didácticos
```

Para agregar un libro o recurso nuevo, copia una entrada existente
y cambia los valores:

```python
{
    "id": 43,                       # único, no repetir
    "titulo": "Título del libro",
    "autor": "Nombre del autor",
    "drive_id": "ID_DE_GOOGLE_DRIVE",  # de la URL de Drive
    "categoria": "Nombre de la categoría",
},
```

- El `drive_id` es la parte de la URL de Google Drive entre
  `/d/` y `/view` (ejemplo: en
  `https://drive.google.com/file/d/1AbCdEfG.../view`, el id es
  `1AbCdEfG...`).
- Si usas una categoría que no existe todavía, se crea sola y
  aparece como un nuevo bloque en la pantalla.
- Si dejas `"drive_id": ""`, la tarjeta se muestra igual pero con
  botón "Próximamente" en vez de enlace, útil para reservar el
  espacio mientras consigues el archivo.

## Qué se quitó del original

- La constelación de estrellas de Orión (Plotly) como menú de
  navegación.
- El panel de autor/moderación (aprobar o rechazar aportes,
  reordenar categorías a mano, editar libros desde la interfaz).
- El formulario de "Sugerir Aporte" para subir libros nuevos desde
  la app.
- Las portadas locales subidas a mano y el embebido de PDF en base64
  (ahora las portadas salen siempre de la miniatura de Drive y el
  botón lleva directo al archivo en Drive).

Si más adelante quieres recuperar alguna de estas funciones, se
puede reincorporar esa lógica del código original; se dejó fuera a
propósito para simplificar y facilitar subir la app a otra fuente.
