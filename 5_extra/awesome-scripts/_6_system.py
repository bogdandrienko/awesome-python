def ubuntu_first_setup():
    """
    # TODO basic
    # create ubuntu VM (2023_01_05_ubuntu_22_04_desktop)
    # change VM settings (network, ram, core, shared folder, shared clipboard...)
    # setup ubuntu desktop lts (Normal installation (ubuntu + ubuntu-PC) + download updates + install third-party software)

    # TODO update system
    # update system with app ubuntu-software

    # TODO insert vbox-guest-additions
    # insert guest additions iso => Files >> CD Drive (VBOX_GAs_6.1.32) >> autorun.sh (Right-click) >> Run as a Program
    sudo adduser ubuntu vboxsf
    # eject guest additions

    # TODO update system repositories and dependencies
    sudo apt-get update -y && sudo apt update -y
    sudo apt-get upgrade -y && sudo apt upgrade -y

    # TODO customization
    # set dark theme and color (settings -> appearance)
    # disable show personal folder (settings -> appearance)
    # set panel to bottom (settings -> appearance -> dock)
    # enable Auto-hide the Dock
    # set backgroud image (settings -> backgroud)
    # set scree blank 1 min (settings -> power)
    # remove apps from panel
    # add russian language (settings -> region & language)
    # add russian to keyboard (settings -> keyboard)
    sudo apt install  gnome-shell-extensions gnome-shell-extension-manager -y
    # >> Apps >> Extension manager >> Browse >> Hide Top Bar >> Install >> Apps >> gnome-shell-extensions (disable all checkboxes without 'show in overview')

    # TODO install modules
    # main modules

    sudo apt-get install -y curl wget git

    # TODO old/ sudo apt-get install -y curl wget git build-essential gcc make libpq-dev unixodbc-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev gettext

    # TODO additional modules
    sudo apt-get install -y nginx gunicorn docker-compose postgresql postgresql-contrib redis openssh-server
    sudo snap install --classic certbot gh

    # TODO install google-chrome
    cd ~/Downloads
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    sudo rm google-chrome-stable_current_amd64.deb

    # TODO install github-desktop
    cd ~/Downloads
    sudo wget https://github.com/shiftkey/desktop/releases/download/release-3.2.1-linux1/GitHubDesktop-linux-3.2.1-linux1.deb
    sudo dpkg -i GitHubDesktop-linux-3.2.1-linux1.deb
    sudo rm GitHubDesktop-linux-3.2.1-linux1.deb

    # TODO install putty-ssh-client
    sudo apt install -y putty

    # TODO install postgresql-pgadmin4
    curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
    sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
    sudo apt-get install -y pgadmin4

    # TODO install virtualbox
    sudo apt-get install -y virtualbox virtualbox-ext-pack virtualbox-guest-additions-iso virtualbox-guest-utils dkms virtualbox-dkms

    # TODO IDE settings
    # create email on mail.ru
    # create account on jetbrains.com
    # start ide, link account, start trial
    # settings -> set font 18
    # settings -> general -> set mouse scroll change font
    # settings -> set new Ui
    # plugins -> install
    """
    pass

def ubuntu():
    """
    # TODO kill freezed process
    ps aux | grep -i apt
    sudo kill -9 6666

    # TODO enter as root user
    sudo -i

    # TODO update os
    sudo apt-get update -y && sudo apt update -y
    sudo apt-get upgrade -y && sudo apt upgrade -y

    # TODO clear terminal
    clear

    # TODO remove file
    sudo rm temp.txt

    # TODO create file
    touch file

    # TODO change file / create file
    sudo nano new.json

    # TODO move file
    sudo mv /temp1/data.json /temp2/data.json

    # TODO change file role
    sudo chmod +x

    # TODO check all dependencies
    sudo apt install -f

    # TODO reboot system
    sudo reboot

    # TODO clear cached dependencies
    sudo apt autoremove -y
    sudo apt-get autoremove -y

    # TODO ufw role
    sudo ufw allow 'Nginx Full'

    # TODO work with system workers
    sudo service nginx start

    sudo systemctl status gunicorn.service

    sudo systemctl enable --now gunicorn.service
    sudo systemctl disable gunicorn

    sudo systemctl start gunicorn
    #sudo systemctl stop gunicorn
    sudo systemctl restart gunicorn

    sudo systemctl daemon-reload

    # TODO work with openssh-server
    sudo systemctl start ssh
    sudo systemctl restart ssh

    # TODO disable swap
    free -m
    swapon -s
    swapon -show
    sudo swapoff -v /swapfile
    sudo rm -f /swapfile

    # TODO enable swap
    dd if =/dev/zero of=/swapfile bs=1024 count=1048576

    # TODO clear system cache
    # login to root user
    sudo -i
    # clear all caches (echo 1|echo 2|echo 3)
    sync; echo 3 > /proc/sys/vm/drop_caches
    """
    pass

def debian():
    """
    su
    apt install sudo
    nano /etc/sudoers
    su debian
    sudo nano /etc/apt/sources.list

    <TODO file> /etc/apt/sources.list
    .....
    deb http://deb.debian.org/debian bullseye main
    deb-src http://deb.debian.org/debian bullseye main
    deb http://http.us.debian.org/debian/ testing non-free contrib main
    .....
    </TODO file> /etc/apt/sources.list

    """
    pass

def windows_first_setup():
    """
    # TODO basic
    # create windows VM (2023_01_22_windows_10_ltsb)
    # change VM settings (network, ram, core, shared folder, shared clipboard...)
    # setup windows 10 ltsb (Normal installation (user + user-PC))

    # TODO customization
    # change personalization and audio theme
    # update system
    # insert guest-additions and install
    # install DWS and SSD Mini Tweaker
    # change performance settings
    # install all need programs
    """
    pass

def windows():
    """
    # TODO remove folder with data
    rmdir /Q /S react

    # TODO move folder with data
    move frontend/build react

    # TODO shell variables
    cd ~
    mkdir Downloads
    cd Downloads
    set /p project_variable= "Please set your project name: "
    IF "%project_variable%"=="" (set project_variable="project_folder")
    mkdir %project_variable% && cd %project_variable%
    set /p env_variable= "Please set your virtual environment name: "
    IF "%env_variable%"=="" (set env_variable="env")
    python -m venv %env_variable%
    call %env_variable%/Scripts/activate.bat
    """
    pass
