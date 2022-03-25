FROM golang:alpine3.14 as builder

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download
COPY *.go ./

RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o server .

FROM scratch

ENV GIN_MODE=release

COPY --from=builder /app/server server

EXPOSE 8080

ENTRYPOINT [ "/server" ]