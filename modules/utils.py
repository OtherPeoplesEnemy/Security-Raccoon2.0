import subprocess
import os

def is_dnf_installed(pkg):
    return subprocess.run(["rpm", "-q", pkg], stdout=subprocess.DEVNULL).returncode == 0

def is_pipx_installed(pkg_name):
    result = subprocess.run(["pipx", "list"], capture_output=True, text=True)
    return pkg_name.lower() in result.stdout.lower()

def is_pip_installed(pkg_name):
    result = subprocess.run(["pip3", "freeze"], capture_output=True, text=True)
    return pkg_name.lower() in result.stdout.lower()

def is_command_available(cmd):
    return subprocess.run(["which", cmd], stdout=subprocess.DEVNULL).returncode == 0

def tool_exists(path):
    return os.path.exists(path)
