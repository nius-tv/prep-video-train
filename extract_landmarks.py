import glob
import json
import sys

from config import *
from face_landmarks import FaceLandmarks
from pathlib import Path


if __name__ == '__main__':
    dir_path = sys.argv[1]
    face_landmarks = FaceLandmarks()

    output_file = open(LANDMARKS_FILE_PATH, 'w')
    frames_dir = '{}/*'.format(dir_path)
    files = glob.iglob(frames_dir)

    for i, file_path in enumerate(files):
        print(i + 1, file_path)
        data = face_landmarks.get(file_path)[0] # [0] = get first face
        data['frame'] = Path(file_path).stem # extracts filename without extension
        data = json.dumps(data)
        output_file.write(data + '\n')
