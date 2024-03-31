# add your code here
# Define a function
def caesar (number_to_shift, text_low): 
    # Checking to see if the user input is decimal and in range
    if not number_to_shift.isdecimal() or not (0 <= int(number_to_shift) <= 25) :
        print("You need to enter a number between 0 and 25!") 
    else:
        # set our variables
        number_to_shift = int(number_to_shift)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        new_alpha = list(alpha)
        new_list = []

        for letters in text_low.lower():
            # Check if the letters are in the alphabet
            if letters in alpha:
                index = alpha.find(letters.lower())
            # Apply the shift of input
                new_index = (index + number_to_shift) %  26
                new_letters = new_alpha[new_index]
                new_list.append(new_letters)
            else:
                # keep non - characters from the sentence
                new_list.append(letters)

        new_text = ''.join(new_list)
        return new_text

# Creating a main function to coordinate caesar function
def main():
    # Asking for user input in our caesar variables
    number_to_shift = input("Please enter a number of places to shift:") 
    text_low = input("Please enter a sentence: ")
    cypher = caesar(number_to_shift, text_low)
    print(cypher)


main()