#!/usr/bin/env python
import install.install_tools as Installer
import utils.utils as Utils
import os
import threading

def main():
    proj_path = os.path.dirname(os.path.realpath(__file__))
    apk_path = f"{os.path.abspath(os.path.join(proj_path, os.pardir))}/apk"
    resources_path = f"{os.path.abspath(os.path.join(proj_path, os.pardir))}/resources"
    output_path = f"{os.path.abspath(os.path.join(proj_path, os.pardir))}/output"

    # Setup project
    proj_dirs_path = [apk_path, resources_path, output_path]
    Utils.setup_proj_dirs(proj_dirs_path)

    # Install necessary tools
    t_install_jadx = threading.Thread(
        target=Installer.install_jadx(resources_path),
        name='install_jadx',
        args=(resources_path))
    t_install_jadx.start()
    

    # Necessary config, apk checks
    

    # TODO run each feature accordingly
    

if __name__=="__main__":
    main()