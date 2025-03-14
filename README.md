# siewdai-android
Security Testing tool for APK to reduce sweetness and bug attraction

## Why siewdai-android?

Android comes in many different confectionery flavors. We know sweet and sugar attract bugs and we don't want that. Siew-dai in Cantonese means less sweet. Siewdai-android aims to automate all the mundane security testing of APKs.

## Requirements

Docker

## Usage

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

