#!/bin/sh
# Exports the current version of the project and stores it as a zip unde releases/v<VERSION>.
# ONLY TESTED ON MAC
ECHO ">> 1 DEFINING VARIABLES"
sh set-environment-variables.sh  # Set variables PLOTLY_PATH, PROJECT_PATH, LIB_PATH

VERSION=v0.0.1
APP_NAME=WhatsTK

OS=macOS
OS_VERSION=10.13
OS_NAME=${OS}-${OS_VERSION}

DEBUG_PATH=debug/${VERSION}
RELEASE_PATH=releases/${VERSION}
mkdir -p ./${RELEASE_PATH}
mkdir -p ./${DEBUG_PATH}

# build app
ECHO ">> 2 CREATE EXECUTABLE"
[ -f ./${DEBUG_PATH}/${APP_NAME} ] && rm -fr ./${DEBUG_PATH}/${APP_NAME}.app/
[ -f ./${DEBUG_PATH}/${APP_NAME}.app/ ] && rm -fr ./${DEBUG_PATH}/${APP_NAME}
pyinstaller --distpath ./${DEBUG_PATH} app.spec

# Add required files
ECHO ">> 3 ADDING EXTERNAL PACKAGES (tk, tcl)"
mkdir -p ./${DEBUG_PATH}/${APP_NAME}.app/Contents/lib/
cp -r ${LIB_PATH}/tk8.6 ${PROJECT_PATH}/${DEBUG_PATH}/${APP_NAME}.app/Contents/lib/tk8.6 
cp -r ${LIB_PATH}/tcl8.6 ${PROJECT_PATH}/${DEBUG_PATH}/${APP_NAME}.app/Contents/lib/tcl8.6 

# Create DMG
ECHO ">> 4 CREATE DMG"
# [ -f ./${DEBUG_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.dmg ] && rm ./${DEBUG_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.dmg
# tar -zcvf test.tar.gz ${RELEASE_PATH}/${APP_NAME}.app/ ${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}.dmg
[ -f ./${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}-Installer.dmg ] && rm -f ./${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}-Installer.dmg
create-dmg \
    --volname ${APP_NAME}-${VERSION}-${OS_NAME}-Installer \
    --window-pos 200 120 \
    --window-size 500 128 \
    --background "assets/drop-arrow.png" \
    --icon-size 128 \
    --icon ${APP_NAME}.app 64 64 \
    --hide-extension ${APP_NAME}.app \
    --app-drop-link 320 64 \
    ./${RELEASE_PATH}/${APP_NAME}-${VERSION}-${OS_NAME}-Installer.dmg \
    ./${DEBUG_PATH}/${APP_NAME}.app/