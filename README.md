# Graphical User Interface for whatstk

## Create App
Given a script name `script.py `

```
pyinstaller --onefile --windowed --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' script.py
```