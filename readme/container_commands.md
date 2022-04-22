## Docker Commands
|Action|Command|Example|
|-|-|-|
|Copy to container| docker cp [HOST_PATH] [CONTAINER NAME]:[DEST_PATH]||
|Export container to a file| docker export [CONTAINER NAME] > [file name.tar]||
|Import container to a file as an image| docker import [file name.tar] [image name]||
|Run a container | docker run [OPTIONS] IMAGE [COMMAND] [ARG...]| docker run --name=testreuse testreuse-v2 sleep infinity|
|Go inside|docker exec -it [CONTAINER NAME] /bin/bash||
|Remove image| docker rmi [IMAGE] | |
|Remove container| docker rm [CONTAINER NAME]|

## Docker run options
|Action|Option|Example|
|-|-|-|
|Name of conatainer| --name |--name=testreuse |
|Network, default is docker|--network|--network=host|
|Mount a folder|-v [HOST_PATH]:[DEST_PATH]|-v /home/amohebbi/models:/root/models|
|Deattach, Not seeing output|-d||
|Expose a port| --expose|--expose=5554-5555 |
|Map ports between host and a container|-p|  -p 5554-5555|
|Give extended privileges to this container|--privileged||
|Run devices inside the container without the --privileged flag|--device|--device=/dev/kvm |
|dedicate cpu cores| --cpuset-cpus=9-17 ||

Example:

```
 docker run --privileged --name=testreuse-atm --cpuset-cpus=9-17  -v /home/amohebbi/models:/root/models -d testreuse-atm sleep infinity
```

```
docker run --privileged --name=testreuse-craft  --cpuset-cpus=0-8  --network=host -v /home/amohebbi/models:/root/models -d testreuse-craft sleep infinity
```




