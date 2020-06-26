function tc
    set data "*.log" "*.xdv" "*.aux" "main.out" "*.bbl" "*.blg" "*.fdb_latexmk" "*.fls" "*.dvi" ".ipynb_checkpoints" "auto" "__pycache__" "*.egg-info" "dist" "build" "*.pyc" "*.cpython-35m-darwin.so" ".pytest_cache*" "*\[Conflict\]*" "*.synctex.gz" "*.spl" "*.toc" "*.bcf"
    for val in $data
        if string match $argv "d" > /dev/null ;
            find . -name $val -exec rm -r "{}" \;
        else
            find . -name $val;
        end
    end
end
