def unencrypt(encrypted_message, key):
    alphabeth= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # key=3
    encrypted_message=encrypted_message.upper()
    original_message=''
    
    for encrypted_character in encrypted_message:
        new_unencrypted_character=''
        
        if encrypted_character in alphabeth:
            position=alphabeth.find(encrypted_character)-key
            if position<0:
                position=position+26
            new_unencrypted_character=new_unencrypted_character+alphabeth[position]
        else:
            new_unencrypted_character=encrypted_character
        original_message=original_message+ new_unencrypted_character
    # print(encrypted_message)
    return(original_message)
def hack_cc(encrypted_message):
    for key in range(1,26):
        print(unencrypt(encrypted_message, key))
hack_cc('L ORYH MHVXV')
