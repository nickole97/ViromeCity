# Brief para pedir un borrador de capítulo

Pega esto al principio de la conversación donde generes el HTML de un capítulo.
Existe porque el primer borrador de `what` traía 98 KB de los que se usaron 16:
el resto era CSS que el libro reemplaza, una imagen en base64 que ya existía
como archivo, y una paleta que no era la del libro.

---

## Pégalo tal cual

> Estoy escribiendo un capítulo para un libro ilustrado sobre el viroma humano.
> El resultado va a un proyecto Quarto que tiene su propia hoja de estilos, así
> que **no diseñes la página** — todo el CSS que escribas se descarta.
>
> Dame un HTML simple con:
>
> - **La prosa**, en párrafos y encabezados normales (`<h2>`, `<h3>`, `<p>`).
> - **Las figuras como SVG en línea**, una por concepto, sin agrupar varias en
>   un mismo SVG.
> - **Sin `<style>`**, sin `style="..."` en los elementos, sin fuentes, sin
>   layout, sin modo oscuro.
> - **Sin imágenes en base64.** Si hace falta una foto o un PNG, deja un
>   `<img src="nombre-descriptivo.png">` y mándamelo aparte.
>
> Para los colores **dentro de los SVG**, usa solo estos cinco pares. Cada color
> tiene su tinta emparejada; usa siempre la pareja, nunca negro sobre amarillo
> ni sobre rosa:
>
> | Significado | Relleno | Tinta encima |
> |---|---|---|
> | decisión, bifurcación | `#4263EB` | `#FFFFFF` |
> | proceso, un paso del protocolo | `#F5D33D` | `#3D3208` |
> | rama, clasificación | `#F9C6DA` | `#7A2848` |
> | contexto, apunte al margen | `#D3D5F7` | `#2E3175` |
> | resultado, lo que obtienes | `#F2A65A` | `#5A3410` |
>
> Grises: texto `#17181C`, secundario `#63656E`, líneas `#E4E5EA`.
> **No uses verde.** Estaba en una paleta anterior y se retiró.
>
> Las etiquetas dentro de las figuras van **en inglés** siempre (`capsid`,
> `dsDNA`, `prophage`), aunque el texto esté en otro idioma: es el vocabulario
> que el lector encuentra en los papers.

---

## Qué pasa después

Yo convierto ese HTML a `sections/<capítulo>.qmd`, saco cada SVG a
`assets/img/<capítulo>/` con nombre descriptivo, y aplico las clases del libro
(`.wide`, `.fivi`, `.beat`, `.parts`). Ver [LEEME.md](LEEME.md).

## Para maquetas visuales es distinto

Si lo que quieres es **explorar diseño** — probar un fondo, un tipo de tarjeta,
una disposición — entonces sí pide HTML completo con su CSS. Una maqueta que se
ve en el navegador vale más que describirla. Pero mándala como maqueta, no como
capítulo: se mira, se decide, y lo que se aprueba lo llevo yo a
`assets/styles.scss`, que es la única hoja del libro.
