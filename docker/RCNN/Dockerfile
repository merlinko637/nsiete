FROM "ubuntu:bionic"

LABEL maintainer = "Matus Zelenak <mato.zelenak@gmail.com>"
LABEL version = "0.9"

RUN apt-get update && yes | apt-get upgrade
RUN apt-get install -y python3
RUN apt-get install -y git python3-pip
RUN pip3 install --upgrade pip
RUN apt-get install curl

# RUN mkdir -p /tensorflow/models
# RUN cd tensorflow/models
# RUN git clone https://github.com/tensorflow/models
# 
# 
# RUN pip3 install tensorflow==1.14
# 
# RUN pip3 install jupyter
# RUN pip3 install matplotlib
# 
# RUN pip3 install Cython
# RUN pip3 install contextlib2
# RUN pip3 install pillow
# RUN pip3 install lxml
# RUN pip3 install jupyter
# RUN pip3 install matplotlib
# 
# 
# RUN git clone https://github.com/cocodataset/cocoapi
# RUN cd cocoapi/PythonAPI
# RUN make
# RUN cp -r pycocotools tensorflow/models/research/


# Make sure you grab the latest version
RUN curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip

# Unzip
RUN unzip protoc-3.2.0-linux-x86_64.zip -d protoc3

# Move protoc to /usr/local/bin/
RUN  mv protoc3/bin/* /usr/local/bin/

# Move protoc3/include to /usr/local/include/
RUN  mv protoc3/include/* /usr/local/include/

RUN ./bin/protoc object_detection/protos/*.proto --python_out=.