## IOPaint的docker镜像

基于[IOPaint](https://github.com/Sanster/IOPaint)构建docker镜像


### build docker
`--build-arg PROXY=http://192.168.50.48:7890`是可选的

- gpu版
    ```shell
    docker build . -t samge/iopaint:gpu -f Dockerfile --build-arg PROXY=http://192.168.50.48:7890
    ```

- cpu版
    ```shell
    docker build . -t samge/iopaint:cpu -f Dockerfile-cpu --build-arg PROXY=http://192.168.50.48:7890
    ```

### upload
```shell
docker push samge/iopaint:gpu
docker push samge/iopaint:cpu
docker push samge/iopaint
```

### use

- gpu版
    ```shell
    docker run -d \
    -p 8080:8080 \
    -v ~/.cache:/root/.cache \
    --gpus all \
    --pull=always \
    --restart=always \
    --name iopaint \
    samge/iopaint:gpu
    ```

- cpu版
    ```shell
    docker run -d \
    -p 8080:8080 \
    -v ~/.cache:/root/.cache \
    --gpus all \
    --pull=always \
    --restart=always \
    --name iopaint \
    samge/iopaint:cpu
    ```