import subprocess
import sys

REQUIRED_PACKAGES = [
    ("re", "re"),
    ("colorama", "colorama"),
    ("datetime", "datetime"),
    ("locale", "locale")
]

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mInstallazione completata: {package_name}")
    except subprocess.CalledProcessError:
        print(f"\033[37m[\033[31mERROR\033[37m] \033[0mErrore durante l'installazione di {package_name}.")

def check_and_install_packages():
    for module_name, package_name in REQUIRED_PACKAGES:
        try:
            __import__(module_name)
            print(f"\033[37m[\033[32mINFO\033[37m] \033[0mModulo trovato: {module_name}")
        except ImportError:
            print(f"\033[37m[\033[33mWARN\033[37m] \033[0mModulo non trovato: {module_name}. Tentativo di installazione...")
            install_package(package_name)

def main():
    print("\033[37m[\033[32mINFO\033[37m] \033[0mAvvio del controllo e installazione dei pacchetti richiesti...")
    check_and_install_packages()
    print("\033[37m[\033[32mINFO\033[37m] \033[0mTutti i pacchetti necessari sono stati verificati.")

if __name__ == "__main__":
    main()
