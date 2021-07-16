|Action|Command|Example|
|-|-|-|
|Copy to container| docker cp [HOST_PATH] [CONTAINER NAME]:[DEST_PATH]||
|Export container to a file| docker export [CONTAINER NAME] > [file name.tar]||
|Import container to a file as an image| docker import [file name.tar]||
|Run a container | docker run [OPTIONS] IMAGE [COMMAND] [ARG...]| docker run --name=testreuse testreuse-v2 sleep infinity|
|Go inside|docker exec -it [CONTAINER NAME] /bin/bash||

### Docker run options
|Action|Option|Example|
|-|-|-|
|Name of conatainer| --name |--name=testreuse |
|Network, default is docker|--network|--network=host|
|Mount a folder|-v [HOST_PATH]:[DEST_PATH]|-v /home/amohebbi/models:/root/models|
|Deattach, Not seeing output|-d||


