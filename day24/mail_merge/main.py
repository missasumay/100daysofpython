#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("day24\\mail_merge\\Input\\Letters\\starting_letter.txt", mode="r+") as starting_letter:
    example_letter = starting_letter.read()

    with open("day24\\mail_merge\\Input\\Names\\invited_names.txt", mode="r+") as list_of_names:

        names = []

        for name in list_of_names:
            formatted_name = name.strip()
            names.append(formatted_name)

    for name in names:
        replaced_name = example_letter.replace("[name]", name)
        with open(f"day24\\mail_merge\\Output\\ReadyToSend\\{name}.txt", mode="w") as letter:
            letter.write(replaced_name)







    

