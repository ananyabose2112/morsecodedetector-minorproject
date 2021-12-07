# Define an empty dictionary 'morse_dict'
morse_dict = {}
# Convert the 2 lists into a dictionary using a tuple
zipped_char_code = zip(character, code)
morse_dict = dict(zipped_char_code)
# Print the dictionary 'morse_dict' on the terminal line by line
for key, value in morse_dict.items():
    print(key, value)
# reverse the previous dict as it's easier to access the keys
zipped_code_char = zip(code,character)
rev_morse_dict = dict(list(zipped_code_char))
# initiating a while loop
while True:
    # empty list to store original message
    ori_msg = [] 
    # empty list to store decoded message
    dec_msg = []
    
    # prompt the user to input morse code
    input_msg = input ("Please enter any Morse Code sequence for decoding. Leave blank to quit. ")
    # append input_msg (string) to ori_msg (string)
    ori_msg.append(input_msg)
    # split each morse code by '*'
    new_msg = input_msg.split("*")
    
    # printing out the original message
    for line in ori_msg: # to print original message without the []
        print("Original message: " + line + "\n")
    
    # loop through each morse code representation
    for j in range (0,len(new_msg)):
        # get the alphanumeric alphabet based on the dict keys and append to dec_msg
        if new_msg[j] in rev_morse_dict.keys():
            dec_msg.append(rev_morse_dict[new_msg[j]])
    
    # printing out the decoded message
    print ("Decoded Message is: " + ''.join(dec_msg) + "\n")
    # end the infinite while loop
    break
# counter to do error check
    i = 0
    # proceed if user enters something
    if (len(input_msg)!=0):
        # while loop to check if only 0, 1 or * has been keyed in
        while (i<len(input_msg)):
            if input_msg[i] == "0" or input_msg[i] == "1" or input_msg[i] == "*":
                i+=1
            else:
                # if invalid chars found, print error message
                print ("Error input, Morse Code sequence should only consists of 0 and 1, with a * between subsequence")
               # break the error check once one error has been found
                break
# loop through each morse code representation
            for j in range (0,len(new_msg)):
                # get the alphanumeric alphabet based on the dict keys and append to dec_msg
                if new_msg[j] in rev_morse_dict.keys():
                    dec_msg.append(rev_morse_dict[new_msg[j]])
                # if morse code representation not found in original list, append input to err_msg
                else:
                    err_msg.append(new_msg[j])
            
            # to print error message only when necessary
            if len(err_msg) != 0:  
                for line in err_msg: 
                    print(line + " has no known morse translation")