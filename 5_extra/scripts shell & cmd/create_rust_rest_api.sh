# install rust
sudo apt update -y && sudo apt-get update -y
sudo apt upgrade -y && sudo apt-get upgrade -y
sudo apt install curl build-essential gcc make -y
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# set 1 
source "$HOME/.cargo/env"

# install rust ide
sudo snap install intellij-idea-ultimate --classic

# create rust project
cd ~
cd Downloads
cargo new rust-rest-api
cd rust-rest-api

nano Cargo.toml
<file>
[dependencies]
actix-web = "4"
</file>

nano src/main.rs
<file>
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
</file>
cargo run
# browse http://127.0.0.1:8080/
cargo build