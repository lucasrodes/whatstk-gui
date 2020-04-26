<head>
 <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
</head>

# Analiza tus chats de WhatsApp (versión beta)
**[english version](../index.md)**

Utiliza *WhatsTK* para analizar las conversaciones de tus chats en WhatsApp. **Actualmente sólo está disponible para macOS**

<br>

<table class="tg" style="display: flex; justify-content: center;">
    <tr>
        <th class="tg-fymr" colspan="2">Descargas</th>
    </tr>
    <tr>
        <td class="tg-0pky">macOS (10.13 y superior)</td>
    <td class="tg-0pky"><a href="dist/WhatsTK.zip"><img src="https://img.shields.io/badge/descargar_zip_⬇-brightgreen.svg"
    alt="WhatsTK user interface" width="100%"></a>
    </td>
    </tr>
</table>
<br>

## Cómo usar

1. Descomprime el archivo descargado.
2. Arranca el programa (doble click en el archivo)
3. Cuando se haya cargado (puede tardar unos segundos), clica e _Load chat file_ para cargar tu archivo `txt` de WhatsApp.

<p style="text-align: center;">
<img src="assets/app-screenshot.png" alt="WhatsTK user interface" width="500" height='auto' style="box-shadow: 10px 13px 21px -6px
rgba(0,0,0,0.22);">
</p>

4. Introduce el formato de la cabecera de los mensajes de tus chats de WhatsApp. Por ejemplo, `%d.%m.%y, %H:%M - %name:`.
5. Clica `Run`.

<br>

A continuación un ejemplo

Los resultados tienen el formato `HTML`, de modo que los grafos son interactivos. A continuación un ejemplo.

<br>
<p style="text-align: center;">
<img src="assets/stats.png" alt="WhatsTK user interface" width="500" height='auto' style="box-shadow: 10px 13px 21px -6px
rgba(0,0,0,0.22);">
</p>
<br>

---
## Preguntas frecuentes

* **¿Como puedo exportar un chat de WhatsApp como fichero?**

    Accede al chat de WhatsApp que quieras analizar usando tu teléfono móbil. Clica en _More_, luego  en _Export chat_ y
    selecciona _Without media_. Espera unos segundos hasta que se genere el fichero (puede tardar varios si el chat es
    pesado) y guárdalo en un lugar que recuerdes (recomendado:
    enviatelo vía correo electrónico a ti mismo/a, de modo que lo tengas accesible en tu ordenador).


* **El icono de la aplicación aparece y desaparece en el Dock. ¿Funciona bien?**

    Este comportamiento es habitual. Espera hasta que se cargue.

* **¿Qué significa el _header_ de mi chat?**

    Abre el archivo del chat exportado (fichero `txt`). Encontraras todos los mensajes del chat en un formato parecido
    al siguiente:

    ```
    15.04.2016, 15:04 - You created group “Sample Group”
    06.08.2016, 13:18 - Messages you send to this group are now secured with end-to-end encryption. Tap for more info.
    06.08.2016, 13:23 - Ash Ketchum: Hey guys!
    06.08.2016, 13:25 - Brock: Hey Ash, good to have a common group!
    06.08.2016, 13:30 - Misty: Hey guys! Long time haven't heard anything from you
    06.08.2016, 13:45 - Ash Ketchum: Indeed. I think having a whatsapp group nowadays is a good idea
    06.08.2016, 14:30 - Misty: Definetly
    06.08.2016, 17:25 - Brock: I totally agree
    07.08.2016, 11:45 - Prof. Oak: Kids, shall I design a smart poke-ball?
    ```

    En este ejemplo, el _header_ es "DÍA.MES.AÑO, HORA:MINUTOS - NOMBRE DE USUARIO:", que corresponde al _header format code_ `%d.%m.%Y, %H:%M - %name:`.
    
<table class="tg" style="display: flex; justify-content: center;">
  <tr>
    <th class="tg-7btt">Codigo unidad de fecha</th>
    <th class="tg-7btt">Definición</th>
  </tr>
  <tr>
    <td class="tg-0pky">%y</td>
    <td class="tg-0pky">Año</td>
  </tr>
  <tr>
    <td class="tg-0pky">%m</td>
    <td class="tg-0pky">Mes del año (1-12)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%d</td>
    <td class="tg-0pky">Día del mes (0-31)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%H</td>
    <td class="tg-0pky">Hora reloj 24h (0-23)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%P</td>
    <td class="tg-0pky">Hora reloj 12h (1-12)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%M</td>
    <td class="tg-0pky">Minutos (0-60)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%S</td>
    <td class="tg-0pky">Segundos (0-60)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%name</td>
    <td class="tg-0pky">Nombre del usuario</td>
  </tr>
</table>

* **Soy programador, ¿dónde puedo acceder al código del proyecto?**

    Consulta la librería de python [whatstk](https://lcsrg.me/whatstk).


**Aun tienes dudas? Pregunta-nos [aquí](https://github.com/lucasrodes/whatstk-gui/issues)!**

<br>

---

*Esta librería usa la librería de python [whatstk](https://lcsrg.me/whatstk).*