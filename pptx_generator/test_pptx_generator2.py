import unittest
from pptx import Presentation

from layouts.Bullet import BulletSlide
from layouts.Picture import PictureSlide
from layouts.Plot import PlotSlide
from layouts.Text import TextSlide
from layouts.Title import TitleSlide


class TestPptxGenerator(unittest.TestCase):
    def setUp(self):
        self.presentation = Presentation()
        self.test_json = {
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
                  "content": "picture.png"
                },
                {
                  "type": "plot",
                  "title": "The Title Text",
                  "content": "sample.dat",
                  "configuration": {
                    "x-label": "The Plot X Label",
                    "y-label": "The Plot Y Label"
                  }
                }
              ]
            }

    def test_titles(self):
        title_slide = TitleSlide("Test Title", "Test Subtitle")
        title_slide.create_slide(self.presentation)

    def test_bullet(self):
        bullet_slide = BulletSlide("Test Bullet Slide", [
                    {"level": 1, "text": "The Level 1 Text"},
                    {"level": 2, "text": "The Level 2 Text"},
                    {"level": 2, "text": "The Level 2 Text"},
                    {"level": 1, "text": "The Level 1 Text"}
                  ])
        bullet_slide.create_slide(self.presentation)

    def test_pic(self):
        pic_slide = PictureSlide("Test Picture Slide", "picture.png")
        pic_slide.create_slide(self.presentation)

    def test_text(self):
        text_slide = TextSlide("Test Text Slide", "This is a test text slide content.")
        text_slide.create_slide(self.presentation)

    def test_plot(self):
        config = {
            "x-label": "X Label",
            "y-label": "Y Label"
        }
        plot_slide = PlotSlide("Test Plot Slide", "sample.dat", config)
        plot_slide.create_slide(self.presentation)


if __name__ == '__main__':
    unittest.main()
