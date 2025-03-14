import os
import sys
import logging
import subprocess
from pathlib import Path
from constants import APKTOOL_BINARY, APKTOOL_JAR, OUTPUT_APKTOOL_PATH

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)-15s - %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S')
logger = logging.getLogger(__name__)

def decompile(APK_PATH, OUTPUT_PATH=OUTPUT_APKTOOL_PATH):
    logger.info(f"APKTool decompiling .apk files at {OUTPUT_PATH}")
    apk_paths = []

    for file in os.listdir(APK_PATH):
        if file.endswith(".apk"):
            logger.info(f"{file} found at {APK_PATH}")
            abs_path = f"{APK_PATH}/{file}"
            apk = {
                "name":file,
                "path":abs_path
            }

            apk_paths.append(apk)
    

    for apk in apk_paths:
        try:
            if (len(APKTOOL_BINARY) > 0 and Path(APKTOOL_BINARY).exists()):
                apktool_bin_path = Path(APKTOOL_BINARY)
            else:
                logger.warning(f"apktool binary not found at {APKTOOL_BINARY}")
            
            if (len(APKTOOL_JAR) > 0 and Path(APKTOOL_JAR).exists()):
                apktool_jar_path = Path(APKTOOL_JAR)
            else:
                logger.warning(f"apktool jar not found at {APKTOOL_JAR}")
                

            output_dir = f"{OUTPUT_PATH}/{apk['name']}"
            if not os.path.exists(output_dir):
                logger.info(f"APKTool creating output directory at {output_dir}")
                os.makedirs(output_dir)

            logger.info(f"APKTool decompiling {apk['name']} to {output_dir}")
            cmd = f"{apktool_bin_path} d {apk['path']} -f -o {output_dir}"
            logger.info(f"Running {cmd}")
            subprocess.run(
                cmd, 
                shell=True, 
                check=True,  
                stderr=subprocess.STDOUT
            )
                    
        except Exception:
            logger.warning(f"APKTool failed to decompile {apk['name']}")



