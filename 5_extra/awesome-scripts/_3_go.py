def setup_lang_and_ide():
    """
    # TODO update system repositories and dependencies
    sudo apt-get update -y && sudo apt update -y
    sudo apt-get upgrade -y && sudo apt upgrade -y

    # TODO install lang
    sudo apt install -y golang-go

    # TODO install ide
    sudo snap install goland --classic
    sudo snap install code --classic
    """

def project():
    """
    # TODO create new project
    cd ~/Downloads
    mkdir go_app && go_app
    go mod init github/bogdandrienko/go_app
    cd go_app
    touch main.rs

    # TODO add needs and remove trash libs
    go mod tidy

    # TODO download all libs
    go get

    # TODO download selected lib
    go get -u github.com/lib/pq
    go get -u github.com/xuri/excelize/v2
    go get -u github.com/gin-gonic/gin

    # TODO create binary(linux) or .exe(windows) temp file and run it
    go run main.go

    # TODO create binary(linux) or .exe(windows) file
    go build main.go
    go build -o x.exe -C bar
    """
    pass

def web():
    """
    cd ~/Downloads
    mkdir gin_rest_api
    go mod init github.com/bogdandrienko/gin_rest_api
    cd gin_rest_api
    nano main.go

    <TODO file>
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
    </TODO file>

    go get
    go run main.go
    # browse http://127.0.0.1:8080/books
    """
    pass
