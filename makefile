IMG=dcimg:latest

docker-img:
	docker build -t $IMG ./integration

docker-cnt:
	docker run -it --rm --name dcenv --mount type=bind,source=$pwd,target=/dc/ $IMG
