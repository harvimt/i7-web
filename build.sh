docker build -t inform7-builder .
touch story.ni
touch output.ulx
mkdir -p build
docker run -ti \
    -v "$PWD/story.ni":/root/project.inform/Source/story.ni:ro \
    -v "$PWD/output.ulx":/root/project.inform/Build/output.ulx \
    inform7-builder
