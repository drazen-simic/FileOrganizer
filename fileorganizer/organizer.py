# Uvoz potrebnih modula za logiranje, manipulaciju putanjama datoteka, obradu datuma i operacije s datotekama
import logging
from pathlib import Path
from datetime import datetime
import os
import shutil

# Rječnik koji definira uobičajene ekstenzije datoteka i njihove odgovarajuće kategorije (npr. Slike, Dokumenti, itd.)
COMMON_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
    "Executables": [".exe", ".bat", ".sh"],
    "Prezentacije": [".ppt", ".pptx"],
    "Others": []  # Kategorija za datoteke koje ne pripadaju nijednoj od navedenih kategorija
}

# Lista za praćenje najnovijih preuzetih datoteka (trenutno nije korištena u kodu)
LATEST_DOWNLOADES = []

# Funkcija koja određuje kategoriju datoteke na temelju njezine ekstenzije
def get_file_category(extension):
    # Iterira kroz svaku kategoriju i povezane ekstenzije
    for category, extensions in COMMON_EXTENSIONS.items():
        # Ako ekstenzija datoteke odgovara jednoj od ekstenzija u kategoriji, vraća naziv kategorije
        if extension.lower() in extensions:
            return category
    # Ako nijedna kategorija nije odgovarala, vraća kategoriju 'Others'
    return "Others"

# Funkcija koja organizira datoteke unutar određenog direktorija
def organize_files(directory):
    # Logira početak procesa organiziranja datoteka
    logging.info(f"Starting organization for: {directory}")
    try:
        # Prolazi kroz sve stavke u zadanim direktorijima
        for item in directory.iterdir():
            # Ako je stavka datoteka (ne direktorij ili simbolička poveznica)
            if item.is_file():
                # Dobiva kategoriju datoteke na temelju njezine ekstenzije
                category = get_file_category(item.suffix)
                # Stvara direktorij za kategoriju ako već ne postoji
                category_dir = directory / category
                category_dir.mkdir(exist_ok=True)
                
                # Dohvaća vrijeme stvaranja datoteke
                creation_time = item.stat().st_ctime
                # Pretvara vrijeme stvaranja u datetime objekt
                creation_date = datetime.fromtimestamp(creation_time)
                # Stvara direktorij za godinu unutar direktorija kategorije
                year_dir = category_dir / str(creation_date.year)
                # Stvara direktorij za mjesec unutar direktorija godine
                month_dir = year_dir / creation_date.strftime("%B")
                # Stvara direktorij za mjesec ako već ne postoji
                month_dir.mkdir(parents=True, exist_ok=True)

                # Premješta datoteku u odgovarajući direktorij za mjesec
                item.rename(month_dir / item.name)
                # Logira premještanje datoteke
                logging.info(f"Moved: {item} -> {month_dir / item.name}")
    # Hvata i logira eventualne pogreške tijekom procesa
    except Exception as e:
        logging.error(f"Error during organization: {e}")

        
# def copy_newest_files(source_dir, destination_dir, num_files=10):
#     """
#     Copies the newest files from the source directory to the destination directory.

#     :param source_dir: Path to the directory containing files to copy.
#     :param destination_dir: Path to the directory where files will be copied.
#     :param num_files: Number of newest files to copy.
#     """
#     source_path = Path(source_dir)
#     destination_path = Path(destination_dir)

#     # Ensure the destination directory exists
#     destination_path.mkdir(parents=True, exist_ok=True)

#     # Get all files in the directory, sorted by creation time (newest first)
#     files = [
#         f for f in source_path.iterdir()
#         if f.is_file()
#     ]
#     files.sort(key=lambda f: f.stat().st_birthtime, reverse=True)  # Sort by creation time (newest first)

#     # Take the newest files
#     newest_files = files[:num_files]

#     for file in newest_files:
#         # Define the path for the copied file in the destination directory
#         destination_file = destination_path / file.name
        
#         # If the file already exists in the destination, skip copying
#         if destination_file.exists():
#             continue

#         try:
#             # Copy the file to the destination directory
#             shutil.copy2(file, destination_file)
#             print(f"Copied: {file.name} -> {destination_file}")
#         except Exception as e:
#             print(f"Failed to copy {file.name}: {e}")
