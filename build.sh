docker build -t inform7-builder .
touch story.ni
rm -f output.ulx
touch output.ulx
docker run -ti \
    -v "$PWD/story.ni":/root/project.inform/Source/story.ni:ro \
    -v "$PWD/output.ulx":/root/project.inform/Build/output.ulx \
    inform7-builder
