function crop
    for f in *.pdf
        pdfcrop "$f" "$f"
    end
end
