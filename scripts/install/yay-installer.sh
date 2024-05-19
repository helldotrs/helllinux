cd ~
sudo pacman -Syu
sudo pacman -S git go
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
