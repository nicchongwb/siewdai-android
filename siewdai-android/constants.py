import os

PROJ_PATH = os.path.dirname(os.path.realpath(__file__))
APK_PATH = f"{os.path.abspath(os.path.join(PROJ_PATH, os.pardir))}/apk"
RESOURCES_PATH = f"{os.path.abspath(os.path.join(PROJ_PATH, os.pardir))}/resources"
OUTPUT_PATH = f"{os.path.abspath(os.path.join(PROJ_PATH, os.pardir))}/output"
OUTPUT_APKTOOL_PATH = f"{OUTPUT_PATH}/apktool"
OUTPUT_JADX_PATH = f"{OUTPUT_PATH}/jadx"


APKTOOL_JAR = RESOURCES_PATH + '/apktool/apktool_2.11.1.jar'
APKTOOL_BINARY = RESOURCES_PATH + '/apktool/apktool'
JADX_BINARY = RESOURCES_PATH + '/jadx/bin/jadx'