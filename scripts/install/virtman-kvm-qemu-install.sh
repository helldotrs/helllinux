yay -S virt-manager qemu libvirt
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
sudo usermod -aG libvirt $(whoami)
echo 'helllinux: you have been added to new usergroup, please restart TE for change to start taking effect'
