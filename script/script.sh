# Docker Build
function build_docker() {
    echo "===================Docker Build====================="
    local BUILD=$(docker build -t $1 --compress .)
    if [[ $? -ne 0 ]]; then
        echo "Error for docker build: $BUILD"
        exit 1
    else
        echo "Docker Build Successfull"
    fi
}

# Docker Validate - Dockerfile & .dockerignore
function check_Dockerfile() {
    local DOCKERFILE="Dockerfile"
    if [[ ! -f $DOCKERFILE ]]; then
        echo "File not Found: Dockerfile"
        exit 1
    fi

    local DOCKERIGNORE=".dockerignore"
    if [[ ! -f $DOCKERIGNORE ]]; then
        echo "File not Found: .dockerignore"
        exit 1
    fi
}

check_Dockerfile
