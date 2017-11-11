from keras.preprocessing import image
import os
import matplotlib.pyplot as plt


PATH_TO_TEST_IMAGES_DIR = 'test_images'
TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(3, 10) ]

img_path_0 = TEST_IMAGE_PATHS[0]
img = image.load_img(img_path_0)
x = image.img_to_array(img)
x = x.reshape((1,) + x.shape)

datagen = image.ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
i = 0
for batch in datagen.flow(x, batch_size=1):
   plt.figure(i)
   imgplot = plt.imshow(image.array_to_img(batch[0]))
   i += 1
   if i % 4 == 0:
       break

plt.show()

