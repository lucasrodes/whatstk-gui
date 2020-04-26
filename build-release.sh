#!/bin/sh
# Exports the current version of the project and stores it as a zip unde releases/v<VERSION>.
# ONLY TESTED ON MAC
ECHO ">> 1 DEFINING VARIABLES"
sh set-environment-variables.sh  # Set variables PLOTLY_PATH, PROJECT_PATH, LIB_PATH

VERSION=v0.0.0
APP_NAME=WhatsTK

OS=macOS
OS_VERSION=10.13
OS_NAME=${OS}-${OS_VERSION}

DEBUG_PATH=debug/${VERSION}
RELEASE_PATH=releases/${VERSION}

# build app
ECHO ">> 2 CREATE EXECUTABLE"
mkdir -p ./${RELEASE_PATH}
pyinstaller --distpath ./${RELEASE_PATH} app.spec

# Add required files
ECHO ">> 3 ADDING EXTERNAL PACKAGES (tk, tcl)"
mkdir -p ${PROJECT_PATH}/${RELEASE_PATH}/${APP_NAME}.app/Contents/lib/
cp -r ${LIB_PATH}/tk8.6 ${PROJECT_PATH}/${RELEASE_PATH}/${APP_NAME}.app/Contents/lib/tk8.6 
cp -r ${LIB_PATH}/tcl8.6 ${PROJECT_PATH}/${RELEASE_PATH}/${APP_NAME}.app/Contents/lib/tcl8.6 

# Compress
ECHO ">> 4 CREATE DMG"
[ -f ./${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.dmg ] && rm ./${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.dmg
hdiutil create -format UDZO -srcfolder ./${RELEASE_PATH}/${APP_NAME}.app/ ./${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.dmg
# tar -zcvf test.tar.gz ${RELEASE_PATH}/${APP_NAME}.app/ ${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.dmg

# Move to debug
ECHO ">> 5 MOVE TO DEBUG"
mkdir -p ${DEBUG_PATH}
[ -f ./${DEBUG_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.app/ ] && rm - f ../${DEBUG_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.app/
[ -f ./${DEBUG_PATH}/app-${VERSION}-${OS_NAME} ] && rm ./${DEBUG_PATH}/app-${VERSION}-${OS_NAME}

mv -f ./${RELEASE_PATH}/${APP_NAME}.app ./${DEBUG_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.app
mv -f ./${RELEASE_PATH}/app ./${DEBUG_PATH}/app-${VERSION}-${OS_NAME}