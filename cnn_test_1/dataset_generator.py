from keras.preprocessing.image import ImageDataGenerator
import group_raw_data


def data_generator():
    # Normalize image data
    train_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
        group_raw_data.train_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary')
    validation_generator = test_datagen.flow_from_directory(
        group_raw_data.validation_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary')
    return train_generator, validation_generator
