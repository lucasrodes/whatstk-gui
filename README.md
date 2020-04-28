## Generate release

Run

```
sh build-release.sh
```

to generate a release from the current code in `app.py`. App is exported as dmg and stored at

```
releases
|-<version>
  |-WhatsTK-<version>-<OS>-<OS_VERSION>-Installer.dmg
```


```
$ sh generate-release.sh
```

_Note: requires a script `set-environment-variables.sh`, which sets the environment variables `PLOTLY_PATH`,
`PROJECT_PATH`, `LIB_PATH`._


### HEADER FORMAT


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
    <td class="tg-0pky">%S</td>
    <td class="tg-0pky">Seconds (0-60)</td>
  </tr>
  <tr>
    <td class="tg-0pky">%name</td>
    <td class="tg-0pky">Name of user</td>
  </tr>
</table>