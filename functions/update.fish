function update
    brew update; brew upgrade; brew cleanup -s;
    conda update -y --all; conda clean -y --all;
end
