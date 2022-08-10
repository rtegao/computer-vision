from logging import raiseExceptions
import skimage.io as io
import matplotlib.pyplot as plt
import numpy

class ImageReader:
    def __init__(self, image_path:str):
        self.image_path = image_path

    def read_image(self) -> numpy.ndarray:
        return io.imread(self.image_path)

    def read_image_asgray(self) -> numpy.ndarray:
        img = self.read_image()
        if len(img.shape) == 3:
            r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
            gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
            return gray
        else:
            ValueError('Image number of chanels is different than expected')



class Image():
    def __init__(self, image:numpy.ndarray):
        self.image = image
    
    def image_plot(self, title:str):
        plt.title(title)
        if len(self.image.shape) == 2:
            plt.imshow(self.image, cmap="gray")
        else:
            plt.imshow(self.image)

    def image_shape(self):
        return self.image.shape