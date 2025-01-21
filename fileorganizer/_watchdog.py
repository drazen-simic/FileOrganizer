import logging  # Uvozi modul za logiranje poruka
import time  # Uvozi modul za rad s vremenom (spavanje u sekundi)
from watchdog.observers import Observer  # Uvozi Observer iz watchdog modula za praćenje promjena u direktorijima
from watchdog.events import FileSystemEventHandler  # Uvozi FileSystemEventHandler za rukovanje događajima u datotečnom sustavu
from fileorganizer.organizer import organize_files  # Uvozi funkciju za organiziranje datoteka iz modula fileorganizer

# Funkcija koja obrađuje događaje sustava datoteka i reorganizira datoteke u direktoriju
def handle_event(event, directory):
    """
    Rukuje događajima sustava datoteka i reorganizira datoteke u direktoriju.
    """
    if not event.is_directory:  # Provjerava je li događaj vezan uz direktorij ili datoteku
        if event.event_type in ("modified", "created"):  # Ako je događaj 'modificiran' ili 'kreiran'
            logging.info(f"Detected {event.event_type} event. Reorganizing files...")  # Logira tip događaja
            organize_files(directory)  # Poziva funkciju za reorganizaciju datoteka u direktoriju

# Funkcija koja pokreće praćenje direktorija za promjene pomoću watchdog biblioteke
def start_watchdog(directory):
    """
    Pokreće praćenje zadanog direktorija za promjene koristeći watchdog biblioteku.
    """
    logging.info(f"Starting watchdog for: {directory}")  # Logira početak praćenja direktorija

    # Kreira instancu promatrača (Observer)
    observer = Observer()

    # Kreira inline rukovatelja događajima
    def on_any_event(event):
        handle_event(event, directory)  # Poziva funkciju za obradu svakog događaja

    # Dodjeljuje handler funkciji za svaki događaj
    event_handler = FileSystemEventHandler()
    event_handler.on_any_event = on_any_event

    # Planira promatrača da koristi handler za zadanom putanjom i bez rekursivnog praćenja
    observer.schedule(event_handler, path=str(directory), recursive=False)
    observer.start()  # Pokreće promatrača

    try:
        logging.info("Watchdog is running. Press Ctrl+C to stop.")  # Logira poruku da je watchdog pokrenut
        while observer.is_alive():  # Petlja koja traje dok je promatrač aktivan (neblokirajuća)
            time.sleep(1)  # Spava 1 sekundu između provjera
    except KeyboardInterrupt:  # Ako se dogodi prekid od strane korisnika (Ctrl+C)
        observer.stop()  # Zaustavlja promatrača
        logging.info("Watchdog stopped.")  # Logira poruku da je watchdog zaustavljen
    observer.join()  # Čeka da promatrač završi čišćenje prije završetka programa
