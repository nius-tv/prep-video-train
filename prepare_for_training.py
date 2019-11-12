import cv2
import glob
import os

from config import *
from scipy import ndimage


def prepare_images_for_training(train_dir):
    files = glob.iglob(train_dir['input'])
    output_dir = train_dir['output']

    for i, image_path in enumerate(files):
        print(i + 1, image_path)
        image = cv2.imread(image_path)
        # Resize image
        image = cv2.resize(image, SCALED_VIDEO_RESOLUTION, interpolation=cv2.INTER_CUBIC)
        # Rotate image
        image = ndimage.rotate(image, ROTATION_ANGLE)
        # Save image
        filename = image_path.split('/')[-1]
        if output_dir == TRAIN_B_DIR_PATH:
            train_a_file_path = '{}/{}'.format(TRAIN_A_DIR_PATH, filename)
            if not os.path.exists(train_a_file_path):
                continue
        output_file = '{}/{}'.format(output_dir, filename)
        assert cv2.imwrite(output_file, image)


if __name__ == '__main__':
    train_dirs = [
        {
            'input': '{}/*'.format(LANDMARKS_DIR_PATH),
            'output': TRAIN_A_DIR_PATH
        },
        {
            'input': '{}/*'.format(FRAMES_DIR_PATH),
            'output': TRAIN_B_DIR_PATH
        }
    ]
    for train_dir in train_dirs:
        prepare_images_for_training(train_dir)
