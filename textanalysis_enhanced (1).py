import os

"""
Program: textanalysis_enhanced.py
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
The enhancements included in this version are:
1. Added error handling for file access issues, such as missing files or permission errors,
   to prevent crashes and provide user-friendly feedback.
2. Used the 'with' statement for file operations to ensure proper resource management
   and automatic file closure, even in the event of an error.
3. Used f-strings for output formatting to enhance readability and maintainability
   of the code, making it easier to understand and modify the output format in the future.
4. Restructured the script to use helper functions placed before main(),
   with main() executed conditionally.
"""


def getFileText(fileName):
    """Opens and returns the text from the given file name.
    Returns None if the file is not found or not accessible."""
    if not os.path.exists(fileName):
        print(f"Error: The file '{fileName}' was not found or is not accessible.")
        print(os.getcwd())  # Show current directory for debugging
        return None
    with open(fileName, 'r') as inputFile:
        text = inputFile.read()
    return text


def countSentences(text):
    """Counts and returns the number of sentences in the text."""
    sentence_endings = ".?;:!"
    sentences = 0
    for char in text:
        if char in sentence_endings:
            sentences += 1
    return sentences


def countWords(text):
    """Counts and returns the number of words in the text."""
    wordList = text.split()
    return len(wordList)


def countSyllables(text):
    """Counts and returns the number of syllables in the text."""
    wordList = text.split()
    syllables = 0
    vowels = "aeiouAEIOU"
    for word in wordList:
        vowelSeen = False
        for character in word:
            if not vowelSeen and character in vowels:
                syllables += 1
                vowelSeen = True
            elif character not in vowels:
                vowelSeen = False

        # Adjustments for silent 'e', 'es', 'ed'
        for ending in ['es', 'ed', 'e']:
            if word.endswith(ending):
                syllables -= 1
                break
        if word.endswith('le'):
            syllables += 1

    return syllables


def main():
    fileName = input("Enter the file name: ")

    text = getFileText(fileName)
    if text is None:
        return

    sentences = countSentences(text)
    words = countWords(text)
    syllables = countSyllables(text)

    # Compute the Flesch Index and Grade Level
    index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    level = int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))

    # Output the results using f-strings
    print("-" * 30)
    print(f"The Flesch Index is: {index:.2f}")
    print(f"The Grade Level Equivalent is: {level}")
    print("-" * 30)
    print(f"Summary Statistics:")
    print(f" - {sentences} sentences")
    print(f" - {words} words")
    print(f" - {syllables} syllables")


if __name__ == "__main__":
    main()
