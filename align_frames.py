from config import *
from PIL import Image, ImageChops


if __name__ == '__main__':
    with open(ALIGNMENTS_FILE_PATH) as f:
        lines = f.readlines()

    for line in lines:
        columns = line.split(',')
        frame = int(columns[0])
        file_path = '{}/{:010d}.{}'.format(FRAMES_DIR_PATH, frame, IMG_FMT)
        print(frame, file_path)

        img = Image.open(file_path)
        offsets = [int(float(offset)) for offset in columns[1:]]
        img = ImageChops.offset(img,
                                xoffset=offsets[0],
                                yoffset=offsets[1])

        filename = file_path.split('/')[-1]
        output_file = '{}/{}'.format(ALIGNED_DIR_PATH, filename)
        img.save(output_file)
