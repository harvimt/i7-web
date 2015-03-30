FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y curl unionfs-fuse git

RUN curl -O 'http://inform7.com/download/content/6L38/gnome-inform7_6L38-0ubuntu1_amd64.deb'
RUN dpkg -i --force-depends gnome-inform7_6L38-0ubuntu1_amd64.deb
RUN apt-get -yf install

RUN rm gnome-inform7_6L38-0ubuntu1_amd64.deb
RUN apt-get remove -y curl

COPY generic_project.inform /root/project.inform
COPY run.sh /run.sh
RUN chmod +x /run.sh
VOLUME /root/project.inform/Source/story.ni
VOLUME /root/project.inform/Build
CMD /run.sh
