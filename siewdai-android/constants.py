import os

PROJ_PATH = os.path.dirname(os.path.realpath(__file__))
APK_PATH = f"{os.path.abspath(os.path.join(PROJ_PATH, os.pardir))}/apk"
RESOURCES_PATH = f"{os.path.abspath(os.path.join(PROJ_PATH, os.pardir))}/resources"
OUTPUT_PATH = f"{os.path.abspath(os.path.join(PROJ_PATH, os.pardir))}/output"

APKTOOL_BINARY = RESOURCES_PATH / '/apktool/apktool_2.11.1.jar'
JADX_BINARY = RESOURCES_PATH / '/jadx/bin/jadx'