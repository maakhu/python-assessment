import csv
from pptx.util import Inches
import matplotlib.pyplot as plt


class PlotSlide:
    def __init__(self, title, content, config):
        self.title = title
        self.content = content
        self.config = config

    def create_slide(self, presentation):
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])
        title = slide.shapes.title
        title.text = self.title

        x_values = self.config['x-label']
        y_values = self.config['y-label']

        # Generate the plot
        x_data, y_data = self.read_plot_data(self.content)
        plt.plot(x_data, y_data)
        plt.xlabel(x_values)
        plt.ylabel(y_values)
        plt.title(self.title)

        # Save the plot as an image
        plot_filename = "plot.png"
        plt.savefig(plot_filename)
        plt.close()

        # Insert the plot image into the slide
        top = Inches(1.5)
        left = Inches(1)
        height = Inches(5.5)
        picture = slide.shapes.add_picture(plot_filename, left, top, height=height)


    @staticmethod
    def read_plot_data(filename):
        x_data = []
        y_data = []
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                x_data.append(float(row[0]))
                y_data.append(float(row[1]))
        return x_data, y_data
