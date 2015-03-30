docker build -t inform7-builder .
touch story.ni
rm -f output.ulx
touch output.ulx
docker run -ti \
    -v "$PWD/story.ni":/root/story.ni \
    -v "$PWD/output.ulx":/root/output.ulx \
    inform7-builder
