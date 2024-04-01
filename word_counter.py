def count_words_from_file(file_path):
    # Open the file in read mode and read its contents
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Convert text to lowercase to count all variations of a word the same

    # Split the text into words based on spaces
    words = text.split()

    # Create a dictionary to keep track of word counts
    word_count = {}

    # Count the occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort the dictionary by the count, descending
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted word counts
    for word, count in sorted_words:
        print(word, ":", count)

# Replace 'path/to/your/file.txt' with the path to the file you want to analyze e.g. '/Users/ayo/Documents/adaptavist/example.txt'
file_path = 'path/to/your/file.txt'
count_words_from_file(file_path)
