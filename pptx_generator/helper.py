from pptx_generator import create_report

user_input_message = "Please enter the .json and .csv filenames separated by comma" \
                     " to prepare the report!" \
                     "(sample.json, sample.csv)\n"


def validate_and_execute(user_input):
    files = []
    try:
        if len(user_input) < 2:
            print("please enter both file names!")
        elif user_input["json"].endswith(".json") and user_input["csv"].endswith(".csv"):
            files = list(user_input.values())
            create_report(files)
        else:
            print("please enter only the filenames with their extensions")

    except IndexError:
        print("please enter only the filenames with their extensions")