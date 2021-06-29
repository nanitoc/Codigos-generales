alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again=True


def caesar(word,shift):
    global New_word
    New_word=''
    for x in word:
        new_index=alphabet.index(x)
        if direction=='encode':
            New_word+=alphabet[new_index+shift]
            
        else:
            New_word+=alphabet[new_index-shift]
            # New_word.append(alphabet[new_index-shift])

while again==True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift)

    if direction=='encode':
        print(f'here is the encode result: {New_word}\n')
    else:
        print(f'here is the decode result: {New_word}\n') 
    
    if input("Type 'yes' if want to go again, Otherwise type'no': \n")=='yes':
        again=True
    else:
        again=False

print('Thank you so much')
