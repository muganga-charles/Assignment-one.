#NUMBER 4
#code that checks if a string has all the vowels
def invowel(word):
    #vowels="aeiouAEIOU"
    if 'a'in word and "e" in word and 'i' in word and 'u' in word and 'o' in word:#checks if the word has all lower case the vowels
        print("the word has every the vowels")
    elif 'A'in word and "E" in word and 'I' in word and 'U' in word and 'O' in word:#checks if the word has all upper case the vowels
        print("the word has every the vowels")
    else:
        print("the word has some vowels")
def main():
    word=input("Enter the word")#asks the user to enter the string
    invowel(word)
main()