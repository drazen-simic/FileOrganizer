import time  # Import the time module to add delays in the program
from watchdog.observers import Observer  # Import Observer to monitor the directory
from watchdog.events import FileSystemEventHandler  # Import FileSystemEventHandler to handle file system events

# Define a handler function to handle file system events
def log_event(event):
    if event.is_directory:
        return  # Ignore directory  events
    
    # Log event type and file path
    print(f"Event type: {event.event_type} | Path: {event.src_path}")

# Create an event handler by subclassing FileSystemEventHandler
handler = FileSystemEventHandler()

# Bind the 'on_modified', 'on_created', and 'on_deleted' events to the handler
#handler.on_modified = log_event
handler.on_created = log_event
#handler.on_deleted = log_event


# Specify the directory to monitor (change this path as needed)
path_to_watch = "."  # Use current directory

# Create an Observer instance
observer = Observer()
# Schedule the Observer to monitor the specified directory with the handler
observer.schedule(handler, path=path_to_watch, recursive=True)

# Start the Observer to begin monitoring
observer.start()

try:
    # Keep the program running to monitor changes
    while True:
        time.sleep(1)  # Sleep for 1 second to reduce CPU usage
except KeyboardInterrupt:
    # Stop the Observer if the program is interrupted (e.g., Ctrl+C)
    observer.stop()

# Wait for the Observer to shut down cleanly
observer.join()
