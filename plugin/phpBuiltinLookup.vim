if exists("g:loaded_phpBuiltinLookup") || &cp
  finish
endif

let g:loaded_phpBuiltinLookup = "0.1.0"
let s:keepcpo                  = &cpo
set cpo&vim

let s:plugindir = expand('<sfile>:p:h:h')
let s:functionsfile = s:plugindir . '/functions'

let &cpo = s:keepcpo
unlet s:keepcpo

if !exists('g:phpBuiltinLookup_map_keys')
    let g:phpBuiltinLookup_map_keys = 1
endif

if !exists('g:phpBuiltinLookup_map_prefix')
    let g:phpBuiltinLookup_map_prefix = '<leader>'
endif

if !filereadable(s:functionsfile)
    echo "[phpInternalLookup] 'functions' file doesn't exist, please follow instructions in the README"
    echo "[phpInternalLookup] Disabled until fixed"

    finish
endif

if g:phpBuiltinLookup_map_keys
    execute "autocmd FileType php inoremap <buffer> " . g:phpBuiltinLookup_map_prefix . "u <C-o>:PHPBuiltinLookup<CR>"
    execute "autocmd FileType php nnoremap <buffer> " . g:phpBuiltinLookup_map_prefix . "u :PHPBuiltinLookup<CR>"
endif

command PHPBuiltinLookup :call <SID>Lookup()

fun! <SID>Lookup()
   let result = system("grep ' " . expand("<cword>") . " ' " . s:functionsfile)
   echo substitute(result, '\n', '', '')
endfun
