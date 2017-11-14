IMG=dcimg:latest

docker-img:
	docker build -t $IMG ./integration

docker-cnt:
	docker run -it --rm --name dcenv --mount type=bind,source=$pwd,target=/dc/ $IMG

build-pytorch:
	cd pytorch && export NO_CUDA=1 && export CMAKE_PREFIX_PATH="$(dirname $(which conda))/../" && python setup.py build develop
	
install-pytorch:
	git clone --recursive https://github.com/pytorch/pytorch
	build-pytorch

bash:
	/bin/bash

env:
	source activate pytorch-py3.6
