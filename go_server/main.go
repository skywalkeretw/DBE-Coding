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

type user struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
}

var users = []user{
	{0, "admin"},
	{1, "OnePlus"},
	{42, "Arthur Dent"},
	{69, "nice"},
	{69420, "Elon Musk"},
	{1000000, "Dr Evil"},
}

func getUsers(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}

func main() {

	r := gin.Default()
	r.GET("/", home)
	r.GET("/users", getUsers)
	r.Run(":8080")

}
