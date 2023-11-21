from sysconfig import get_platform;
from os.path import join;
import shutil;
import sys;

prefix="build"

if sys.version_info[:2] < (3, 10):
    base_dir=f"lib.{get_platform()}-{sys.version_info[0]}.{+sys.version_info[1]}"
else:
    base_dir=f"lib.{get_platform()}-{sys.implementation.cache_tag}"

lib64Path=join("DisplayCAL", "lib64")

if sys.platform=="darwin":
    libFile=f"RealDisplaySizeMM.{sys.implementation.cache_tag}-{sys.platform}.so"
else:
    lib64Path=join(lib64Path, f"python{sys.version_info[0]}{sys.version_info[1])"
    libFile=f"RealDisplaySizeMM.{sys.implementation.cache_tag+sys.platform}-x86_64-linux-gnu.so"


source=join (prefix, base_dir, lib64Path, libFile)

print(f"Copying {source} to {dest}")
shutil.copy(source, lib64Path)