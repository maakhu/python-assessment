# write command line app to accept conf file and run the report
from helper import validate_and_execute, user_input_message


user_input = input(user_input_message)
files = user_input.split(', ')
try:
    if len(files) == 2:
        files_dictionary = {"json": files[0], "csv": files[1]}
        validate_and_execute(files_dictionary)
    else:
        print("please enter both of the filenames with their extensions (sample.json, sample.csv)")
except IndexError:
    print("please enter both filenames with their extensions")

