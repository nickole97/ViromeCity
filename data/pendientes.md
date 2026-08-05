# pendientes.md — primera pasada de literatura (viroma humano)

**Fecha:** 4 de agosto de 2026
**Autor de la pasada:** Claude (Cowork). Entrada no confiada — todo se añadió con `verified: no` y `title` vacío. Nada de esto aparece en el mapa publicado hasta que una persona resuelva el DOI y confirme el país de las muestras.

---

## 1. Qué se añadió

**11 filas nuevas**, todas al final de `data/studies.csv`, sin tocar ni reformatear las 17 existentes (comprobado: las primeras 18 líneas son idénticas byte a byte; el diff de git solo muestra las adiciones).

Prioricé países ausentes del listado actual. **10 países nuevos** entran al archivo (PE ya estaba, pero como parte de un estudio multipaís distinto):

| id | país(es) | sitio | año | por qué vale |
|---|---|---|---|---|
| india_gut2022 | IN | gut | 2022 | India ausente; viroma DNA intestinal de población del norte de India |
| cameroon2019 | CM | gut | 2019 | Camerún ausente; 221 muestras fecales, metagenómica viral |
| bangladesh2020 | BD | gut | 2020 | Bangladés ausente; viroma en heces de lactantes |
| iran_blood2023 | IR | blood | 2023 | Irán ausente **y** sitio sangre poco representado |
| vietnam2025 | VN | gut | 2025 | Vietnam ausente; fageoma/viroma intestinal |
| latam_diarrhea2016 | PE;NI;CL | gut | 2016 | Nicaragua y Chile ausentes (Sudamérica/Centroamérica) |
| spain_oral2018 | ES | oral | 2018 | **sitio oral ausente** hasta ahora (ES ya estaba, pero en sangre) |
| southafrica_resp2022 | ZA | respiratory | 2022 | **sitio respiratorio ausente** hasta ahora (ZA ya estaba, pero en intestino) |
| kuwait2020 | KW | gut | 2020 | Kuwait ausente (golfo Pérsico) |
| kenya_infants2026 | KE | gut | 2026 | Kenia ausente (África subsahariana) |
| qatar2022 | QA | gut | 2022 | Catar ausente (golfo Pérsico) |

Cobertura nueva por región: sur de Asia (IN, BD), Sudeste Asiático (VN), África subsahariana (CM, KE), Oriente Medio/Golfo (IR, KW, QA), Sudamérica/Centroamérica (NI, CL). Además se cubren dos sitios corporales que faltaban por completo: **oral** y **respiratorio**.

Cada DOI se comprobó contra una fuente autoritativa (página de la revista, PMC, o la API de CrossRef) antes de añadir la fila; no hay DOIs inventados. El país de cada fila es el del **origen de las muestras**, tomado del texto del artículo, no de la afiliación de los autores.

---

## 2. Qué encontré y descarté (y por qué)

**Descartados por no poder determinar el país de las muestras (regla 2):**

- **Foulongne et al. 2012, viroma DNA de piel** (`10.1371/journal.pone.0038499`). Sería valioso: es el único candidato para el sitio **piel**, que sigue ausente del archivo. Pero la abstract solo dice que se analizaron "cinco individuos sanos y un paciente con carcinoma de células de Merkel", sin indicar de dónde salieron las muestras. Los autores están en Montpellier (Francia), pero eso es dónde trabajan, no necesariamente de dónde son las muestras. No lo adiviné. **Necesita ojo humano:** si al leer el texto completo se confirma que los sujetos eran franceses, añádelo como `FR` y cubre el sitio piel.

**Descartados por ser detección dirigida y no caracterización de comunidad viral (regla "qué no cuenta"):**

- **Gabón y República del Congo, lactantes** (`10.1371/journal.pone.0185569`). Habría aportado dos países nuevos (GA, CG), pero los virus se detectaron solo con PCR múltiplex en tiempo real de 7 virus entéricos concretos; solo las bacterias se secuenciaron por metagenómica. No hay caracterización de la comunidad viral.
- **Burkina Faso, niños con diarrea, Uagadugú** (`10.1371/journal.pone.0153652`). "Prevalence and Genetic Diversity of Enteric Viruses": detección/genotipado dirigido por PCR de virus entéricos conocidos, no metagenómica de comunidad.

**Descartados por prioridad (válidos, pero de países/sitios ya cubiertos; disponibles si se quiere reforzar):**

- **Piel, EE. UU.** — Hannigan et al. 2015, mBio (`10.1128/mbio.01578-15`). País (US) claro, y cubriría el sitio piel, pero US está muy sobrerrepresentado; no lo añadí por la prioridad de países que pediste. Es el candidato de respaldo si se decide cubrir piel sin esperar a resolver el de Foulongne.
- **Sudáfrica, Free State, viroma entérico longitudinal pediátrico** 2024 (ScienceDirect `S0168170224000960`). Estudio primario válido, pero ZA ya está.
- **Etiopía, viroma entérico, ensayo de agua limpia** (`10.1371/journal.pone.0202054`). Primario válido, pero ET ya está.

**Descartados por categoría (regla "qué no cuenta"):**

- Catálogos y bases agregadas que aparecieron repetidamente en las búsquedas (Gut Virus Database, GPD, MGV, CHVD, el Chinese Gut Virus Catalogue, el "early-life gut virome catalog") — excluidos como ya contemplados aparte.
- Revisiones y comentarios.

---

## 3. Dudas que necesitan ojo humano

1. **latam_diarrhea2016 (PE;NI;CL).** El grueso son 58 niños peruanos con diarrea; Nicaragua y Chile aparecen como muestras adicionales de validación. Lo marqué en los tres países. Conviene confirmar si las muestras de NI y CL bastan para contar como esos países en el mapa, o si debería quedar solo como PE.
2. **iran_blood2023 (IR, sangre).** La cohorte son politransfundidos (talasemia, hemodiálisis) más 100 donantes sanos; el viroma en sangre puede reflejar exposición transfusional. Aun así caracteriza la comunidad viral en sangre. Confirmar que encaja en el criterio.
3. **bangladesh2020 (BD).** El estudio incluye 16 lactantes de EE. UU. como comparación; las muestras principales (30) son de Bangladés. Lo marqué BD. Confirmar al leer el texto.
4. **qatar2022 y kuwait2020.** Son niños con gastroenteritis, pero el enfoque es metagenómica de la diversidad viral (comunidad), no vigilancia de un solo patógeno. Los conté como caracterización de comunidad; revisar por si se prefieren fuera.
5. **Columna `n` vacía** en varias filas (india_gut2022, latam_diarrhea2016, kuwait2020, kenya_infants2026, qatar2022): no pude fijar un recuento con unidad clara desde la abstract sin transcribir a ojo. Preferí dejarlo en blanco a poner un número dudoso. Rellenar al verificar el texto completo.
6. **`title` vacío a propósito** en las 11 filas: se rellena solo con `scripts/fetch-titles.py` desde CrossRef, como indica el README.
7. **Sitio piel sigue sin cubrir.** Depende de resolver el punto de Foulongne (arriba) o de aceptar el estudio de EE. UU. de Hannigan.

---

## 4. Referencias de los estudios añadidos (para la verificación)

- india_gut2022 — https://doi.org/10.1099/jgv.0.001774
- cameroon2019 — https://doi.org/10.1128/msphere.00585-18
- bangladesh2020 — https://doi.org/10.1038/s41598-020-71791-4
- iran_blood2023 — https://doi.org/10.3390/v15071425
- vietnam2025 — https://doi.org/10.3390/pathogens14100985
- latam_diarrhea2016 — https://doi.org/10.1007/s00705-016-2756-4
- spain_oral2018 — https://doi.org/10.1371/journal.pone.0191867
- southafrica_resp2022 — https://doi.org/10.3390/v14112516
- kuwait2020 — https://doi.org/10.1186/s12985-020-1287-5
- kenya_infants2026 — https://doi.org/10.1016/j.isci.2026.114900
- qatar2022 — https://doi.org/10.1016/j.meegid.2022.105367
