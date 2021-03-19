set nocompatible
filetype indent plugin on

" Better command-line completion
set wildmenu

" Show partial commands in the last line of the screen
set showcmd

" Allow backspacing over autoindent, line breaks and start of insert action
set backspace=indent,eol,start

set autoindent
set ruler
set laststatus=2
set confirm
set mouse=a

set cmdheight=2
set number
set shiftwidth=4
set tabstop=4
set expandtab

" Map Y to act like D and C, i.e. to yank until EOL, rather than act as yy,
map Y y$

syntax on
set hlsearch
set confirm

set autowriteall
au FocusLost * :wa

set nowrap
set fdm=indent
set clipboard=unnamed
set undofile

" show cursor line in insert mode
let &t_SI.="\e[5 q"
let &t_SR.="\e[4 q"
let &t_EI.="\e[1 q"

set ttimeoutlen=0
set undodir=/home/wangl/.vim/undofiles

" lhs comments
map ,# :s/^/#/<CR>:nohlsearch<CR>
map ,/ :s/^/\/\//<CR>:nohlsearch<CR>
map ,c :s/^\/\/\\|^--\\|^> \\|^[#"%!;]//<CR>:nohlsearch<CR>
" wrapping comments
map ,< :s/^\(.*\)$/<!-- \1 -->/<CR>:nohlsearch<CR>
map ,d :s/^\([/(]\*\\|<!--\) \(.*\) \(\*[/)]\\|-->\)$/\2/<CR>:nohlsearch<CR>

if has("win32")
    set guifont=Consolas:h12
    set guioptions -=m
    set guioptions -=T
    set columns=120
    set lines=40
    winpos 700 200
    set shell=C:\Windows\Sysnative\wsl.exe
    set shellpipe=|
    set shellredir=>
    set shellcmdflag=
    set undodir=C:\vim\undodir
endif

set notimeout ttimeout timeoutlen=100

" map esc and scrool up to enter normal mode in vim terminal
function! ExitNormalMode()
    unmap <buffer> <silent> <RightMouse>
        call feedkeys("a")
endfunction
function! EnterNormalMode()
    if &buftype == 'terminal' && mode('') == 't'
        call feedkeys("\<c-w>N")
        call feedkeys("\<c-y>")
        map <buffer> <silent> <RightMouse> :call ExitNormalMode()<CR>
    endif
endfunction
tmap <silent> <ScrollWheelUp> <c-w>:call EnterNormalMode()<CR>
"

nmap <leader>\ <Plug>SlimeSendCell
let g:slime_python_ipython = 1
let g:slime_target = "vimterminal"
let g:slime_cell_delimiter = "#%%"
