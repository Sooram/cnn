NUM_LABELS = 15
IMAGE_SIZE = 48
#--------------------------------------------------------------------------------------
# load filenames from directories
#--------------------------------------------------------------------------------------
filenames = []

#--------------------------------------------------------------------------------------
# train test split
#--------------------------------------------------------------------------------------
TRAIN_PERCENT = 0.7
train_filenames = []
test_filenames = []
for i in range(NUM_LABELS):
    train_size = int(len(filenames[i]) * TRAIN_PERCENT)
    train_filenames.append(filenames[i][:train_size])
    test_filenames.append(filenames[i][train_size:])

print "number of train images = ", len(train_filenames)
print "number of test images = ", len(test_filenames)
#--------------------------------------------------------------------------------------
# conv model
#--------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------
# train
#--------------------------------------------------------------------------------------
