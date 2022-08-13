from logging import raiseExceptions
import skimage.io as io
import matplotlib.pyplot as plt
import numpy
class Image:
    def __init__(self):
        pass
    
    def image_plot(self, image: numpy.array, title:str):
        plt.title(title)
        if len(image.shape) == 2:
            plt.imshow(image, cmap="gray")
        else:
            plt.imshow(image)

    def image_shape(self, image: numpy.array):
        return image.shape

class ImageReader(Image):
    def __init__(self, image_path:str):
        super().__init__()     
        self.image_path = image_path

    def read_image(self) -> numpy.ndarray:
        return io.imread(self.image_path)

    def read_image_asgray(self) -> numpy.ndarray:
        img = self.read_image()
        if len(img.shape) == 3:
            r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
            gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
            return gray
        ValueError('Image number of chanels is different than expected')
            
class ImageTranformer(Image):
    def __init__(self, image:numpy.ndarray):
        self.image = image
    
    def negative_tranformation(self):
        w,h = self.image.shape
        for i in range(w):
            for j in range(h):
                self.image[i,j] = 255 - self.image[i,j]
        return self.image