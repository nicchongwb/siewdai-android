# siewdai-android
Security Testing tool for APK to reduce sweetness and bug attraction

## Why siewdai-android?

Android comes in many different confectionery flavors. We know sweet and sugar attract bugs and we don't want that. Siew-dai in Cantonese means less sweet. Siewdai-android aims to automate all the mundane security testing of APKs.

## Requirements

Docker
Jadx
Apktool

## Usage

The tool will dynamically download jadx from https://github.com/skylot/jadx/releases/download/v1.5.1/jadx-v1.5.1.zip unzip into the resources directory. This project comes with the necessary binaries in resources directory. If you require another jadx version, manually change accordingly before building the Docker image.
```
resources
└── jadx
    ├── LICENSE
    ├── README.md
    ├── bin
    │   ├── jadx
    │   ├── jadx-gui
    │   ├── jadx-gui.bat
    │   └── jadx.bat
    └── lib
        └── jadx-1.5.1-all.jar
```

This project also comes with APKTool v2.11.1 in resources directory. If needed change it accordingly before building Docker image.


Place APK files into apk directory of this project

Linux
```sh
./run.sh
```



## Configuration

Before building the Docker image, you can change the resources such as jar (eg. apktool), or config such as string-search-regex.json.


## Features

- Finding hardcoded sensitive information in APK
- Finding sensitive information in Fridump data
- APK SSL certificate expiry

