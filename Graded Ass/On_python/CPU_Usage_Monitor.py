import psutil
import time

# Set CPU usage threshold for alerting, Default threshold is set to 80% & Check interval is set to 1 second
CPU_THRESHOLD = 80  # percent
CHECK_INTERVAL = 1  # seconds

def monitor_cpu(threshold=CPU_THRESHOLD, interval=CHECK_INTERVAL):
    """
    Continuously monitor CPU usage.
    Display alert if usage exceeds the given threshold.
    Handles keyboard interruption and unexpected errors.
    """
    print(" Monitoring CPU usage... (Press Ctrl+C to stop)\n")
    
    try:
        while True:
            # psutil.cpu_percent(interval) waits for the interval and returns % usage
            cpu_usage = psutil.cpu_percent(interval=interval)

            # Check if CPU usage exceeds the threshold, alert the user if it does
            if cpu_usage > threshold:
                print(f" Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f" CPU usage is normal: {cpu_usage}%")
                
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("\n Monitoring stopped by user.")
    
    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()