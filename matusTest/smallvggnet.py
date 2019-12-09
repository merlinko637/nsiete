# smallvggnet.py

# import the necessary packages
import keras
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K

# define our SmallVGGNet class and the build method
# Should I use "ELU" for hidden layer as better for image classification?
class SmallVGGNet:
    @staticmethod
    def build(width, height, depth, classes):
        # initialize the model along with the input shape to be "channels last" and the channels dimension/depth itself
        model = Sequential()   # (i.e. TensorFlow ordering)
        inputShape = (height, width, depth)
        chanDim = -1

        # if we are using "channels first", update the input shape and channels dimension
        if K.image_data_format() == "channels_first":   # (i.e. Theano ordering)
            inputShape = (depth, height, width)
            chanDim = 1

        # CONV => RELU => POOL layer set              # first CONV layer has 32 filters of size 3x3
        model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))                 # ReLU (Rectified Linear Unit) activation function
        model.add(BatchNormalization(axis=chanDim))   # normalize activations of input volume before passing to next layer
        model.add(MaxPooling2D(pool_size=(2, 2)))     # progressively reduce spatial size (width and height) of input 
        model.add(Dropout(0.25))                      # disconnecting random neurons between layers, reduce overfitting

        # (CONV => RELU) * 2 => POOL layer set          # filter dimensions remain the same (3x3)
        model.add(Conv2D(64, (3, 3), padding="same"))   # increase total number of filters learned (from 32 to 64)
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(64, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        # (CONV => RELU) * 3 => POOL layer set
        model.add(Conv2D(128, (3, 3), padding="same"))   # total number of filters learned by CONV layers has doubled (128)
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(128, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(128, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        # first (and only) set of fully connected layer (FC) => RELU layers
        model.add(Flatten())
        model.add(Dense(512))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))

        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        # return the constructed network architecture
        return model