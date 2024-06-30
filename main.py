# Allows neatened printing of report
from pprint import pprint

def main():
    # Path to the book's text file
    book_path = "books/frankenstein.txt"
    
    # Read the book text
    text = get_book_text(book_path)
    
    # Count words and characters
    num_words = get_num_words(text)
    
    num_characters = get_num_chars(text)

    character_report = [
        # {"character": "a", "occurences": 5000},
        # {"character": "b", "occurences": 5000}
    ]


    for char, count in num_characters.items():
        character_report.append({"character": char, "occurences": count})

    # Sorts characters into list from most often occuring to least often
    character_report.sort(key=lambda char_dict: char_dict["occurences"], reverse=True)
    
    #Print results
    print(f"---Begin report of {book_path}")
    print(f"The total number of words is {num_words}")
    pprint (character_report)
    print ("---End Report---")

def get_num_words(text):
    # Return word count
    return len(text.split())

def get_book_text(path):
    # Read and return file contents
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    # Convert text to lowercase and initialize dictionary
    lowered_words = text.lower()
    num_characters = {}
    
    # Count each character
    for char in lowered_words:
        #Verifies character is alphabetic
        if char.isalpha():
            if char in num_characters:
                num_characters[char] += 1
            else:
                num_characters[char] = 1
        
    return num_characters

# Run the main function
main()