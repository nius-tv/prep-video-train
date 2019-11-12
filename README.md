docker build \
	-t prep-video-train \
	.

export IMAGE=us.gcr.io/plasmic-artefacts-2/prep-video-train
export PLASMIC_DIR=$HOME/triphop
docker run \
	-v $(pwd):/app \
	-v $PLASMIC_DIR/data/training:/data \
	-v $PLASMIC_DIR/models:/models \
	-it $IMAGE \
	bash

1) Use After Effects to remove chroma key from the training video. Replace it with a solid green color.

2) Use After Effects to convert the training video into a sequence of image files. Save the image files into /data/frames directory. 

Note: After Effects might change the color "scheme" of the images, resulting in image files looking visually different than the ones perceived in the video. By experiment with the different output settings in the render pannel, you can aproximate to the training video perceived colors -- we suspect it is a problem with the encoding.

3) Manually, delete images containing "blinks" and other "strange" gestures.

4) Run python3 extract_landmarks.py /data/frames

5) Run python3 calculate_alignments.py

6) Run python3 align_frames.py

7) Run python3 extract_landmarks.py /data/aligned

8) Run python3 landmarks_to_images.py

9) Run python3 prepare_for_training.py
