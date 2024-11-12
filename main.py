import os
import platform
import tempfile
import requests
import time
import ctypes
import screeninfo
import argparse
import json
import subprocess
import sys

# Funzione per ottenere il percorso del file di configurazione in base al sistema operativo
def get_config_path():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.getenv('APPDATA'), "wallpaper_changer_config.json")
    elif system == "Darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support", "wallpaper_changer_config.json")
    elif system == "Linux":
        return os.path.join(os.path.expanduser("~"), ".config", "wallpaper_changer_config.json")
    else:
        raise ValueError("Sistema operativo non supportato.")

CONFIG_PATH = get_config_path()

# Funzione per ottenere la risoluzione dello schermo principale
def get_screen_resolution():
    screen = screeninfo.get_monitors()[0]
    return screen.width, screen.height

# Funzione per scaricare l'immagine da un URL e salvarla nel percorso specificato
def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        return True
    return False

# Funzioni per cambiare lo sfondo in base al sistema operativo
def change_wallpaper_windows(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def change_wallpaper_mac(image_path):
    script = f"""osascript -e 'tell application "System Events" to set picture of every desktop to "{image_path}"'"""
    os.system(script)

def change_wallpaper_linux(image_path):
    command = f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}"
    os.system(command)

# Funzione per salvare la configurazione dell'applicazione in un file JSON
def save_config(config_data):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as config_file:
        json.dump(config_data, config_file)

# Funzione per caricare la configurazione da file JSON o creare una configurazione predefinita
def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as config_file:
            return json.load(config_file)
    return {
        "url": "https://picsum.photos/{screen_width}/{screen_height}",
        "tempo_intervalo": 10
    }

# Funzione principale per scaricare e impostare lo sfondo
def set_random_wallpaper(url_template, interval_seconds):
    while True:
        # Ottiene le dimensioni dello schermo
        width, height = get_screen_resolution()
        image_url = url_template.format(screen_width=width, screen_height=height)
        
        # Scarica l'immagine in un file temporaneo
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_image_file:
            image_path = temp_image_file.name

        # Scarica e imposta l'immagine come sfondo
        if download_image(image_url, image_path):
            print("Immagine scaricata con successo:", image_path)
        else:
            print("Errore nel download dell'immagine.")
            return

        # Cambia lo sfondo in base al sistema operativo
        current_os = platform.system()
        if current_os == "Windows":
            change_wallpaper_windows(image_path)
        elif current_os == "Darwin":
            change_wallpaper_mac(image_path)
        elif current_os == "Linux":
            change_wallpaper_linux(image_path)
        else:
            print(f"Non supportato per il sistema operativo: {current_os}")
            return

        # Attende il tempo specificato prima di cambiare nuovamente lo sfondo
        time.sleep(interval_seconds)

# Funzione per configurare o rimuovere l'avvio automatico dell'applicazione
def setup_autostart(enable=True):
    current_os = platform.system()
    script_path = os.path.abspath(sys.argv[0])

    if current_os == "Windows":
        startup_path = os.path.join(os.getenv('APPDATA'), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        shortcut_path = os.path.join(startup_path, "wallpaper_changer.lnk")
        if enable:
            if not os.path.exists(shortcut_path):
                subprocess.run(['powershell', '-Command', 
                                f"$s=(New-Object -COM WScript.Shell).CreateShortcut('{shortcut_path}');"
                                f"$s.TargetPath='{script_path}';$s.Save()"])
                print("Avvio automatico configurato per Windows.")
        else:
            if os.path.exists(shortcut_path):
                os.remove(shortcut_path)
                print("Avvio automatico rimosso per Windows.")

    elif current_os == "Darwin":  # macOS
        plist_path = os.path.expanduser("~/Library/LaunchAgents/com.user.wallpaperchanger.plist")
        if enable:
            plist_content = f"""
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
            <plist version="1.0">
            <dict>
                <key>Label</key>
                <string>com.user.wallpaperchanger</string>
                <key>ProgramArguments</key>
                <array>
                    <string>{script_path}</string>
                </array>
                <key>RunAtLoad</key>
                <true/>
            </dict>
            </plist>
            """
            with open(plist_path, "w") as plist_file:
                plist_file.write(plist_content)
            subprocess.run(["launchctl", "load", plist_path])
            print("Avvio automatico configurato per macOS.")
        else:
            if os.path.exists(plist_path):
                subprocess.run(["launchctl", "unload", plist_path])
                os.remove(plist_path)
                print("Avvio automatico rimosso per macOS.")

    elif current_os == "Linux":
        autostart_dir = os.path.expanduser("~/.config/autostart")
        os.makedirs(autostart_dir, exist_ok=True)
        desktop_path = os.path.join(autostart_dir, "wallpaper_changer.desktop")
        if enable:
            desktop_entry = f"""
            [Desktop Entry]
            Type=Application
            Exec=python3 {script_path}
            Hidden=false
            NoDisplay=false
            X-GNOME-Autostart-enabled=true
            Name=WallpaperChanger
            """
            with open(desktop_path, "w") as desktop_file:
                desktop_file.write(desktop_entry)
            print("Avvio automatico configurato per Linux.")
        else:
            if os.path.exists(desktop_path):
                os.remove(desktop_path)
                print("Avvio automatico rimosso per Linux.")

# Funzione principale
def main():
    # Carica la configurazione
    config_data = load_config()
    
    # Parser degli argomenti della riga di comando
    parser = argparse.ArgumentParser(description="Cambia lo sfondo periodicamente con un'immagine da URL.")
    parser.add_argument("-u", "--url", type=str, default=config_data["url"], 
                        help="URL dell'immagine da usare come sfondo (con supporto per {screen_width} e {screen_height})")
    parser.add_argument("-t", "--tempo_intervalo", type=int, default=config_data["tempo_intervalo"], 
                        help="Intervallo di tempo (in secondi) tra i cambi di sfondo")
    parser.add_argument("--setup-autostart", action="store_true", help="Configura l'avvio automatico")
    parser.add_argument("--remove-autostart", action="store_true", help="Rimuove l'avvio automatico")
    
    # Interpreta gli argomenti e salva le impostazioni aggiornate
    args = parser.parse_args()
    config_data["url"] = args.url
    config_data["tempo_intervalo"] = args.tempo_intervalo
    save_config(config_data)

    # Configura o rimuove l'avvio automatico in base agli argomenti
    if args.setup_autostart:
        setup_autostart(enable=True)
    elif args.remove_autostart:
        setup_autostart(enable=False)
    else:
        set_random_wallpaper(args.url, args.tempo_intervalo)

if __name__ == "__main__":
    main()
