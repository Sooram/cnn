#--------------------------------------------------------------------------------------
# create a certain size of batch for images and labels(one-hot encoded)
#--------------------------------------------------------------------------------------
import numpy as np
import random

BATCH_SIZE = 2
NUM_LABELS = 4
IMAGE_SIZE = 48
filenames = [['0-1', '0-2'],["1-1", '1-2', '1-3'],['2-1','2-2','2-3'],['3-1','3-2']]

# def get_batch(BATCH_SIZE):
# randomly select 'batch_size' of data from each class
batch_names = []
batch_labels = []
for label in range(len(filenames)):
    print(label)
    randomly_selected = random.sample(filenames[label], BATCH_SIZE)
    for filename in randomly_selected:
        batch_names.append(filename)
        batch_labels.append(label)
    # randomly_selected = np.random.choice(len(filenames[i]), size=BATCH_SIZE, replace=False)
    # for idx in len(randomly_selected):
    #     batch_names.append(filenames[i][idx])

# one-hot encode labels
def one_hot_encode(x, num_labels):
    """
    One hot encode a list of sample labels. Return a one-hot encoded vector for each label.
    : x: List of sample Labels
    : return: Numpy array of one-hot encoded labels
    """
    return np.eye(num_labels)[x]
batch_encoded_labels = one_hot_encode(batch_labels, NUM_LABELS)

# read in image files
batch_images = []
for filename in batch_names:
    print(filename)
    # open, read, and convert image files to pixels
    # resize 

# reshape 'batch_images'
batch_images = np.array(batch_images)
batch_images = batch_images.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1)

# return(batch_images, batch_encoded_labels)

#--------------------------------------------------------------------------------------
# check the first image 
#--------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

image_0 = batch_images[0]
label_0 = batch_encoded_labels[0]
print "image_0 shape = ", image_0.shape 
print "image_0 label = ", label_0   
image_0 = np.resize(image_0, (48,48))
plt.imshow(image_0, cmap='Greys_r')
plt.show()