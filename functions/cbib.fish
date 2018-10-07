function cbib
    if not test -e ~/.config/fish/functions/extract_used_bib_entries.py
        wget https://raw.githubusercontent.com/nzw0301/my-fish/master/functions/extract_used_bib_entries.py -P ~/.config/fish/functions
    end
    python ~/.config/fish/functions/extract_used_bib_entries.py $argv;
end
