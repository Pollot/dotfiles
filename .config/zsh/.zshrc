# History
HISTFILE=~/.cache/zsh
HISTSIZE=10000
SAVEHIST=10000

# Vi keybindings
bindkey -v

# Autosuggestions: https://github.com/zsh-users/zsh-autosuggestions
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

# Syntax highlighting: https://github.com/zsh-users/zsh-syntax-highlighting
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
# Paths
ZSH_HIGHLIGHT_STYLES[path]='fg=blue'
# Precommand modifiers
ZSH_HIGHLIGHT_STYLES[precommand]='fg=yellow'

# Directory history: https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dirhistory
# Alt + left -> past directory ; Alt + right -> recent directory
# Alt + down -> child directory ; Alt + up -> parent directory
source ~/.config/zsh/dirhistory.zsh

# Sudo: https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/sudo
# Press ESC x 2 to add sudo at the beggining
source ~/.config/zsh/sudo.zsh

# Neofetch
neofetch

# Prompt
eval "$(starship init zsh)"
