# Timer App

This is a simple Python application that provides two main functionalities: a countdown timer and a stopwatch. The application uses threading to allow the user to stop the timer or stopwatch at any time by pressing Enter.

## Features

- **Countdown Timer**: Set a timer for a specific number of seconds. The timer will count down to zero, and you can stop it at any time.
- **Stopwatch**: Start a stopwatch to measure elapsed time. The stopwatch will keep running until you stop it.

## Requirements

- Python 3.x

## How to Use

1. **Run the Application**:
   ```sh
   python timer_app.py
   ```

2. **Choose a Function**:
   - Enter `1` to use the Countdown Timer.
   - Enter `2` to use the Stopwatch.

### Countdown Timer

- After selecting the Countdown Timer, enter the duration in seconds.
- The timer will start counting down and display the remaining time.
- Press Enter at any time to stop the timer.

### Stopwatch

- After selecting the Stopwatch, it will start and display the elapsed time.
- Press Enter at any time to stop the stopwatch.

## Repeat or Exit

- After stopping the timer or stopwatch, you can choose to run the timer again or exit the application.

## Example

### Running the Countdown Timer

```plaintext
Welcome to the Timer App!

1. Countdown Timer
2. Stopwatch
Enter your choice (1 or 2): 1
Enter the duration of the countdown timer in seconds: 10
Timer started!

Time remaining: 10 seconds
Time remaining: 9 seconds
Time remaining: 8 seconds
...
Press Enter to stop the timer...

Timer stopped!
Do you want to run the timer again? (yes/no): no
```

### Running the Stopwatch

```plaintext
Welcome to the Timer App!

1. Countdown Timer
2. Stopwatch
Enter your choice (1 or 2): 2
Stopwatch started!

Elapsed time: 1.23 seconds
Elapsed time: 1.33 seconds
Elapsed time: 1.43 seconds
...
Press Enter to stop the timer...

Stopwatch stopped!
Do you want to run the timer again? (yes/no): no
```

## Notes

- The application uses threading to allow the timer and stopwatch to run concurrently with the main program.
- The stop event is used to signal the threads to stop when the user presses Enter.

## License

This project is licensed under the MIT License.

This README file provides an overview of the Timer App, instructions on how to use it, and example usage scenarios.
