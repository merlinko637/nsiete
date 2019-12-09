FROM "ubuntu:bionic"

LABEL maintainer = "Matus Zelenak <mato.zelenak@gmail.com>"
LABEL version = "1.1"

RUN apt-get update && yes | apt-get upgrade

RUN apt-get install -y git python3-pip python3-venv libsm6 libxext6 libxrender-dev
RUN pip3 install --upgrade pip
ENV PATH="$PATH:/env/bin"
ENV PYTHONPATH="$PYTHONPATH:/usr/local/lib/python3.6/dist-packages"


RUN cd /usr && git clone https://github.com/AntonMu/TrainYourOwnYOLO

RUN python3 -m venv env 
RUN /bin/bash -c "source /env/bin/activate"

RUN cd usr/TrainYourOwnYOLO && pip3 install -r requirements_gpu.txt