from pptx_generator.pptx_generator import create_report

user_input_message = "Please enter the .json filename" \
                     " to prepare the report!" \
                     "(e.g. sample.json)\n"


def validate_and_execute(user_input):
    try:
        if len(user_input) != 1:
            print("please enter one file name!")
        elif user_input["json"].endswith(".json"):
            file = list(user_input.values())
            create_report(file)
        else:
            print("please enter only the filenames with their extensions")

    except IndexError:
        print("please enter only the filenames with their extensions")