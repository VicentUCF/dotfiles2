function cdd() {
	cd "$(ls -d -- */ | fzf)" || echo "Invalid directory"
}

function j() {
	fname=$(declare -f -F _z)

	[ -n "$fname" ] || source "$DOTLY_PATH/modules/z/z.sh"

	_z "$1"
}

function recent_dirs() {
	# This script depends on pushd. It works better with autopush enabled in ZSH
	escaped_home=$(echo $HOME | sed 's/\//\\\//g')
	selected=$(dirs -p | sort -u | fzf)

	cd "$(echo "$selected" | sed "s/\~/$escaped_home/")" || echo "Invalid directory"
}

function export_apps(){
  npm list -g --depth 0 | grep -v npm >"$DOTFILES_PATH/langs/js/global_modules.txt"
  volta list all --format plain | awk '{print $2}' >"$DOTFILES_PATH/langs/js/global_modules.txt"
  pacman -Qm | awk '{print $1}' >"$DOTFILES_PATH/os/arch/yay/global_packages.txt"
  comm -23 <(pacman -Qqt | sort) <({ pacman -Qqg xorg; echo base; } | sort -u) >"$DOTFILES_PATH/os/arch/pacman/global_packages.txt"
}

function import_apps(){
  cat "$DOTFILES_PATH/langs/js/global_modules.txt" | xargs -I % volta install %
  cat "$DOTFILES_PATH/os/arch/yay/global_packages.txt" | xargs -I % yay -S %
  cat "$DOTFILES_PATH/os/arch/pacman/global_packages.txt" | xargs -I % sudo pacman -S --needed %
}

function import_private_functions() {
  for file in "$DOTFILES_PATH/shell/private-functions/"*; do
    function_name=$(basename "$file")
    eval "$function_name() {
      unset -f $function_name
      source "$file"
      $function_name \$@
    }"
  done
}