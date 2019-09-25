import cv2
import json
import numpy as np

from config import *


def landmarks_to_image(landmarks, output_file):
    shape = (ORIGINAL_VIDEO_RESOLUTION[1], ORIGINAL_VIDEO_RESOLUTION[0]) # columns, rows
    image = np.zeros(shape, np.uint8)
    points = landmarks['outer_lip'] + landmarks['inner_lip'] # only use mouth landmarks

    color = (255, 255, 255) # white
    for x, y in points:
        # 3 = radius
        # -1 = thinkness, when value is set to -1, the circle will be filled with color
        cv2.circle(image, (x, y), 3, color, -1)

    cv2.imwrite(output_file, image)


if __name__ == '__main__':
    with open(LANDMARKS_FILE_PATH) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        data = json.loads(line)
        frame = data['frame']
        print(i + 1, frame)

        output_file = '{}/{}.{}'.format(LANDMARKS_DIR_PATH, frame, IMG_FMT)
        landmarks_to_image(data, output_file)
