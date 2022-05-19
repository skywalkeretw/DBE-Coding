compose: build up

kind: build create load deploy

build:
	docker-compose -f docker-compose.yml build $(c)
up:
	docker-compose -f docker-compose.yml up -d
down:
	docker-compose down

create: 
	kind create cluster --name ds-cluster --config kind-cluster-config.yml
	
delete:
	kind delete cluster --name ds-cluster

load: create
	kind load docker-image service1:latest --name ds-cluster
	kind load docker-image service2:latest --name ds-cluster
	kind load docker-image service3:latest --name ds-cluster

deploy: load
	kubectl apply -f service1/service1.yml
	kubectl apply -f service2/service2.yml
	kubectl apply -f service3/service3.yml