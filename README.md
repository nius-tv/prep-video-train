docker build \
    -t prep-video \
    .

docker run \
    -v $(pwd):/app \
    -v /Users/carloschinchilla/triphop/data/video:/data \
    -v /Users/carloschinchilla/triphop/models:/models \
    -it prep-video \
    bash

ffmpeg -y \
    -i /data/train.mov \
    -framerate 29.97 \
    /data/frames/%010d.png

python3 extract_landmarks.py
python3 landmarks_to_images.py
python3 prepare_for_training.py