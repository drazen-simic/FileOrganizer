from pathlib import Path  # Uvozi Path iz modula pathlib za rad s putanjama datoteka (nije korišten u ovom kodu)
import shutil  # Uvozi modul za operacije s datotekama i direktorijima (nije korišten u ovom kodu)
import json  # Uvozi modul za rad s JSON podacima
import logging  # Uvozi modul za logiranje poruka

# Funkcija za postavljanje logiranja
def setup_logging(log_file):
    logging.basicConfig(
        handlers=[  # Definira koji će se handleri koristiti za logiranje
        logging.StreamHandler(),  # Ispisuje poruke u konzolu
        logging.FileHandler(log_file),  # Ispisuje poruke u datoteku
    ],
        level=logging.INFO,  # Postavlja razinu logiranja na INFO (prikazuje INFO poruke i više ozbiljne)
        format="%(asctime)s - %(levelname)s - %(message)s"  # Postavlja format logova: datum, razina logiranja, poruka
    )
    logging.info("Logging setup complete.")  # Logira poruku da je postavljanje logiranja završeno

# Funkcija za učitavanje konfiguracije iz JSON datoteke
def load_config(config_file: str):
    """Load configuration from a JSON file."""  # Komentar koji objašnjava funkciju
    with open(config_file, 'r') as file:  # Otvara JSON datoteku u režimu za čitanje
        config = json.load(file)  # Učitava sadržaj JSON datoteke u Python objekt
    return config  # Vraća učitanu konfiguraciju
