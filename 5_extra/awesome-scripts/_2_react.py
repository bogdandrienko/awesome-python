def setup_lang_and_ide():
    """
    # TODO update system repositories and dependencies
    sudo apt-get update -y && sudo apt update -y
    sudo apt-get upgrade -y && sudo apt upgrade -y

    # TODO install lang
    curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
    source ~/.bashrc
    nvm ls-remote
    nvm install 18.16.0

    # TODO install ide
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
    cd ~/Downloads
    npx -y create-react-app react_app --template redux-typescript
    npx -y create-react-app react_app --template pwa-typescript

    npm install prettier axios react-redux react-router-dom
    npm install react-bootstrap react-router-bootstrap react-player

    npm install
    npm init

    npm start
    npm run build
    """
    pass
