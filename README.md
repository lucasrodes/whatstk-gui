# Graphical User Interface for whatstk

## Create App
Given a script name `app.py `

```
pyinstaller --onefile --windowed --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' --name test --icon='favicon2.ico' test.py
```

pyinstaller --onefile --windowed app.spec
