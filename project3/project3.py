import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    print("Time's up!")

# Set the countdown duration in seconds
duration = 10

# Start the countdown
countdown(duration)


