import json
import numpy as np

from config import *


def get_first_sort(points, asc, axis):
    index = 0 if asc else -1
    axis = 0 if axis.lower() == 'x' else 1 # 0 = X axis
    # Sorts ascendant
    return np.sort(points, axis=axis)[index]


def get_points(all_points, part, asc, axis):
    sorted_points = []

    for points in all_points:
        lm_part_points = points[part]
        point = get_first_sort(lm_part_points, asc, axis)
        sorted_points.append(point)

    return np.array(sorted_points)


def get_median_point(points):
    x = np.median(points[:, 0])
    y = np.median(points[:, 1])
    return x, y


def load_data(lines):
    data = []

    for line in lines:
        line = json.loads(line)
        data.append(line)

    return data


if __name__ == '__main__':
    with open(LANDMARKS_FILE_PATH) as f:
        lines = f.readlines()
    all_points = load_data(lines)

    points = get_points(all_points, part='left_eye', asc=False, axis='x')
    g_left_point = get_median_point(points)

    points = get_points(all_points, part='right_eye', asc=True, axis='x')
    g_right_point = get_median_point(points)

    points = get_points(all_points, part='nose_bridge', asc=False, axis='y')
    g_nose_point = get_median_point(points)

    output_file = open(ALIGNMENTS_FILE_PATH, 'w')

    for points in all_points:
        left_point = get_first_sort(points['left_eye'], asc=False, axis='x')
        right_point = get_first_sort(points['right_eye'], asc=True, axis='x')
        nose_point = get_first_sort(points['nose_bridge'], asc=False, axis='y')

        # Check eye X
        if abs(left_point[0] - g_left_point[0]) + abs(right_point[0] - g_right_point[0]) > EYE_TOLERANCE:
            continue
        # Check eye Y
        if abs(left_point[1] - g_left_point[1]) + abs(right_point[1] - g_right_point[1]) > EYE_TOLERANCE:
            continue
        # Check nose
        if abs(nose_point[0] - g_nose_point[0]) > NOSE_TOLERANCE \
            or abs(nose_point[1] - g_nose_point[1]) > NOSE_TOLERANCE:
            continue

        offset = np.subtract(nose_point, g_nose_point)
        print(offset)

        frame = points['frame']
        offset = offset.tolist()
        line = '{},{},{}\n'.format(frame, offset[0], offset[1])
        output_file.write(line)
