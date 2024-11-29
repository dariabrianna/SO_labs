import signal
import os
import random
import string
import sys

# Handler for SIGUSR1
def handle_sigusr1(signum, frame):
    print("SIGUSR1 received")

# Handler for SIGUSR2
def handle_sigusr2(signum, frame):
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=100))
    print("SIGUSR2 received, printing 100 random ASCII characters:")
    print(random_chars)
    sys.exit(0)  # Terminate the program

# Register signal handlers
signal.signal(signal.SIGUSR1, handle_sigusr1)
signal.signal(signal.SIGUSR2, handle_sigusr2)

print(f"Process ID: {os.getpid()}")  # Display the process ID to send signals manually

# Keep the program running indefinitely to listen for signals
while True:
    signal.pause()  # Wait for signals
