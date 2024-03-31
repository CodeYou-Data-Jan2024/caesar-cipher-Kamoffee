# add your code here
# Define the caesar function
def caesar (text_low):
    new_sentence = "" 
    number_to_shift = 5
    alpha = "abcdefghijklmnopqrstuvwxyz"

    #Checking if the letter is in the sentence but with lowercase
    for letter in text_low.lower():
        # Check if the letters are in the alphabet
        if letter in alpha:
            index = alpha.find(letter)
            # Apply the shift of input
            new_index = (index + number_to_shift) % 26
            # Adding the new index to the sentence
            new_sentence += alpha[new_index]
        else:
         # keep non - characters from the sentence
            new_sentence += letter

    return new_sentence


# Creating a main function to coordinate caesar function
def main():
    # Asking for user input in our caesar variables
    text_low = input("Please enter a sentence: ")
    cypher = caesar(text_low)
    # Sentence that is going to be printed when the function will be called
    print("The encrypted sentence is: " + cypher)

# Calling the main function
main()