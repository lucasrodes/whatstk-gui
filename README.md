## Generate release

Run

```
sh generate-release.sh
```

to generate a release from the current code in `app.py`. App is exported as dmg and stored at

```
releases
|-<version>
  |-WhatsTK-<version>-<OS>-<OS_VERSION>.dmg
```


```
$ sh generate-release.sh
```

_Note: requires a script `set-environment-variables.sh`, which sets the environment variables `PLOTLY_PATH`, `PROJECT_PATH`, `LIB_PAT`._