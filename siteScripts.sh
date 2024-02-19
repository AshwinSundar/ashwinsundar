createBlogPost() {
    inp=$(tr '[:upper:]' '[:lower:]' <<< $1)
    for f in "blog"/*; do
        if [ "$inp.md" == $(basename $f) ]; then
            echo "file already exists"
            exit 0
        fi
    done

    # cp templates/blogTemplate.txt drafts/$inp.md
    touch drafts/$inp.md
    echo "New blog post created at /drafts/$inp.md"
}

compile() {
    compileMarkdown
    compileTailwind
}

compileMarkdown() {
    # DONE - add body/head tags so VSCode Live Server will update immediately when html file is updated by this script
    # TO DO - create script that only updates one file, instead of everything
    files=$(find blog -name "*.md")
    for f in $files; do
        output_name=blog/compiled/$(basename "${f%.*}").html
        pandoc -s -f markdown --css="" $f > $output_name
        head=$(head -n10 templates/blogTemplate.html) # first n = 10 lines 
        tail=$(tail -n2 templates/blogTemplate.html) # last n = 2 lines
        echo $head | cat - blog/compiled/$(basename "${f%.*}").html > temp && mv temp blog/compiled/$(basename "${f%.*}").html
        echo $tail >> blog/compiled/$(basename "${f%.*}").html
    done
    echo "Markdown files compiled"
}

compileTailwind() {
    tailwind -i styles/tailwind.css -o styles/o.tailwind.css
    echo "Tailwind compiled"
}

live() {
    live-server &
    tailwind -i styles/tailwind.css -o styles/o.tailwind.css --watch
}

"$@"