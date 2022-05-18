package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func home(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"body": "Hello From Service 1",
	})
}

func main() {
	r := gin.Default()
	r.GET("/", home)
	r.Run(":8080")
}
