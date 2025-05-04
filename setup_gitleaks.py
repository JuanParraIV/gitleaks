import os
import shutil
import subprocess
import sys

GITLEAKS_CONFIG_SOURCE = os.path.expanduser(
    os.path.join(os.path.dirname(__file__), ".pre-commit-config.yaml")
)
GITLEAKS_CONFIG_TARGET = os.path.join(os.getcwd(), ".pre-commit-config.yaml")


def copy_gitleaks_config():
    if not os.path.exists(GITLEAKS_CONFIG_SOURCE):
        print(f"No se encontró el archivo de configuración en {GITLEAKS_CONFIG_SOURCE}")
        sys.exit(1)
    if os.path.abspath(GITLEAKS_CONFIG_SOURCE) == os.path.abspath(
        GITLEAKS_CONFIG_TARGET
    ):
        print(
            "El archivo de configuración ya está en la ubicación de destino. No se realiza copia."
        )
        return
    shutil.copy(GITLEAKS_CONFIG_SOURCE, GITLEAKS_CONFIG_TARGET)
    print(f"Archivo .pre-commit-config.yaml copiado a {GITLEAKS_CONFIG_TARGET}")


def install_pre_commit():
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pre-commit"], check=True
        )
        print("pre-commit instalado correctamente.")
    except subprocess.CalledProcessError:
        print("Error instalando pre-commit.")
        sys.exit(1)


def run_pre_commit_install():
    try:
        subprocess.run(["pre-commit", "install"], check=True)
        print("pre-commit hook instalado correctamente.")
    except subprocess.CalledProcessError:
        print("Error ejecutando 'pre-commit install'.")
        sys.exit(1)


def main():
    copy_gitleaks_config()
    install_pre_commit()
    run_pre_commit_install()


if __name__ == "__main__":
    main()
