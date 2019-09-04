FROM ubuntu:18.04

RUN apt-get update -y

RUN apt-get install -y cmake # required by dlib
RUN apt-get install -y libboost-all-dev # required by dlib
RUN apt-get install -y libsm6 # required by opencv
RUN apt-get install -y python3.5
RUN apt-get install -y python3-pip

RUN pip3 install dlib==19.8
RUN pip3 install opencv-python==3.4.0.12
