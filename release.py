from cx_Freeze import setup, Executable

build_exe_options = {
	"include_files":["data\\dirs.lgz"]
}

setup(
	name="Logizar CLI",
	version="0.0.1",
	description="Terminal de controle Logizar",
	build_exe=build_exe_options,
	executables= [Executable("lgz_debug.py",targetName="lgz0.exe")]
)