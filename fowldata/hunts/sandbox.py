def decode(message_file):
    word_map = {}
    message_file = "message_file.txt"
    with open(message_file, 'r') as file:
        for line in file:
            key, value = line.split(" ")
            word_map[int(key)] = value.rstrip('\n') 
    number = len(word_map)
    word_selection_indicies = pyramid_cipher(number)
    print(f"word_selection_indicies: {word_selection_indicies}")
    print(f"word_map: {word_map}")
    return create_string(word_selection_indicies, word_map)

def pyramid_cipher(number):
    word_selection_indicies = []
    selected_index = 0
    incrementing_index = 1
    while selected_index < number:     
        selected_index += incrementing_index
        print(f"selected_index: {selected_index}")
        incrementing_index += 1
        word_selection_indicies.append(selected_index)
    return word_selection_indicies

def create_string(word_selection_indicies, word_map):
    decoded_message = ""
    for i in word_selection_indicies:
        decoded_message += word_map[i] + " "
    return decoded_message.rstrip(" ")
