# Tarea programada para Claude Cowork — buscar papers de viroma humano

Dale acceso solo a la carpeta `~/Desktop/ViromeCity/data/`. No necesita más, y
así no puede tocar nada del libro.

Pégale el texto de debajo de la línea con `/schedule`, cadencia mensual.

Cuando termine, aquí hacemos: rellenar títulos → verificar → confirmar países →
`quarto render` → commit → push. Nada de lo que Cowork escriba llega a la web
hasta que pase por eso.

---

Cada mes, busca estudios publicados de **viroma humano** que no estén ya en mi
lista, y añádelos a `data/studies.csv`.

## Contexto

Estoy construyendo un mapa interactivo para un libro sobre análisis de viroma
humano. El mapa colorea cada país por cuánto se ha muestreado en repositorios
públicos, y al hacer clic en un país despliega los artículos que lo estudiaron.
Ese listado de artículos es lo que tú alimentas. Sirve para que un investigador
encuentre su propia población y llegue al paper.

## Qué buscar

Los criterios canónicos están en `data/README.md`, sección "What qualifies as a
study" — léela. Lo de abajo es el resumen.

Estudios primarios que **secuencien el viroma de sujetos humanos**: intestino,
vaginal, sangre, oral, piel, respiratorio, cualquier sitio corporal.

**Sí cuentan:** metagenómica viral, enriquecimiento VLP, viroma DNA o RNA,
estudios de cohorte que caractericen la comunidad viral.

**No cuentan:** revisiones, catálogos y bases de datos agregadas (GPD, MGV,
CHVD, GVD ya están contemplados aparte), estudios de un solo virus o de
vigilancia de patógenos sin caracterización de comunidad, y cualquier cosa que
no sea de sujetos humanos.

**Prioriza países que faltan.** La lista está muy sesgada hacia Europa, EE. UU.,
China y Japón. Un estudio de África subsahariana, Sudamérica, el sur de Asia u
Oceanía vale mucho más que el número dieciocho de una cohorte danesa.

## Cómo añadirlos

Abre `data/studies.csv` y **añade filas al final**. No modifiques ni reordenes
las que ya están. Lee `data/README.md` antes: explica cada columna.

Las columnas son:

```
id,verified,countries,year,site,n,label,title,url
```

Rellena así:

| columna | qué poner |
|---|---|
| `id` | `primerautor + año`, en minúsculas: `shkoporov2019`. Si no hay primer autor obvio, `lugar_tema`: `ethiopia_amhara` |
| `verified` | **siempre `no`.** Sin excepciones — ver abajo |
| `countries` | ISO-3166 **alpha-2** del país **de las muestras**, `;` para varios: `CN;PK` |
| `year` | año de **publicación** |
| `site` | `gut`, `vaginal`, `blood`, `gut, oropharynx` … |
| `n` | como lo diga el paper, **con su unidad**: `647 one-year-olds`, `12 samples` |
| `label` | versión corta y fiel del título, para que quepa en el panel del mapa |
| `title` | **déjalo vacío.** Se rellena solo desde CrossRef |
| `url` | `https://doi.org/…`. Si solo tienes un PMC ID, conviértelo a DOI antes |

Las comas dentro de un campo van entre comillas dobles: `"4,198 individuals"`.

## Las cuatro reglas que no puedes romper

**1. `verified` es siempre `no`.** Tú no verificas nada. Una persona resuelve
después el DOI y confirma el registro. Una fila marcada `no` no aparece en el
mapa publicado — se queda esperando. Si pusieras `yes`, publicarías algo que
nadie ha comprobado.

**2. El país es de dónde salieron las muestras, no dónde trabajan los autores.**
Un grupo de Boston publicando sobre una cohorte de Malawi es `MW`. Este es el
campo que ninguna herramienta puede comprobar por ti, y el que más se equivoca.
Si el paper no lo dice con claridad, **no adivines**: pon el país que sí puedas
sostener y anótalo en el informe.

**3. El país cuenta solo donde se secuenció el viroma.** Muchos papers tamizan
cohortes extra por PCR buscando un virus concreto; esos países **no** cuentan. Y
suelen estar en el cuerpo del artículo, no en el abstract — si solo lees el
abstract no los verás, así que ante un estudio multipaís di en el informe qué
pudiste comprobar y qué no.

**4. No inventes DOIs.** Si no encuentras el identificador, no añadas la fila.
Prefiero una lista corta a una con un enlace que no lleva a ninguna parte.

## Qué entregar

Además de las filas, escribe `data/pendientes.md` (sobrescríbelo cada vez) con:

- Cuántas filas añadiste y de qué países
- Cualquier estudio que encontraste y **descartaste**, y por qué — sobre todo si
  fue por no poder determinar el país
- Cualquier duda que necesite ojo humano

Y para que sepas si algo ya está: los identificadores actuales de la lista son
la columna `id` del CSV. Compruébalos antes de añadir, para no duplicar.
