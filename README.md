# Graphical User Interface for whatstk

## Create App
Given a script name `app.py `

```
pyinstaller --onefile --windowed --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' --name cd WhatsTK --icon='favicon.png' app.py
```