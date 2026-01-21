# Memoria del Proyecto de Documentación

Esta memoria detalla el trabajo realizado para la creación del sitio de documentación técnica con MkDocs, cumpliendo con los requisitos especificados en la tarea.

## 1. Enlaces del Proyecto

*   **Repositorio GitHub**: [https://github.com/Isuth86/documentacion-docker](https://github.com/Isuth86/documentacion-docker)
*   **Sitio Web Publicado (GitHub Pages)**: [https://Isuth86.github.io/documentacion-docker/](https://Isuth86.github.io/documentacion-docker/)

## 2. Estructura y Contenido

El sitio web consta de más de 5 secciones principales, superando el mínimo requerido:

1.  **Inicio** (`index.md`): Portada con presentación del proyecto y resumen.
2.  **Introducción** (`introduccion.md`): Contexto sobre Docker y virtualización.
3.  **Instalación** (`instalacion.md`): Guía paso a paso para desplegar LAMP.
4.  **Práctica WordPress + MariaDB** (`wordpress_mariadb.md`): Página adicional con un caso práctico complejo (Multi-container).
5.  **Uso y Funcionamiento** (`uso.md`): Instrucciones de operación y administración.
6.  **Conclusiones** (`conclusiones.md`): Reflexiones finales sobre el aprendizaje.

## 3. Configuración Técnica (MkDocs)

### Tema y Personalización
Se ha utilizado el tema **Material for MkDocs** configurado en `mkdocs.yml` con las siguientes características:
*   **Idioma**: Español (`es`).
*   **Paleta de colores**:
    *   Modo Claro: Primario Índigo, Acento Azul.
    *   Modo Oscuro: Esquema Slate, Primario Índigo, Acento Azul.
*   **Navegación**: Barra superior con pestañas (`navigation.top`) y menús expandibles.
*   **Buscador**: Habilitado con sugerencias y resaltado (`search.suggest`, `search.highlight`).

### Extensiones Markdown Habilitadas
Para enriquecer el contenido y cumplir con la rúbrica, se han activado las siguientes extensiones:

*   **Admonitions**: Bloques de aviso (Nota, Info, Advertencia) para resaltar información importante.
*   **Pymdownx.details**: Bloques desplegables (collapsible) utilizados para secciones de "Solución de Problemas" o contenido extenso.
*   **Pymdownx.highlight** y **superfences**: Resaltado de sintaxis para bloques de código con botón de copiado.
*   **Pymdownx.tabbed**: Pestañas de contenido.
*   **Attr_list**: Para añadir atributos personalizados a elementos HTML.

## 4. Despliegue y Control de Versiones

*   **GitHub**: Se han realizado commits claros siguiendo la evolución del proyecto.
*   **GitHub Pages**: El despliegue se ha automatizado mediante el comando `mkdocs gh-deploy`, alojando el sitio estático en la rama `gh-pages`.
