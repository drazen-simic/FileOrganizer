from fileorganizer.utils import load_config
import logging
from pathlib import Path
from fileorganizer.organizer import organize_files
from fileorganizer.backup import create_backup
from fileorganizer._watchdog import start_watchdog
from fileorganizer.utils import setup_logging
import sys
def main():
    # Load configuration
    config = load_config(r'config\config.json')
    
    # Access specific settings
    target_dir = Path(config['directories']['downloads'])
    log_file = config['logging']['log_file']
    
    # Set up logging
    setup_logging(log_file)
    
    # Validate the directory
    if not target_dir.exists() or not target_dir.is_dir():
        logging.error(f"Invalid directory: {target_dir}")
        return

    # Create backup if enabled
    if config['backup']['enabled']:
        #stavljamo target_dir zato što u create_backup funkciji prvi redak uzima parent od 
        #danog argumenta, u mom slucaju User/Polaznik/Downoloads parent je User/Polaznik/
        # i na tu putanju dodaju 'directory.name + _backup' što je u mom slučaju Downloads_backup.
        create_backup(target_dir, config['backup']['type'])
    

    # Organize files
    organize_files(target_dir)

    # Start watchdog if enabled
    if config['watchdog']['enabled']:
        start_watchdog(target_dir)

if __name__ == "__main__":
    main()
  

        
        
