import logging
from pptx_generator import create_report

user_input_message = "Please enter the .json filename" \
                     " to prepare the report!" \
                     "(e.g. sample.json)\n"


def validate_and_execute(user_input):
    try:
        if len(user_input) != 1:
            print("please enter one file name!")
            logging.error('incorrect user input')
        elif user_input["json"].endswith(".json"):
            file = list(user_input.values())
            logging.info("helper worked")

            create_report(file)
        else:
            print("please enter only the filenames with their extensions")
            logging.error('incorrect user input')
    except IndexError:
        print("please enter only the filenames with their extensions")
        logging.error('incorrect user input')