import os
import platform
import pathlib
import ctypes


def get_expected_library_path():
    system = platform.system()
    lib_name = "libreltrans.so" if system == "Linux" else "libreltrans.dylib"
    project_root = pathlib.Path(__file__).resolve().parent
    return project_root / "build" / "lib" / lib_name


def run_diagnostics():
    print("Reltrans Build Diagnostics")
    print("-" * 30)

    system = platform.system()
    print(f"Operating System : {system}")

    headas = os.environ.get("HEADAS")
    print(f"HEADAS           : {headas}")

    lib_path = get_expected_library_path()
    print(f"Expected Library : {lib_path}")

    exists = lib_path.exists()
    print(f"Library Exists   : {exists}")

    if not exists:
        print("\nLibrary not found.")
        print("To build:")
        print("  1. Ensure HEASOFT is installed and sourced.")
        print("  2. Run `make` in the reltrans root directory.")
        return

    try:
        ctypes.cdll.LoadLibrary(str(lib_path))
        print("Library Loadable : YES")
    except OSError as e:
        print("Library Loadable : NO")
        print(f"Load Error       : {e}")


if __name__ == "__main__":
    run_diagnostics()
