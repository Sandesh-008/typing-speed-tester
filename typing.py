# Typing Speed Tester

import time
import random
import textwrap

# Predefined sample sentences
Sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a widely used high-level programming language.",
    "Typing speed is measured in words per minute.",
    "Practice makes a person perfect in every skill.",
    "Artificial Intelligence is transforming the world."
]

def get_random_text():
    """Returns a random sentence from the list."""
    return random.choice(Sentences)

def calculate_wpm(start_time, end_time, typed_text):
    """Calculates words per minute."""
    time_taken = end_time - start_time
    word_count = len(typed_text.split())
    minutes = time_taken / 60
    wpm = word_count / minutes if minutes > 0 else 0
    return round(wpm, 2), round(time_taken, 2)

def calculate_accuracy(original, typed):
    """Compares original and typed texts and calculates accuracy."""
    original_words = original.split()
    typed_words = typed.split()
    correct = 0

    for orig_word, typed_word in zip(original_words, typed_words):
        if orig_word == typed_word:
            correct += 1

    accuracy = (correct / len(original_words)) * 100 if original_words else 0
    return round(accuracy, 2)

def run_typing_test():
    print("\n*-----Welcome to the Python Typing Speed Tester!-----*\n")
    input("(Press ENTER to begin the test...)\n")

    text_to_type = get_random_text()
    print("Type the following sentence:")
    print("\n" + textwrap.fill(text_to_type, width=70) + "\n")

    input("(Press ENTER when you're ready to start typing...)\n")

    start_time = time.time()
    try:
        typed_text = input("Start Typing : ")
    except KeyboardInterrupt:
        print("\nTest interrupted. Exiting...")
        return
    
    
    end_time = time.time()

    wpm, time_taken = calculate_wpm(start_time, end_time, typed_text)
    accuracy = calculate_accuracy(text_to_type, typed_text)

    print("\n*----- Test Results -----*")
    print(f"Time Taken: {time_taken} seconds")
    print(f"Words Per Minute (WPM): {wpm}")
    print(f"Accuracy: {accuracy}%")

    print("\nThanks for using the Typing Speed Tester. Keep practicing!\n")

if __name__ == "__main__":
    run_typing_test()
