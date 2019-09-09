import cv2
import glob

from config import SCALED_VIDEO_RESOLUTION
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
        image = ndimage.rotate(image, 90)
        # Save image
        filename = image_path.split('/')[-1]
        output_file = '{}/{}'.format(output_dir, filename)
        cv2.imwrite(output_file, image)


if __name__ == '__main__':
    train_dirs = [
        {'input': '/data/landmarks/*', 'output': '/data/pix2pix/train_A'},
        {'input': '/data/frames/*'   , 'output': '/data/pix2pix/train_B'}
    ]
    for train_dir in train_dirs:
        prepare_images_for_training(train_dir)
