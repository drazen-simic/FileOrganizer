import argparse
import logging
from pathlib import Path
from fileorganizer.organizer import organize_files
from fileorganizer.backup import create_backup
from fileorganizer._watchdog import start_watchdog
from fileorganizer.utils import setup_logging

"""Program se pokreće tako da u terminal napišete: python main.py"""
"""Ako želite mijenjati defaultne argumente onda nakon 'python main.py' pišete
--directory putanja/do/direktorija --backup tar ili zip --log putanja/do/logfajla --watchdog (ako ne želite pokrenuti wathdog onda ne upisujete --watchdog)"""
def main():
    parser = argparse.ArgumentParser(description="Organize your Downloads folder.")
    parser.add_argument("--directory", type=str,default=r"C:\Users\Polaznik\Downloads", help="Path to the directory to organize.")
    parser.add_argument("--backup", type=str, choices=["zip", "tar"], default="zip", help="Create a backup before organizing (zip/tar).")
    parser.add_argument("--log", type=str, default=r"logs\\organizer.log", help="Path to the log file.")
    parser.add_argument("--watchdog", action="store_true",default=False, help="Enable watchdog for live monitoring.")
    args = parser.parse_args()

    # Set up logging
    setup_logging(args.log)


    # Validate the directory
    target_dir = Path(args.directory)
    if not target_dir.exists() or not target_dir.is_dir():
        logging.error(f"Invalid directory: {target_dir}")
        print(f"Error: '{target_dir}' is not a valid directory.")
        return

    # Create backup if requested
    if args.backup:
        create_backup(target_dir, args.backup)
        

    # Organize files
    organize_files(target_dir)

    # Start watchdog if enabled
    if args.watchdog:
        start_watchdog(target_dir)

if __name__ == "__main__":
    main()