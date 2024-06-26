import psutil  # Import psutil module for CPU monitoring
import sys  # Import sys module for system-specific parameters and functions
from datetime import datetime  # Import datetime module for date and time manipulation

class cosmicCPUMonitor:
    def __init__(self, alert1, alert2):
        """
        Initialize cosmicCPUMonitor object with alert thresholds.

        Args:
        - alert1 (int): First alert threshold for CPU usage (%).
        - alert2 (int): Second alert threshold for CPU usage (%).
        """
        self.alert1 = alert1  # Initialize alert1 attribute
        self.alert2 = alert2  # Initialize alert2 attribute

    def healthify(self):
        """
        Monitor CPU usage and display alerts or status message dynamically.
        """
        print("Monitoring CPU usage... Press Ctrl+C to stop.")  # Print initial monitoring message
        try:
            while True:
                current_cpu_usage = psutil.cpu_percent(1.5)  # Get current CPU usage percentage
                
                if current_cpu_usage > self.alert2:
                    print("Alert!!! CPU usage exceeds threshold: 90%")  # Print alert message for > 90% usage
                elif current_cpu_usage > self.alert1:
                    print("Alert! CPU usage exceeds threshold: 85%")  # Print alert message for > 85% usage
                else:
                    print(f"Breathe in the cosmic vibes, your CPU is cruising at {current_cpu_usage}%", end='\r')  # Print normal status message with current CPU usage percentage
                    sys.stdout.flush()  # Flush the output to update immediately on the console

        except KeyboardInterrupt:
            print("\nUser has stopped the monitoring process!!")  # Handle keyboard interrupt to stop monitoring

        except Exception as e:
            print(f"\nAn error occurred: {e}")  # Handle any other exceptions during monitoring

# Main execution block
if __name__ == "__main__":
    warning_one = 85  # Define first alert threshold (% CPU usage)
    warning_two = 90  # Define second alert threshold (% CPU usage)

    start = cosmicCPUMonitor(warning_one, warning_two)  # Create an instance of cosmicCPUMonitor
    start.healthify()  # Start monitoring CPU usage
