set nocompatible              " 关闭和vi的兼容 
filetype off                  " 打开文件时，不识别文件类型  

" 常用设置
set tabstop=4
set shiftwidth=4
set fileformat=unix
set fileencodings=utf-8,gb2312,gbk,cp936,big5,ucs-bom
set encoding=utf-8
set termencoding=utf-8
set fileencoding=utf-8
" 显示命名字符
set showcmd
" 自动缩进,设置每次单击Enter键后，光标移动到下一行时与上一行的起始字符对齐
set autoindent
" 语法检查
syntax on
" 设置检查的行数，准确的语法高亮和屏幕刷新速度的折衷
syntax sync minlines=256
" 文件高亮的最大列数, 超出此列数后续行不一定能正确高亮
set synmaxcol=200
" 突出显示当前行
set cursorline
" 语法高亮
set hls 
" 显示行号
set nu
" 显示当前模式
set showmode
" 实时显示搜索结果
set incsearch
" 忽略大小写
set ignorecase
" 高亮搜索结果
set hlsearch
" 编辑下面出现状态栏，显示当前编辑是第几行，第几列及当前vim的模式
set laststatus=2
set ruler
" 由于关闭了和vi相关的兼容，想用退格键将字段缩进的删掉，必须设置这个选项 
set backspace=indent,eol,start

" 插件管理
set rtp+=~/.vim/bundle/vundle/    " 载入特定目录插件
call vundle#rc()

" 用vundle管理插件
Bundle 'gmarik/vundle'            

" 文件浏览插件，:NERDTree或者配置的快捷键F2开启，快捷键可以根据情况自己配置
" 导入插件用Bundle，可以用Plugin替换，两者效果一样
Bundle 'scrooloose/nerdtree'      
let NERDTreeWinPos='left'          " 文件目录在左边显示，可以自己设置为right 右边显示
let NERDTreeWinSize=20             " 窗口大小
map <F2> :NERDTreeToggle<CR>       


" 自动代码补全
Bundle 'Shougo/neocomplete.vim'
" 配置直接拷贝官方的例子 https://github.com/Shougo/neocomplete.vim 
let g:acp_enableAtStartup = 0
" Use neocomplete.
let g:neocomplete#enable_at_startup = 1
" Use smartcase.
let g:neocomplete#enable_smart_case = 1
" Set minimum syntax keyword length.
let g:neocomplete#sources#syntax#min_keyword_length = 3
let g:neocomplete#lock_buffer_name_pattern = '\*ku\*'

" Define dictionary.
let g:neocomplete#sources#dictionary#dictionaries = {
    \ 'default' : '',
    \ 'vimshell' : $HOME.'/.vimshell_hist',
    \ 'scheme' : $HOME.'/.gosh_completions'
        \ }

" Define keyword.
if !exists('g:neocomplete#keyword_patterns')
    let g:neocomplete#keyword_patterns = {}
endif
let g:neocomplete#keyword_patterns['default'] = '\h\w*'

" Plugin key-mappings.
inoremap <expr><C-g>     neocomplete#undo_completion()
inoremap <expr><C-l>     neocomplete#complete_common_string()

" Recommended key-mappings.
" <CR>: close popup and save indent.
inoremap <silent> <CR> <C-r>=<SID>my_cr_function()<CR>
function! s:my_cr_function()
  return (pumvisible() ? "\<C-y>" : "" ) . "\<CR>"
  " For no inserting <CR> key.
  "return pumvisible() ? "\<C-y>" : "\<CR>"
endfunction
" <TAB>: completion.
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"
" <C-h>, <BS>: close popup and delete backword char.
inoremap <expr><C-h> neocomplete#smart_close_popup()."\<C-h>"
inoremap <expr><BS> neocomplete#smart_close_popup()."\<C-h>"
" Close popup by <Space>.
"inoremap <expr><Space> pumvisible() ? "\<C-y>" : "\<Space>"

" AutoComplPop like behavior.
"let g:neocomplete#enable_auto_select = 1

" Shell like behavior(not recommended).
"set completeopt+=longest
"let g:neocomplete#enable_auto_select = 1
"let g:neocomplete#disable_auto_complete = 1
"inoremap <expr><TAB>  pumvisible() ? "\<Down>" : "\<C-x>\<C-u>"

" Enable omni completion.
autocmd FileType css setlocal omnifunc=csscomplete#CompleteCSS
autocmd FileType html,markdown setlocal omnifunc=htmlcomplete#CompleteTags
autocmd FileType javascript setlocal omnifunc=javascriptcomplete#CompleteJS
autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
autocmd FileType xml setlocal omnifunc=xmlcomplete#CompleteTags

" Enable heavy omni completion.
if !exists('g:neocomplete#sources#omni#input_patterns')
  let g:neocomplete#sources#omni#input_patterns = {}
endif
let g:neocomplete#sources#omni#input_patterns.perl = '\h\w*->\h\w*\|\h\w*::'

