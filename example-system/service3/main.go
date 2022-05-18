package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func home(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"body": "Hello From Service 2",
	})
}

func getService1(c *gin.Context) {

	r, err := http.Get("http://service1:8080")
	if err != nil {
		log.Println(err)
	}
	var data interface{}
	err = json.NewDecoder(r.Body).Decode(&data)
	if err != nil {
		log.Println(err)
	}
	c.JSON(http.StatusOK, data)
}

func main() {
	r := gin.Default()
	r.GET("/", home)
	r.GET("/s1", getService1)
	r.Run(":8080")
}
