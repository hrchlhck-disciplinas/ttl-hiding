build:
	docker build -t teste:server -f Dockerfile.servidor . && \
	docker build -t teste:client -f Dockerfile.cliente .

server:
	docker run -it --rm -p 8888:8888 teste:server

client:
	docker run -it --rm --env-file=.env teste:client 