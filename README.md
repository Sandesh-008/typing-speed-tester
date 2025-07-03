# Typing Speed Tester – Python CLI Project

A simple and effective Python command-line application that measures your typing speed and accuracy. Whether you're practicing for a job test or just want to improve your typing skills, this project gives instant feedback in a clean interface.

---

## Features

- Random sentence prompt from a curated list
- Real-time speed calculation in **Words Per Minute (WPM)**
- Accuracy tracking based on word-by-word comparison
- Option to retry with a different prompt
- Graceful handling of keyboard interruptions

---

## Concepts & Modules Used

- Python **functions**
- String **manipulation and comparison**
- **`time`** module for tracking performance
- **Input/output** handling with clean formatting
- Basic **error handling**

---

## Requirements
---

- Python 3.6 or higher
- No external libraries needed

---

## How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/YourUsername/typing-speed-tester.git

   ---

2. **Navigate to the folder:
```
cd typing-speed-tester

```
3. **Run the application:
```
python main.py

````
---

## Sample Output

*-----Welcome to the Python Typing Speed Tester!-----*

(Press ENTER to begin the test...)

Type the following sentence:

Artificial Intelligence is transforming the world.

(Press ENTER when you're ready to start typing...)

Start Typing : Artifical Intelligence is transformng the word.

*----- Test Results -----*
Time Taken: 12.37 seconds
Words Per Minute (WPM): 38.76
Accuracy: 60.0%

Thanks for using the Typing Speed Tester. Keep practicing!
---

## Author

**Sandesh Salokhe**  
GitHub: [@Sandesh-008](https://github.com/Sandesh-008)

---

##License

This project is open source and available under the MIT License.

---

## Notes

- Works across all major platforms (Windows, macOS, Linux)
- You can customize the sentence list in the `Sentences[]` variable
- For color output, you can reintroduce ANSI escape codes as needed
