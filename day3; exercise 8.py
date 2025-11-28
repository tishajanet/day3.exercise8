#Ask the user for two words and print them combined with a space
import sys
def main():
    first_word = input("Enter a word: ") #Tisha
    second_word = input("Enter a word: ")#Janet
    print(f"{first_word}",f"{second_word}") #Tisha Janet
    return 0
if __name__ == '__main__':
    sys.exit(main())
