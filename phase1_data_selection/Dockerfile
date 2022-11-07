FROM python:3.4.8-stretch

RUN apt-get update
RUN apt-get install -y vim
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install ez_setup
RUN pip install pylint
RUN mkdir work
RUN cd work && git clone https://github.com/fukuball/fuku-ml.git

#docker build -t fukuball-fuku-ml-3.4.8 .