class BulletSlide:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def create_slide(self, presentation):
        print(self.content)
        bullet_slide_layout = presentation.slide_layouts[1]
        slide = presentation.slides.add_slide(bullet_slide_layout)
        shapes = slide.shapes

        title_shape = shapes.title
        body_shape = shapes.placeholders[1]

        title_shape.text = self.title

        tf = body_shape.text_frame
        tf.text = ''

        for bullet in self.content:
            p = tf.add_paragraph()
            p.text = bullet['text']
            p.level = bullet['level']
