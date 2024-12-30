import os
import datetime

class TextLogger:
    def __init__(self, log_file = "file-io/projects/text_logger/log.txt"):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self.file = log_file
        
    def log(self, messageType, message):
        self.rotate_logs()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {messageType}: {message}\n"
        with open(self.file, "a") as file:
            file.write(log_entry)
        print(log_entry.strip())
    
    def info(self, message):
        self.log("INFO", message)
    
    def warning(self, message):
        self.log("WARNING", message)
        
    def error(self, message):
        self.log("ERROR", message)
    
    def rotate_logs(self, max_size = 1024 * 1024):
        if os.path.exists(self.file) and os.path.getsize(self.file) > max_size:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            rotated_file = f"{self.file}_{timestamp}"
            os.rename(self.file, rotated_file)
            print(f"Rotated log file to {rotated_file}")
