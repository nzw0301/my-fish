function ms
    ssh kserver2 /mslab/link/ms $argv
    ssh server2 /home/local/bin/ms-script/ms $argv
end
