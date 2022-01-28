#!/bin/bash

if [ -z "$1" ] ; then
    echo "You need to provide an URL to extruct as argument"
    exit 1
fi

docker run --rm -v $(pwd)/extruct_react.py:/home/seluser/extruct_react.py --shm-size="2g" -it extruct-react $1