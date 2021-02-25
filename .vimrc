set encoding=utf-8
set t_Co=256

set number
set cursorline
set showmode

syntax on
set autoindent
set expandtab
set softtabstop=2
set tabstop=2
set wrap
set linebreak
set ruler
set showmatch
set hlsearch
set ignorecase
set smartcase
set backspace=2

set mouse=a

set viminfo='10,\"100,:20,%,n~/.viminfo 
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif
