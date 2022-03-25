package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func home(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"data": "Hello World",
	})
}

func main() {

	r := gin.Default()
	r.GET("/", home)
	r.Run(":8080")

}
