class TitleSlide:
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle

    def create_slide(self, presentation):
        title_slide_layout = presentation.slide_layouts[0]
        slide = presentation.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        title.text = self.title
        subtitle.text = self.subtitle
