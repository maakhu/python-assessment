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
from layouts.Title import TitleSlide
from layouts.Bullet import BulletSlide
from layouts.Picture import PictureSlide
from layouts.Text import TextSlide


filename_time = datetime.now().strftime("%H:%M:%S_%d.%m.%Y")
title = "report_" + str(filename_time) + ".pptx"

presentation = Presentation()

title_slide = TitleSlide("My Title", "Subtitle")
title_slide.create_slide(presentation)

bullets = ["Bullet 1", "Bullet 2", "Bullet 3"]
bullet_slide = BulletSlide("Bullet Slide Title", bullets)
bullet_slide.create_slide(presentation)

picture = "pic.png"
pic_slide = PictureSlide("Picture Title", picture)
pic_slide.create_slide(presentation)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod " \
       "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, " \
       "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea " \
       "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate " \
       "velit esse cillum dolore eu fugiat " \
       "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in" \
       "culpa qui officia deserunt mollit anim id est laborum."

text_slide = TextSlide("Lorem Ipsum", text)
text_slide.create_slide(presentation)


presentation.save(title)
