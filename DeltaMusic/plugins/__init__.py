import glob
import os

def __list_all_modules():
    work_dir = os.path.dirname(__file__)
    mod_paths = glob.glob(os.path.join(work_dir, "*.py"))  

    all_modules = [
        os.path.basename(f)[:-3]  
        for f in mod_paths
        if os.path.isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules

ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
