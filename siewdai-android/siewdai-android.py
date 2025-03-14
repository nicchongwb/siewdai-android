#!/usr/bin/env python
import os
import threading
from constants import *
import install.install_tools as Installer
import utils.utils as Utils
import decompiler.apktool as Apktool

def main():
    # proj_path = os.path.dirname(os.path.realpath(__file__))
    # apk_path = f"{os.path.abspath(os.path.join(proj_path, os.pardir))}/apk"
    # resources_path = f"{os.path.abspath(os.path.join(proj_path, os.pardir))}/resources"
    # output_path = f"{os.path.abspath(os.path.join(proj_path, os.pardir))}/output"

    # Setup project
    proj_dirs_path = [APK_PATH, RESOURCES_PATH, OUTPUT_PATH]
    Utils.setup_proj_dirs(proj_dirs_path)

    # Install necessary tools
    t_install_apktool = threading.Thread(
        target=Installer.install_apktool(RESOURCES_PATH),
        name='t_install_apktool',
        args=(RESOURCES_PATH))
    
    t_install_jadx = threading.Thread(
        target=Installer.install_jadx(RESOURCES_PATH),
        name='install_jadx',
        args=(RESOURCES_PATH))
    
    t_install_apktool.start()
    t_install_jadx.start()

    t_install_apktool.join()
    t_install_jadx.join()

    # Necessary config, apk checks
    

    # TODO run each feature accordingly

    # Apktool decompile
    Apktool.decompile(APK_PATH, OUTPUT_PATH)    

if __name__=="__main__":
    main()