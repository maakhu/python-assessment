from helper import validate_and_execute, user_input_message


user_input = input(user_input_message)
# files = user_input.split(', ')
try:
    if len(user_input) >= 6:
        files_dictionary = {"json": user_input}
        validate_and_execute(files_dictionary)
    else:
        print("please enter the json filename with their extension (sample.json)")
except IndexError:
    print("please enter the correct filename with its extension")

