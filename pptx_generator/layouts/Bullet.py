class BulletSlide:
    def __init__(self, title, bullets):
        self.title = title
        self.bullets = bullets

    def create_slide(self, presentation):
        bullet_slide_layout = presentation.slide_layouts[1]
        slide = presentation.slides.add_slide(bullet_slide_layout)
        shapes = slide.shapes

        title_shape = shapes.title
        body_shape = shapes.placeholders[1]

        title_shape.text = self.title

        tf = body_shape.text_frame
        tf.text = 'Find the bullet slide layout'

        p = tf.add_paragraph()
        p.text = 'Use _TextFrame.text for first bullet'
        p.level = 1

        p = tf.add_paragraph()
        p.text = 'Use _TextFrame.add_paragraph() for subsequent bullets'
        p.level = 2

