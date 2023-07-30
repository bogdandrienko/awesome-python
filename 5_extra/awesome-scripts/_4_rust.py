def setup_lang_and_ide():
    """
    # TODO update system repositories and dependencies
    sudo apt-get update -y && sudo apt update -y
    sudo apt-get upgrade -y && sudo apt upgrade -y

    # TODO install lang
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    # todo set 1
    source "$HOME/.cargo/env"

    # TODO install ide
    sudo snap install intellij-idea-ultimate --classic
    sudo snap install code --classic
    """

def project():
    """
    # TODO create new project
    cd ~/Downloads
    cargo new rust_app
    cd rust_app
    touch main.rs

    # TODO create binary(linux) or .exe(windows) temp file and run it
    cargo run

    # TODO create binary(linux) or .exe(windows) file
    cargo build

    # TODO run file
    source main
    """
    pass

def web():
    """
    # TODO create rust project
    cd ~/Downloads
    cargo new actix_rest_api
    cd actix_rest_api
    nano Cargo.toml

    <TODO file>
    ........
    [dependencies]
    actix-web = "4"
    </TODO file>

    nano src/main.rs

    <TODO file>
    use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};

    #[get("/")]
    async fn hello() -> impl Responder {
        HttpResponse::Ok().body("Hello world!")
    }

    #[post("/echo")]
    async fn echo(req_body: String) -> impl Responder {
        HttpResponse::Ok().body(req_body)
    }

    async fn manual_hello() -> impl Responder {
        HttpResponse::Ok().body("Hey there!")
    }

    #[actix_web::main]
    async fn main() -> std::io::Result<()> {
        HttpServer::new(|| {
            App::new()
                .service(hello)
                .service(echo)
                .route("/hey", web::get().to(manual_hello))
        })
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
    }
    </TODO file>

    cargo run
    # browse http://127.0.0.1:8080/
    """
    pass
