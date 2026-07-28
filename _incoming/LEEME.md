# _incoming — bandeja de entrada de borradores

Aquí van los borradores nuevos de capítulos: HTML descargado, imágenes,
SVG, lo que sea. **Nada de esto se publica.** Es material en tránsito,
esperando a convertirse en `.qmd`.

Está en `.gitignore`, así que no ensucia `git status` ni entra al repo.

## Cómo nombrar

`<capitulo>-v<N>.html` — `where-v3.html`, `why-v1.html`. La versión importa:
si dejas dos versiones del mismo capítulo, la de número más alto gana.

Los assets que acompañen al borrador, en una subcarpeta con el mismo nombre:
`where-v3/heatmap.svg`.

## Qué pasa después

El borrador se convierte a `sections/<capitulo>.qmd`, sus imágenes van a
`assets/img/`, y los widgets interactivos pesados van a `components/` como
HTML propio (no se incrustan en el capítulo). El borrador viejo se guarda en
`_archive/sections-html/` y el de aquí se borra.

Regla que originó esta carpeta: **nada se descarga a la raíz del repo.**
