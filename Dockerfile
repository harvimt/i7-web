FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y curl

RUN curl -O 'http://inform7.com/download/content/6L38/gnome-inform7_6L38-0ubuntu1_amd64.deb'
RUN dpkg -i --force-depends gnome-inform7_6L38-0ubuntu1_amd64.deb
RUN apt-get -yf install

RUN rm gnome-inform7_6L38-0ubuntu1_amd64.deb
RUN apt-get remove -y curl

RUN apt-get install -y python3-pip
RUN python3.4 -m pip install vase

COPY generic_project.inform /root/project.inform
COPY run.py /run.py
RUN chmod +x /run.py
CMD python3.4 /run.py
