import time
import threading

def countdown_timer(seconds, stop_event):
    print("Timer started!\n")
    while seconds > 0 and not stop_event.is_set():
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    if not stop_event.is_set():
        print("\nTimer finished!")
    else:
        print("\nTimer stopped!")

def stopwatch(stop_event):
    print("Stopwatch started!\n")
    start_time = time.time()
    try:
        while not stop_event.is_set():
            elapsed_time = time.time() - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds", end='\r')
            time.sleep(0.1)  # Update time every 0.1 second
    except KeyboardInterrupt:
        pass
    print("\nStopwatch stopped!")

def main():
    while True:
        print("Welcome to the Timer App!\n")
        print("1. Countdown Timer")
        print("2. Stopwatch")
        choice = input("Enter your choice (1 or 2): ")

        stop_event = threading.Event()

        if choice == '1':
            seconds = int(input("Enter the duration of the countdown timer in seconds: "))
            timer_thread = threading.Thread(target=countdown_timer, args=(seconds, stop_event))
            timer_thread.start()
        elif choice == '2':
            timer_thread = threading.Thread(target=stopwatch, args=(stop_event,))
            timer_thread.start()
        else:
            print("Invalid choice. Please enter '1' or '2'.")
            continue

        input("Press Enter to stop the timer...\n")
        stop_event.set()
        timer_thread.join()

        repeat = input("Do you want to run the timer again? (yes/no): ")
        if repeat.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
