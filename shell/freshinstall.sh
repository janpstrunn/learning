# Must

echo "Getting ready!"
echo "Some security improvements will be done before starting!"
echo "Setting up DoH"
sh -c "$(curl -sL https://nextdns.io/install)"
echo "Setting up a firewall"
sudo pacman -S ufw
echo "Enabling the firewall"
sudo ufw enable

# Essential

echo "Installing wanted softwares"
sudo pacman -S libreoffice neofetch ranger ueberzug ffmpeg ffmpegthumbnailer git mpv nitrogen gimp obsidian rsync rclone flatpak gocryptfs keepassxc neovim picom starship gvfs mtpfs scrcpy tmux bash-completion tumbler audacity shotcut obs-studio handbrake  lxappearance thunar thunar-volman thunar archive-plugin usbutils gnu-free-fonts ttf-dejavu ttf-dejavu-nerd fuse2 polkit udiskie udisks2 deltachat-desktop curtail converseen flameshot python-psutil rhythmbox zoxide

# Optional 
# sudo pacman -S lynx thunderbird cmatrix

echo "Installing yay"
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

echo "Removing Ristretto and Parole"
sudo pacman -Rns ristretto parole

echo "Installing yay softwares"
yay -S jdownloader2
yay -S autokey-gtk
yay -S qtile-extras

echo "Almost done!"
echo "Installing flatpak softwares"
flatpak install com.github.tchx84.Flatseal
flatpak install io.github.zen_browser.zen
flatpak install org.nomacs.ImageLounge
flatpak install org.keepassxc.KeePassXC
echo "We are done! Enjoy!"
echo "Extra tips:"
echo "Configure the system"
echo "Check VPN configurations"
