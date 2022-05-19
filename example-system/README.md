# A example distributed System 

This is a example cloud based approche to a distributed system made up of 3 services implemented in go.

each component can be accessed using localhost and port 808{service number}`

## Docker Compose
To start System using docker compose:
```bash
make compose
```
To stop the Docker Compose system run:
```bash
make down
```
## KinD
To start System using docker compose:
```bash
make kind
```
Cleanup the Kind Cluster run:
```bash
make delete
```