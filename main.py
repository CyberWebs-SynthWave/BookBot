from collections import Counter



def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text=text.lower()
    return dict(Counter(char for char in text if char.isalpha()))

def main():


    book_file = 'books/frankenstein.txt'
    
    with open(book_file, 'r') as f:
        file_content = f.read()
        print(file_content)

        print(f"--- Begin report of {book_file} ---")

        word_count = count_words(file_content)
        print(f"This book has {word_count} words.")

        char_count = count_characters(file_content)
        print("Charcter counts", char_count)
        
        report(book_file,word_count,char_count)


def report(book_file, word_count,char_count):

    sorted_char_count =  sorted(char_count.items(), key=lambda item:item[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"The '{char}' characters was found {count} times")


    print("--- End Report ---")    


#call main
if __name__ == "__main__":
    main()