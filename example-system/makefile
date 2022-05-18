build:
	docker-compose -f docker-compose.yml build $(c)
up:
	docker-compose -f docker-compose.yml up -d
down:
	docker-compose -f docker-compose.yml down

create:
	kind create cluster --name ds-cluster --config kind-cluster-config.yml

delete:
	kind delete cluster --name ds-cluster

load:
	kind load docker-image service1:latest --name ds-cluster
	kind load docker-image service2:latest --name ds-cluster
	kind load docker-image service3:latest --name ds-cluster