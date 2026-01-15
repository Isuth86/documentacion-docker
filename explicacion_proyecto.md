# Explicación del Proyecto de Documentación

Este documento detalla los componentes, configuración y extensiones utilizadas en la creación de este sitio de documentación con MkDocs.

## Estructura del Proyecto

El proyecto sigue la estructura estándar de MkDocs:

*   **mkdocs.yml**: Archivo de configuración global. Define el tema, navegación y extensiones.
*   **docs/**: Directorio que contiene los archivos fuente en Markdown.
    *   `index.md`: Página de inicio.
    *   `introduccion.md`, `instalacion.md`, `uso.md`, `conclusiones.md`: Páginas de contenido.
    *   `assets/`: Directorio para imágenes y recursos estáticos.

## Configuración y Tema

Se ha utilizado el tema **Material for MkDocs** (`material`) por su diseño moderno y responsivo.
*   **Idioma**: Configurado en español (`es`).
*   **Paleta de Colores**: Color primario índigo con acentos azules. Incluye selector de modo claro/oscuro.

## Extensiones Markdown Implementadas

Se han habilitado varias extensiones en `mkdocs.yml` para enriquecer el contenido:

1.  **Admonitions (Advertencias)**:
    Permiten crear bloques de "Nota", "Advertencia", "Info", etc. Utilizadas en `index.md` y `uso.md`.
    Ejemplo: `!!! info "Nota"`

2.  **pymdownx.details (Bloques desplegables)**:
    Permite ocultar/mostrar contenido complejo. Utilizado en la sección de "Solución de Problemas" en `uso.md`.
    Ejemplo: `??? info "Título"`

3.  **pymdownx.highlight y superfences**:
    Mejora el resaltado de sintaxis para bloques de código. Permite copiar el código con un clic.

4.  **pymdownx.tabbed**:
    Permite crear pestañas de contenido (aunque no se ha abusado de su uso, está habilitado para futuras expansiones).

## Despliegue

El sitio está preparado para ser desplegado en **GitHub Pages**.
El comando `mkdocs gh-deploy` compila el sitio y lo sube a la rama `gh-pages` automáticamente.
