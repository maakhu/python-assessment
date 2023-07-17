# Project planning
# make separate classes for different layout styles
# - Title slide
# - Text slide
# - List slide
# - Picture slide
# - Plot slide (the plot data should be read from a .dat file)
#  Each class/function should take relevant parameters and
#  generate the corresponding slide using the python-pptx library.

# Define a function to read the configuration file and generate the report based on the configuration.
import collections
import collections.abc
from pptx import Presentation
from datetime import datetime

filename_time = datetime.now().strftime("%H:%M:%S_%d.%m.%Y")
title = "report_" + str(filename_time) + ".pptx"

presentation = Presentation()


presentation.save(title)

