# add your code here
# Define the caesar function
def caesar (sentence):
    encrypted_sentence = "" 
    encryption_key = 5
    alpha = "abcdefghijklmnopqrstuvwxyz"

    #Checking if the letter
    for letter in sentence.lower():
        # Check if the letters are in the alphabet
        if letter in alpha:
            index = alpha.find(letter)
            # Apply the shift of input
            new_index = (index + encryption_key) % 26
            # Adding the new index to the sentence
            encrypted_sentence += alpha[new_index]
        else:
         # keep non - characters from the sentence
            encrypted_sentence += letter

    return encrypted_sentence


# Creating a main function to coordinate caesar function
def main():
    # Asking for user input in our caesar variables
    text_low = input("Please enter a sentence: ")
    cypher = caesar(text_low)
    # Sentence that is going to be printed when the function will be called
    print("The encrypted sentence is: " + cypher)

# Calling the main function
main()