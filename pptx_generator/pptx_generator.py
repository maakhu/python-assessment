import collections
import collections.abc
from helper import validate_and_execute
from pptx import Presentation
from datetime import datetime
from layouts.Title import TitleSlide
from layouts.Bullet import BulletSlide
from layouts.Picture import PictureSlide
from layouts.Text import TextSlide
from layouts.Plot import PlotSlide
import json
import csv


def create_report(files):
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

    # Read plot data from the content file
    content = files[1]
    with open(content) as file:
        plot_data = json.load(file)

    plot = {
       "x-label": "The Plot X Label",
       "y-label": "The Plot Y Label"
    }
    plot_slide = PlotSlide("Title", plot_data, plot)
    plot_slide.create_slide(presentation)

    presentation.save(title)
