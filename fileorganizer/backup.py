import logging  # Uvozi modul za logiranje poruka
import shutil   # Uvozi modul za operacije s datotekama i direktorijima (nije korišten u ovom kodu)
from pathlib import Path  # Uvozi Path iz modula pathlib za rad s putanjama datoteka
import zipfile  # Uvozi modul za rad sa ZIP arhivama
import tarfile  # Uvozi modul za rad s TAR arhivama

# Funkcija za stvaranje sigurnosne kopije (backup) direktorija
def create_backup(directory, backup_type):
    # Definira naziv sigurnosne kopije na temelju imena direktorija
    backup_name = directory.parent / f"{directory.name}_backup"
    try:
        # Ako je tip sigurnosne kopije 'zip', poziva funkciju za stvaranje zip arhive
        if backup_type == "zip":
            zip_backup(directory, backup_name)
            
        # Ako je tip sigurnosne kopije 'tar', poziva funkciju za stvaranje tar arhive
        elif backup_type == "tar":
            tar_backup(directory, backup_name)
            
    # Ako dođe do pogreške tijekom stvaranja sigurnosne kopije, bilježi pogrešku
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")

# Funkcija za stvaranje ZIP sigurnosne kopije
def zip_backup(directory, backup_name):
    # Otvara novi ZIP arhivu za pisanje
    with zipfile.ZipFile(f"{backup_name}.zip", "w") as zipf:
        # Iterira kroz sve datoteke i poddirektorije u direktoriju
        for file in directory.rglob("*"):
            # Dodaje svaku datoteku u ZIP arhivu, relativno prema početnom direktoriju
            zipf.write(file, file.relative_to(directory))
    # Logira informaciju o uspješno stvorenoj ZIP sigurnosnoj kopiji
    logging.info(f"Backup created: {backup_name}.zip")
    
    
# Funkcija za stvaranje TAR.GZ sigurnosne kopije
def tar_backup(directory, backup_name):
    # Otvara novu TAR.GZ arhivu za pisanje (kompresija u GZ formatu)
    with tarfile.open(f"{backup_name}.tar.gz", "w:gz") as tar:
        # Dodaje cijeli direktorij u TAR arhivu
        tar.add(directory, arcname=directory.name)
    # Logira informaciju o uspješno stvorenoj TAR.GZ sigurnosnoj kopiji
    logging.info(f"Backup created: {backup_name}.tar.gz")
