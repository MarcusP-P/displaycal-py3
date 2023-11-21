from sysconfig import get_platform;
from os.path import join;
import shutil;
import sys;

prefix="build"

if sys.version_info[:2] < (3, 10):
    base_dir="lib."+get_platform()+"-"+sys.version_info[0]+"."+sys.version_info[1]
else:
    base_dir="lib."+get_platform()+"-"+sys.implementation.cache_tag

lib64Path=join("DisplayCAL", "lib64")

if sys.platform=="darwin":
    libFile="RealDisplaySizeMM."+sys.implementation.cache_tag+"-"+sys.platform+".so"
else:
    lib64Path=join(lib64Path, "python"+sys.version_info[0]+sys.version_info[1])
    libFile="RealDisplaySizeMM."+sys.implementation.cache_tag+sys.platform+"-x86_64-linux-gnu.so"

source=join (prefix, base_dir, lib64Path, libFile)

shutil.copy(source, lib64Path)