### Create instance

``` 
gcloud compute instances create node2 \
--enable-nested-virtualization \
--zone=us-central1-a \
--min-cpu-platform="Intel Haswell" \
--boot-disk-size=200G \
--image=ubuntu-1804-bionic-v20211021 \
--image-project=ubuntu-os-cloud \
--custom-cpu=8 \
--custom-memory=16 
```
