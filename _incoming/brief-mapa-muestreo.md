# Brief — mapa interactivo de muestreo del virome humano

Pégale esto entero a Claude (claude.ai) junto con tu tabla de datos. Está escrito
para que lo que salga entre en `components/` sin retoques.

---

## Qué construir

Una página HTML **autónoma en un solo archivo** con un mapa mundial interactivo:
cada país coloreado por el número de estudios (o de muestras) de virome humano
publicados, con tooltip al pasar el ratón y enlace al artículo al hacer clic.

Va a vivir dentro de un libro Quarto, embebida en un capítulo mediante `<iframe>`.

## Contrato técnico — no negociable

1. **Un solo archivo `.html`.** CSS y JS en línea. **Sin CDNs, sin `fetch()`, sin
   dependencias de red en tiempo de ejecución.** Si necesitas la geometría del
   mundo (TopoJSON/GeoJSON o un SVG), va incrustada en el archivo.
2. **Sin `@media (prefers-color-scheme: dark)`.** El libro es light-only a
   propósito.
3. **Tokens de diseño en `:root`, exactamente estos:**
   ```css
   :root{
     --paper:#FFFFFF; --ink:#14213D; --muted:#5C6B82; --line:#E2E6EC; --surface:#FFFFFF;
     --accent:#0891B2; --purple:#6C63C9; --coral:#E85D4E; --star:#D99A1B;
     --sans:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;
     --display:"Space Grotesk",ui-sans-serif,system-ui,sans-serif;
     --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,monospace;
   }
   ```
   Y el `<link>` a Google Fonts para esas tres familias en el `<head>`.
4. **La rampa de color va de `#E0F2F7` a `#0891B2`** (claro → cian). Los países
   sin datos en `#F1F3F6` con borde `#E2E6EC` — el gris significa "cero
   estudios", que es el dato, no un hueco.
5. **Los datos van en un único objeto al principio del `<script>`**, con un
   comentario que diga cómo actualizarlo. Nada de valores repartidos por el
   código.
6. **Tipografía:** títulos en `var(--display)` 500; cuerpo en `var(--sans)`;
   cifras, códigos de país y etiquetas técnicas en `var(--mono)` 500. Los
   kickers en mono 11px, 700, `letter-spacing:1.5px`, mayúsculas.
7. **Bordes redondeados a 8px.** Nada de sombras fuertes.
8. **Accesible:** el color no puede ser el único canal. Tooltip con la cifra
   exacta, y una lista o tabla debajo del mapa con los mismos datos.

## Forma de los datos

```js
// Actualizar aquí. iso3 = código ISO 3166-1 alpha-3.
const DATA = {
  USA: { studies: 42, samples: 3100, refs: [
    { label: "Gregory et al. 2020, Cell Host & Microbe", url: "https://doi.org/..." }
  ]},
  // ...
};
```

## Interacción

- **Hover:** tooltip con país, nº de estudios, nº de muestras.
- **Clic:** despliega la lista de artículos de ese país, con enlaces que abren
  en pestaña nueva.
- **Sin datos:** el tooltip debe decirlo explícitamente — "no published studies"
  —, no quedarse mudo.
- Que funcione con teclado, no solo con ratón.

## Lo que NO debe hacer

- No inventes cifras ni DOIs. Si falta un dato, deja el país sin datos.
- No pongas título ni bajada grandes en la página: el capítulo ya los lleva.
  Un kicker en mono está bien.
- No uses verde `#0F6E56` ni papel cálido `#FBF9F4` — son de una paleta
  retirada del proyecto.
- Nada de mapas 3D, globos giratorios ni animaciones de entrada.

## Proyección

Robinson o Natural Earth. **Mercator no** — exagera Europa y Norteamérica, que
es justo el sesgo que la figura denuncia.

---

## Cuando lo tengas

Guárdalo como `components/sampling-map.html` y dímelo. Yo le añado el script que
reporta su altura al capítulo y lo enlazo con `::: embed`, igual que el heatmap
corporal y la curva de riqueza.
