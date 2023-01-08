# install go
sudo apt update -y && sudo apt-get update -y
sudo apt upgrade -y && sudo apt-get upgrade -y
sudo apt install -y golang-go

# install go ide
sudo snap install -y goland --classic

# create go project
cd ~
cd Downloads
mkdir go-rest-api
cd go-rest-api
go mod init example/go-rest-api
go mod tidy

nano main.go
<file>
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.New()

	r.GET("/books", listBooksHandler)
	r.POST("/books", createBookHandler)
	r.DELETE("/books/:id", deleteBookHandler)

	r.Run()
}

type Book struct {
	ID     string `json:"id"`
	Title  string `json:"title"`
	Author string `json:"author"`
}

var books = []Book{
	{ID: "1", Title: "Harry Potter", Author: "J. K. Rowling"},
	{ID: "2", Title: "The Lord of the Rings", Author: "J. R. R. Tolkien"},
	{ID: "3", Title: "The Wizard of Oz", Author: "L. Frank Baum"},
}

func listBooksHandler(c *gin.Context) {
	c.JSON(http.StatusOK, books)
}

func createBookHandler(c *gin.Context) {
	var book Book

	if err := c.ShouldBindJSON(&book); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	books = append(books, book)

	c.JSON(http.StatusCreated, book)
}

func deleteBookHandler(c *gin.Context) {
	id := c.Param("id")

	for i, a := range books {
		if a.ID == id {
			books = append(books[:i], books[i+1:]...)
			break
		}
	}

	c.Status(http.StatusNoContent)
}
</file>

go get
go run main.go
# browse http://127.0.0.1:8080/books
go build main.go