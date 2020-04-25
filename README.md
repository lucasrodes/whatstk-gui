<head>
 <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
</head>

# Analyze your WhatsApp chats
**[versión en español](esp.md)**

Use *WhatsTK* to analyse your WhatsApp chats. **Currently it is only available for mac OS.**

<br>

<table class="tg" style="display: flex; justify-content: center;">
    <tr>
        <th class="tg-fymr" colspan="2">Downloads</th>
    </tr>
    <tr>
        <td class="tg-0pky">macOS (Catalina)</td>
    <td class="tg-0pky"><a href="dist/WhatsTK.zip"><img src="https://img.shields.io/badge/download_zip_⬇-brightgreen.svg"
    alt="WhatsTK user interface" width="100%"></a>
    </td>
    </tr>
</table>
<br>

## How to use

1. UnZip the downloaded file.
2. Start the program (double click on the file)
3. Once the Software is loaded (might take few seconds), click on _Load chat file_ to select file.

<p style="text-align: center;">
<img src="assets/app-screenshot.png" alt="WhatsTK user interface" width="500" height='auto' style="box-shadow: 10px 13px 21px -6px
rgba(0,0,0,0.22);">
</p>

4. Write down the header format of your whatsapp chat file. For instance `%d.%m.%y, %H:%M - %name:` (check more on
   `headers` section below).
5. Click on `Run`.

<br>

Below an example of the results

<br>
<p style="text-align: center;">
<img src="assets/stats.png" alt="WhatsTK user interface" width="500" height='auto' style="box-shadow: 10px 13px 21px -6px
rgba(0,0,0,0.22);">
</p>
<br>

---
## FAQs

* **How can I get the chat of a WhatsApp chat?**

    Open the WhatsApp chat you want to analyze on your mobile phone. Click on _More_, then click on _Export chat_ and
    choose _Without media_. Wait few seconds until the chat export file has been created and save it (recommended: send it via mail to yourself so it is available on your computer).


* **App icon shows on Dock, disappears and then appears again.**

    This is the normal behaviour. Wait until it loads.

* **Which is the header of my chat?**

    Open the exported chat file. You will find that the messages have a similar format:

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

    In this example, the header is "DAY.MONTH.YEAR, HOUR:MINUTES - USERNAME:", which corresponds to a header format code
    is: `%d.%m.%Y, %H:%M - %name:`.
    
<table class="tg" style="display: flex; justify-content: center;">
  <tr>
    <th class="tg-7btt">Date Unit Code</th>
    <th class="tg-7btt">Definition</th>
  </tr>
  <tr>
    <td class="tg-0pky">%y</td>
    <td class="tg-0pky">Year</td>
  </tr>
  <tr>
    <td class="tg-0pky">%m</td>
    <td class="tg-0pky">Month of the year (1-12)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%d</td>
    <td class="tg-0pky">Day of the month (0-31)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%H</td>
    <td class="tg-0pky">Hour 24h-clock (0-23)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%P</td>
    <td class="tg-0pky">Hour 12h-clock (1-12)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%M</td>
    <td class="tg-0pky">Minutes (0-60)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%name</td>
    <td class="tg-0pky">Name of user</td>
  </tr>
</table>

* **I am an experimented coder. Where can I access to the code?**

    Check python library [whatstk](https://lcsrg.me/whatstk).

<br>
<br>
> **Not resolved? Ask your question [here](https://github.com/lucasrodes/whatstk-gui/issues)!**

---

*This library uses [whatstk](https://lcsrg.me/whatstk) python library.*