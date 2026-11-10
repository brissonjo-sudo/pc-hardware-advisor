<!-- language-bar -->
[English](../README.md) · [Français](README.fr.md) · **Español** · [Deutsch](README.de.md) · [Português](README.pt.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)
<!-- /language-bar -->

> Traducción automática no revisada por una persona. La versión en inglés (../README.md) prevalece. Las correcciones son bienvenidas: consulta ../CONTRIBUTING.md.

# PC Hardware Advisor

PC Hardware Advisor es un plugin para Claude (Claude Code, y Cowork en la aplicación de escritorio de Claude) que hace que Claude sea fiable en hardware de PC de escritorio. Encuentra el mejor precio entregado de una pieza en cualquier lugar del mundo, comprueba que las piezas funcionan juntas, diseña equipos completos para un uso y un presupuesto, dimensiona máquinas para IA local, valora anuncios de segunda mano y vigila precios de forma programada. Cada cifra que ofrece tiene fecha, fuente y un grado de confianza, y el plugin solo lee: nunca compra nada y nunca contacta con un vendedor.

Claude responde en el idioma en que escribes. Los nombres de las piezas, los SKU y las unidades se mantienen tal como se publican.

## Qué hace

Seis skills y un subagente.

- **`hunt-prices`**: encuentra el mejor precio entregado (con IVA, aranceles y envío incluidos) para un artículo exacto, en todo el mundo. Los distribuidores directos aparecen primero, los mercados se listan por separado y cada fila incluye una columna de confianza. Usa el agente `price-scout` para leer varias webs en paralelo.
- **`check-compatibility`**: emite veredictos por pares entre piezas: compatible, compatible con condiciones o incompatible. Un veredicto condicional indica la condición exacta y la fuente.
- **`build-config`**: diseña un equipo completo a partir del uso, el presupuesto, el país y tus restricciones. Devuelve una configuración principal y una variante más barata y otra más potente. Solo propone piezas nuevas y piezas reacondicionadas profesionalmente.
- **`size-local-ai`**: dimensiona hardware para ejecutar modelos en local. Cubre VRAM, ancho de banda de memoria, estimaciones de tokens por segundo (etiquetadas como estimaciones), multi-GPU, APU, eGPU y pilas de software.
- **`review-used-listing`**: revisa un anuncio de segunda mano concreto y devuelve un veredicto: comprar, negociar o evitar. Añade preguntas para el vendedor, pruebas que hacer en la entrega y un margen de negociación.
- **`track-price`**: programa nuevas comprobaciones de un precio, te avisa solo cuando baja de tu umbral y mantiene un archivo de historial. Nunca compra.
- **`price-scout`** (agente): lee varias páginas de distribuidores o mercados para una pieza exacta y devuelve filas de precios normalizadas, sin análisis. `hunt-prices` lo lanza.

Fuera del alcance: consolas, smartphones, tabletas, portátiles como productos, y cualquier cosa que compre o contacte con vendedores.

## Principios

- **Cada precio tiene fecha.** Un precio sin fecha de lectura no se informa.
- **El vendedor está tipificado.** Distribuidor directo, vendedor de mercado, reacondicionador o particular son filas distintas, nunca mezcladas.
- **Precio entregado, o "sin gastos".** Los precios incluyen IVA, aranceles y envío a tu país. Cuando no se puede establecer un componente, la fila indica "sin gastos" en lugar de adivinar.
- **La confianza se muestra.** Cada cifra indica cuán bien está respaldada.
- **Nada se inventa.** Si una especificación, un precio o una norma no se puede justificar con una fuente, Claude lo dice.
- **Sitios bloqueados: recurso al navegador, nunca trucos.** Si un sitio rechaza la lectura automatizada y hay una herramienta de navegador disponible, Claude te ofrece en una línea abrir la página en tu navegador; responde «sí» y lee las pocas páginas que importan, solo de lectura, y lo indica. Se detiene ante cualquier captcha o control de bots y nunca imita a una persona para superarlo. Si no, te pide una captura de pantalla o texto pegado. No se usan agentes de usuario alternativos, cachés ni espejos.
- **Solo lectura.** El plugin nunca compra, nunca crea cuentas, nunca envía formularios y nunca contacta con vendedores. Eso lo haces tú.

Diez referencias compartidas (método de investigación, tiendas por país, criterios para tiendas, compra internacional, lista de verificación del mercado de segunda mano, zócalos y chipsets, memoria, fuentes de alimentación y conectores, factores de forma y cajas, ancho de banda de GPU para IA) están fechadas y tienen fuentes. Se revisaron por última vez el 2026-11-07.

## Instalación

### Claude Code

Usa el repositorio como marketplace y luego instala el plugin desde él.

```
claude plugin marketplace add <owner/repo or local path>
claude plugin install pc-hardware-advisor@pc-hardware-advisor
```

`marketplace add` acepta un repositorio de GitHub (`owner/repo`), una URL de git o https, o una ruta local. Para este repositorio, la dirección de GitHub es `brissonjo-sudo/pc-hardware-advisor`. Añade `--scope project` o `--scope local` a cualquiera de los dos comandos si no quieres una instalación para todo el usuario (el valor por defecto es `user`).

Revisa lo instalado con `claude plugin marketplace list`.

### Desarrollo local

Para probar el plugin desde una copia de trabajo sin instalarlo:

```
claude --plugin-dir <path to this repository>
```

### Claude de escritorio / Cowork

Obtén el archivo `pc-hardware-advisor.plugin` (adjunto a una versión cuando se publica una, o generado desde una copia de trabajo con `python scripts/build_plugin.py`, que lo escribe en `dist/`), arrástralo a la aplicación de escritorio de Claude y acepta el aviso de instalación.

### OpenAI Codex (experimental)

El repositorio también es un marketplace de Codex (`.agents/plugins/marketplace.json`, manifiesto `.codex-plugin/plugin.json`). Añádalo y luego instale el plugin desde el directorio de plugins de la aplicación de escritorio de ChatGPT o de Codex (`/plugins`):

```
codex plugin marketplace add brissonjo-sudo/pc-hardware-advisor
```

Aún no probado. Codex no tiene subagentes: las páginas de precios se leen una a una, más despacio. El seguimiento de precios programado necesita una herramienta de programación en la sesión. El repositorio es privado: el comando necesita acceso git a él.

## Actualizar, verificar y desinstalar

**Actualizar (Claude Code).** Actualice el marketplace, luego el plugin, y reinicie Claude Code:

```
claude plugin marketplace update pc-hardware-advisor
claude plugin update pc-hardware-advisor@pc-hardware-advisor
```

Solo se ofrece una actualización cuando cambia la `version` de `plugin.json`.

**Verificar.** Pregunte a Claude «¿qué skills de plugin tienes para hardware de PC?», o ejecute `claude plugin list` y busque `pc-hardware-advisor` y su versión.

**Desinstalar.** Ejecute `claude plugin uninstall pc-hardware-advisor@pc-hardware-advisor`. En la aplicación de escritorio de Claude, quite el plugin en los ajustes de plugins. Los archivos de historial de precios que creó permanecen donde los guardó.

El repositorio es actualmente privado, así que la vía del marketplace solo funciona para cuentas con acceso; el archivo `.plugin` es la alternativa.

## Ejemplos de peticiones

Claude elige la skill adecuada según la petición. Algunos ejemplos:

1. "Encuentra el mejor precio entregado en Alemania para un Ryzen 7 9800X3D. Primero distribuidores directos, mercados por separado."
2. "¿Compensa más importar una RTX 5070 Ti desde EE. UU. a Canadá una vez incluidos los aranceles y el envío?"
3. "¿Funcionará este kit DDR5-6000 con una placa ASUS TUF B650 y un Ryzen 7 7700? Dame un veredicto por cada par."
4. "Prepárame un PC gaming silencioso para 1440p con 1.400 EUR en España. Dame también una variante más barata y otra más potente."
5. "Quiero ejecutar un modelo de 70B en local a una velocidad utilizable. ¿Qué VRAM y ancho de banda de memoria necesito, y bastarían dos GPU de 24 GB de segunda mano?"
6. "Revísame este anuncio de una RTX 3090 de segunda mano (enlace abajo). ¿La compro, negocio o la evito? ¿Qué le pregunto al vendedor?"
7. "Vigila el precio de la Samsung 990 Pro de 2 TB en el Reino Unido y avísame solo si baja de 120 GBP."
8. En francés: "Trouve-moi le meilleur prix livré en France pour une alimentation 850 W ATX 3.1, vendeurs directs d'abord, places de marché à part."
9. En español: "Quiero montar un PC para edición de vídeo con 1.800 EUR en España. ¿Qué configuración me recomiendas, y qué compatibilidad debo vigilar entre placa, RAM y GPU?"
10. "¿Puede una APU con 64 GB de memoria unificada ejecutar un modelo de 32B, y a qué velocidad? Indica qué es una estimación."

## Conectores

Las skills se refieren a las herramientas por categoría (búsqueda web, lectura web, comparador de precios, sitio de anuncios clasificados, navegador, programador, notificaciones), no por producto, así que cualquier herramienta equivalente sirve. Nada en el plugin requiere una cuenta, una clave de API ni un servicio de pago. Las categorías, las fuentes de datos opcionales y las reglas que se aplican a todas las herramientas están en [CONNECTORS.md](../CONNECTORS.md).

## Límites

- **Los precios son perecederos.** Un precio solo es válido en su fecha de lectura. El stock y las promociones cambian en cuestión de horas.
- **Algunos sitios bloquean la lectura automatizada.** Esas filas se marcan como bloqueadas, y Claude te pide una captura de pantalla o texto pegado.
- **Las normas fiscales y arancelarias son volátiles.** El IVA, los aranceles aduaneros y los umbrales de minimis cambiaron varias veces en 2025 y 2026. Consulta la fuente oficial antes de una importación grande.
- **Las estimaciones son estimaciones.** Las cifras de tokens por segundo y las proyecciones similares son modeladas, no medidas en tu equipo, y se etiquetan como tales.
- **La cobertura de la investigación tiene huecos.** Algunos países, tiendas y piezas de nicho están cubiertos de forma escasa. Las referencias indican dónde.
- **Use el esfuerzo alto.** En las pruebas del mantenedor, `build-config` con esfuerzo medio leyó menos tiendas y pasó por alto opciones más baratas. Elija el esfuerzo alto en su aplicación antes de pedir una configuración o una búsqueda de precios.
- **No es asesoramiento financiero ni jurídico.** El plugin informa una decisión de compra. No asesora sobre cuestiones fiscales, aduaneras ni de derecho de consumo.

## Privacidad

El plugin en sí no recopila nada ni envía nada a ningún sitio. Los historiales de precios que escribe `track-price` se quedan donde tú decidas guardarlos. Las herramientas que Claude usa para buscar y leer páginas (búsqueda web, lectura web, programador) se rigen por las condiciones y las políticas de privacidad de sus propios proveedores.

## Traducciones

Traducciones automáticas de este README, no revisadas por una persona: [README.fr.md](README.fr.md), [README.es.md](README.es.md), [README.zh-CN.md](README.zh-CN.md), [README.hi.md](README.hi.md), [README.pt.md](README.pt.md), [README.ar.md](README.ar.md), [README.de.md](README.de.md), [README.ja.md](README.ja.md). Prevalece la versión en inglés.

## Contribuir

Las contribuciones son bienvenidas bajo condiciones específicas, que incluyen una cesión de derechos. Lee [CONTRIBUTING.md](../CONTRIBUTING.md) antes de abrir una pull request.

## Licencia

PC Hardware Advisor es de código disponible bajo la PolyForm Noncommercial License 1.0.0 (SPDX: PolyForm-Noncommercial-1.0.0). El uso no comercial está permitido para todo el mundo; el uso comercial requiere una licencia separada del autor. La misma licencia cubre las skills, las referencias, la documentación y las traducciones.

Texto completo: [LICENSE](../LICENSE) y <https://polyformproject.org/licenses/noncommercial/1.0.0>.
