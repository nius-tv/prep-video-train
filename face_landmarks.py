import cv2
import dlib

from config import shape_predictor_model_path


class FaceLandmarks(object):

    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(shape_predictor_model_path)

    def get(self, input_image):
        image = cv2.imread(input_image)
        faces_lms = []
        # The 1 in the second argument indicates that we want to upsample the image one time.
        # This will make everything bigger and allow us to detect more faces.
        for face in self.detector(image, 1):
            shape = self.predictor(image, face)
            landmarks = [(p.x, p.y) for p in shape.parts()]
            faces_lms.append({
                'jaw': landmarks[0:17],
                'left_eyebrow': landmarks[17:22],
                'right_eyebrow': landmarks[22:27],
                'nose_bridge': landmarks[27:31],
                'lower_nose': landmarks[31:36],
                'left_eye': landmarks[36:42],
                'right_eye': landmarks[42:48],
                'outer_lip': landmarks[48:60],
                'inner_lip': landmarks[60:68]
            })
        return faces_lms
