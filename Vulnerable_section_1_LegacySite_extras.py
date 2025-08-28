         return card_file_data
     except (json.JSONDecodeError, UnicodeDecodeError):
         pass
    with open('Temp/binary', 'wb') as card_file:
         card_file.write(card_file_data)
     # KG: Are you sure you want the user to control that input?
    print(f"running: {CARD_PARSER} 2 Temp/binary > Temp/binary;")
    ret_val = system(f"{CARD_PARSER} 2 Temp/binary > Temp/binary;")
     if ret_val != 0:
         return card_file_data
    with open("Temp/binary", 'rb') as tmp_file:
         return tmp_file.read()