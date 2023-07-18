# Python Assessment - Task 1: PPTX Report Generator

![Python Version](https://img.shields.io/badge/python-3.11.4-blue.svg)

This repository contains a Python script that generates a PowerPoint (PPTX) report based on a JSON input. The script uses the `python-pptx` library to create slides with various layouts, such as title, text, bullet points, pictures, and plots.

## Getting Started

Follow the steps below to set up the project on your local machine and generate a PPTX report.

### Prerequisites

- Python 3.11.4 or higher
- `python-pptx` library

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/maakhu/python-assessment.git
```

2. Navigate to the Task1_PPTX_report directory:

```bash
cd python-assessment/Task1_PPTX_report
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

### Usage

1. Create a JSON file with the content for the PPTX report. The JSON structure should follow the format given in the example below:

```json
{
  "presentation": [
    {
      "type": "title",
      "title": "The Title Text",
      "content": "The Sub-Title Text"
    },
    {
      "type": "text",
      "title": "The Title Text",
      "content": "The Long Text"
    },
    {
      "type": "list",
      "title": "The Title Text",
      "content": [
        {"level": 1, "text": "The Level 1 Text"},
        {"level": 2, "text": "The Level 2 Text"},
        {"level": 2, "text": "The Level 2 Text"},
        {"level": 1, "text": "The Level 1 Text"}
      ]
    },
    {
      "type": "picture",
      "title": "The Title Text",
      "content": "path/to/image.jpg"
    },
    {
      "type": "plot",
      "title": "The Title Text",
      "content": "path/to/data.csv",
      "configuration": {
        "x-label": "The Plot X Label",
        "y-label": "The Plot Y Label"
      }
    }
  ]
}
```

2. Run the script with the JSON file as input:

```bash
python pptx_generator.py input_file.json
```

3. A PPTX report file will be generated in the same directory with a name like `report_HH:MM:SS_DD.MM.YYYY.pptx`.

## Test

The repository includes a test suite to verify the functionality of the `pptx_generator.py` script. Pytest framework has been used to prepare the tests, to run the tests, use the following command after installing Pytest:

```bash
pytest
```

## Acknowledgments

- [python-pptx](https://python-pptx.readthedocs.io/): The Python library used for generating PowerPoint presentations.

---

Thank you for checking out this project! If you have any questions or feedback, feel free to reach out. Happy coding! 🚀