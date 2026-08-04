# Mapa interactivo de muestreo — texto para pegar en claude.ai

Todo lo que hay debajo de la línea es el prompt. Cópialo entero, pega tu tabla
de datos donde lo pide, y mándalo.

Cuando te devuelva el archivo, guárdalo como `components/sampling-map.html` y
avísame: yo le añado el script que reporta su altura y lo enlazo en el capítulo
con `::: embed`, igual que el heatmap corporal y la curva de riqueza.

---

Necesito que me construyas una página HTML autónoma con un mapa mundial
interactivo. Te doy contexto primero porque cambia bastante el resultado.

**El proyecto.** Estoy escribiendo *Virome City*, una guía ilustrada que lleva a
un investigador desde la idea de una muestra de virome humano hasta el análisis.
La audiencia es mixta: doctorandos y postdocs por un lado, estudiantes que se
asoman al virome por primera vez por el otro. No es un libro sobre viromas — es
una herramienta para hacer análisis de viromas. Esa distinción decide todo lo
demás: la biología se explica solo donde cambia lo que el lector debería hacer.

Es un libro Quarto, **solo modo claro** (a propósito, sin modo oscuro), y va a
existir también **en papel**.

**Dónde va esta figura.** En el capítulo 3, "Where do viruses hide?", en una
sección titulada "Why is so much of it unclassified?". El argumento que la
figura tiene que sostener es este: la mayoría de los estudios publicados de
virome humano vienen de un puñado de regiones, así que las bases de datos de
referencia están construidas con esas muestras; una librería de una población
subrepresentada va a dejar una fracción no clasificada mayor, y eso **no es un
fallo del pipeline** — es una propiedad de la referencia, y saberlo pertenece al
diseño del estudio, no al troubleshooting posterior.

**Qué quiero que haga el mapa.** Que un lector encuentre su propia población,
vea cuánto se ha muestreado, y pueda irse a leer el artículo. Es un recurso, no
una ilustración.

**Cómo se va a mostrar.** Embebida en un `<iframe>` dentro del capítulo. El
capítulo ya le pone un título y una descripción encima, así que la página no
debe repetirlos: nada de títulos grandes ni bajadas. Un kicker pequeño en
monoespaciada está bien.

## Contrato técnico — esto no es negociable

1. **Un solo archivo `.html`**, con el CSS y el JS en línea. **Sin CDNs, sin
   `fetch()`, sin ninguna dependencia de red en tiempo de ejecución.** Si
   necesitas la geometría del mundo (TopoJSON, GeoJSON o un SVG), va incrustada
   en el archivo. La única excepción es el `<link>` de Google Fonts del punto 3.

2. **Sin `@media (prefers-color-scheme: dark)`.** El libro es solo modo claro.

3. **Estos tokens exactos en `:root`**, y el `<link>` a Google Fonts para las
   tres familias:

   ```css
   :root{
     --paper:#FFFFFF; --ink:#14213D; --muted:#5C6B82; --line:#E2E6EC; --surface:#FFFFFF;
     --accent:#0891B2; --purple:#6C63C9; --coral:#E85D4E; --star:#D99A1B;
     --sans:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;
     --display:"Space Grotesk",ui-sans-serif,system-ui,sans-serif;
     --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,monospace;
   }
   ```

4. **Rampa de color de `#E0F2F7` a `#0891B2`** (claro → cian). Los países sin
   datos en `#F1F3F6` con borde `#E2E6EC`. El gris significa "cero estudios
   publicados", que es el dato — no es un hueco.

5. **Proyección Robinson o Natural Earth. Mercator no**, porque infla Europa y
   Norteamérica, que es exactamente el sesgo que la figura denuncia.

6. **Los datos en un único objeto al principio del `<script>`**, con un
   comentario que explique cómo actualizarlo. Nada de valores repartidos por el
   código.

7. **Tipografía:** cuerpo en `var(--sans)`; cifras, códigos de país y etiquetas
   técnicas en `var(--mono)` peso 500; cualquier titulillo en `var(--display)`
   peso 500. Los kickers en mono 11px, peso 700, `letter-spacing:1.5px`,
   mayúsculas. Radio de esquina 8px, sin sombras fuertes.

8. **Accesible.** El color no puede ser el único canal de información: tooltip
   con la cifra exacta, navegable con teclado, y debajo del mapa una tabla con
   los mismos datos ordenada de mayor a menor.

9. **Todo el texto de la interfaz en inglés** — el libro se traducirá y las
   etiquetas técnicas se quedan en inglés en todos los idiomas.

## Interacción

- **Hover:** tooltip con el país, el número de estudios y el número de muestras.
- **Clic:** despliega la lista de artículos de ese país, con enlaces que abren
  en pestaña nueva.
- **Países sin datos:** el tooltip lo dice explícitamente ("no published
  studies"), no se queda mudo.

## Lo que no debe hacer

- **No inventes cifras ni DOIs.** Si un país no está en mi tabla, va sin datos.
  Prefiero un mapa medio vacío a uno con números plausibles pero falsos.
- No uses el verde `#0F6E56` ni el papel cálido `#FBF9F4`: son de una paleta que
  el proyecto retiró.
- Nada de globos 3D, mapas giratorios ni animaciones de entrada.
- No pongas leyenda de "datos estimados" si los datos son reales; y si son
  parciales, dilo con precisión.

## Mis datos

```
[PEGA AQUÍ TU TABLA: país (ISO3), nº de estudios, nº de muestras, y para cada
uno la cita y el DOI o URL. Si todavía no la tienes completa, empieza con los
diez o quince países que sí tengas y déjame el objeto preparado para ampliarlo.]
```

Usa esta forma:

```js
// Actualizar aquí. iso3 = código ISO 3166-1 alpha-3.
const DATA = {
  USA: { studies: 42, samples: 3100, refs: [
    { label: "Gregory et al. 2020, Cell Host & Microbe", url: "https://doi.org/..." }
  ]},
  // ...
};
```

Devuélveme el archivo completo, listo para guardar. Si algo del contrato choca
con lo que necesitas para que funcione, dímelo antes de romperlo.
