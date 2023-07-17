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
from pptx import Presentation
from datetime import datetime
from pptx_generator.layouts.Title import TitleSlide
from pptx_generator.layouts.Bullet import BulletSlide


filename_time = datetime.now().strftime("%H:%M:%S_%d.%m.%Y")
title = "report_" + str(filename_time) + ".pptx"

presentation = Presentation()

title_slide = TitleSlide("My Title", "Subtitle")
title_slide.create_slide(presentation)

bullets = ["Bullet 1", "Bullet 2", "Bullet 3"]
bullet_slide = BulletSlide("Bullet Slide", bullets)
bullet_slide.create_slide(presentation)

presentation.save(title)
