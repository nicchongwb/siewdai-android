import logging
import shutil
import tempfile
import zipfile
import platform
import os
import sys
from pathlib import Path
from urllib.request import (
    ProxyHandler,
    Request,
    build_opener,
    getproxies,
    urlretrieve
)

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)-15s - %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S')
logger = logging.getLogger(__name__)

def download_file(url, file_path):
    req = Request(url)
    system_proxies = getproxies()
    proxy_handler = ProxyHandler(system_proxies)
    opener = build_opener(proxy_handler)

    with opener.open(req) as response:
        if response.status == 200:
            file_size = int(response.headers.get('Content-Length', 0))
            downloaded = 0
            block_size = 8192  # 8KB

            with open(file_path, 'wb') as f:
                while True:
                    buffer = response.read(block_size)
                    if not buffer:
                        break
                    downloaded += len(buffer)
                    f.write(buffer)

                    # Print progress
                    if file_size > 0:
                        done = int(50 * downloaded / file_size)
                        fmt = (f'\r[{"#" * done}{"-" * (50 - done)}] '
                               f'{downloaded * 100 / file_size:.2f}%')
                        sys.stdout.write(fmt)
                        sys.stdout.flush()

            if downloaded != file_size:
                err = (f'Downloaded file size ({downloaded}) '
                       f'does not match expected size ({file_size})')
                raise Exception(err)

            return downloaded
        else:
            raise Exception(f'Failed to download file. Status code: {response.status}')

def is_jadx_installed(install_path):
    """
    Example of resources directory in root repository directory

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
    """
    if os.path.isdir(install_path + '/jadx'):
        logger.info('JADX is already installed at %s', install_path + '/jadx')
        return True
    return False
    

def install_jadx(install_path, version='1.5.1'):
    if is_jadx_installed(install_path):
        return
    
    """Install JADX dynamically"""
    try:
        url = ('https://github.com/skylot/jadx/releases/download/'
               f'v{version}/jadx-{version}.zip')
        jadx_dir = Path(install_path)  / 'jadx'
        extract_dir = jadx_dir

        if extract_dir.exists():
            logger.info('JADX is already installed at %s', extract_dir)
            return

        logger.info('Downloading JADX from %s', url)
        shutil.rmtree(jadx_dir, ignore_errors=True)

        with tempfile.NamedTemporaryFile(
                delete=False,
                mode='wb',
                suffix='.zip') as tmp_zip_file:

            downloaded_size = download_file(url, tmp_zip_file.name)
            logger.info('JADX download complete. File size: %d bytes', downloaded_size)

            # Extract the zip file
            logger.info('Extracting JADX to %s', extract_dir)
            extract_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(tmp_zip_file.name, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    zip_ref.extract(member, extract_dir)

        # Set execute permission
        set_rwxr_xr_x_permission_recursively(extract_dir)

        logger.info('JADX installed successfully')
    except Exception:
        logger.exception('Error during JADX installation')
    finally:
        if 'tmp_zip_file' in locals():
            Path(tmp_zip_file.name).unlink()


def install_apktool(install_path, version='2.11.1'):
    """Install APKTool dynamically"""
    try:
        url = ('https://github.com/iBotPeaches/Apktool/releases/download/'
               f'v{version}/apktool_{version}.jar')
        apktool_dir = Path(install_path)  / 'apktool'        
        apktool_path = apktool_dir / f"apktool_{version}.jar"

        if not apktool_dir.exists():
            os.makedirs(apktool_dir)
            
        if apktool_path.exists():
            logger.info('APKTool is already installed at %s', apktool_path)
            return

        logger.info('Downloading APKTool from %s', url)
        urlretrieve(url, apktool_path)
        logger.info('APKTool download complete.')

        # Set execute permission
        set_rwxr_xr_x_permission_recursively(apktool_dir)

        logger.info('APKTool installed successfully')
    except Exception:
        logger.exception('Error during APKTool installation')


def set_rwxr_xr_x_permission_recursively(directory_path):
    """Set execute permissions recursively."""
    if platform.system() == 'Windows':
        logger.info('Permission setting is skipped on non-Unix systems.')
        return

    logger.info('Setting execute permission for directory')
    directory_path.chmod(0o755)

    # Recursively set permissions for all files and
    # directories within the root directory
    for path in directory_path.rglob('*'):
        path.chmod(0o755)