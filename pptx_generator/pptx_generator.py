import collections
import collections.abc
from pptx import Presentation
from datetime import datetime
from pptx_generator.layouts.Title import TitleSlide
from pptx_generator.layouts.Bullet import BulletSlide
from pptx_generator.layouts.Picture import PictureSlide
from pptx_generator.layouts.Text import TextSlide
from pptx_generator.layouts.Plot import PlotSlide
import json


def create_report(input_file):
    filename_time = datetime.now().strftime("%H:%M:%S_%d.%m.%Y")
    filename = "report_" + str(filename_time) + ".pptx"

    # Read input files
    json_content = open(input_file[0])
    json_data = json.load(json_content)

    presentation = Presentation()

    for slide in json_data['presentation']:
        if slide["type"] == "title":
            titles(presentation, slide['title'], slide['content'])
        elif slide["type"] == "text":
            text(presentation, slide['title'], slide['content'])
        elif slide["type"] == "list":
            bullet(presentation, slide['title'], slide['content'])
        elif slide["type"] == "picture":
            pic(presentation, slide['title'], slide['content'])
        elif slide["type"] == "plot":
            plot(presentation, slide['title'], slide['content'], slide['configuration'])

    presentation.save(filename)


def titles(presentation, title, content):
    title_slide = TitleSlide(title, content)
    title_slide.create_slide(presentation)


def bullet(presentation, title, content):
    bullets = content
    bullet_slide = BulletSlide(title, bullets)
    bullet_slide.create_slide(presentation)


def pic(presentation, title, content):
    pic_slide = PictureSlide(title, content)
    pic_slide.create_slide(presentation)


def text(presentation, title, content):
    text_slide = TextSlide(title, content)
    text_slide.create_slide(presentation)


def plot(presentation, title, content, config):
    plot_slide = PlotSlide(title, content, config)
    plot_slide.create_slide(presentation)
