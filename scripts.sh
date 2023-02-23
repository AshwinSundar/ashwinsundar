# bash scripts.sh createPage
## $1 - name of page
createPage() {
    # TO DO
    # add path argument
    inp=$(tr '[:upper:]' '[:lower:]' <<< $1)
    cp templates/htmlTemplate.txt $inp.html
}

# bash scripts.sh createBlogPost
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
    compileSass
    compileMarkdown
    compileMusicPages
}

# bash scripts.sh deploy
deploy() {
    compile
    git add . 
    read -p 'Enter commit message: ' msg
    git commit -m "$msg"
    git push
    sleep 3
    gh run watch
}

# bash scripts.sh compileSass
# settings.json -> emeralwalk.runonsave(.scss)
compileSass() {
    # TO DO - create script that only updates one file, instead of everything
    files=$(find styles -name "*.scss")
    for f in $files; do
        sass $f styles/compiled/$(basename "${f%.*}").css
    done
    echo "Sass files compiled"
}

# bash scripts.sh compileMarkdown
# settings.json -> emeralwalk.runonsave(.md)
compileMarkdown() {
    # DONE - add body/head tags so VSCode Live Server will update immediately when html file is updated by this script
    # TO DO - create script that only updates one file, instead of everything
    files=$(find blog -name "*.md")
    for f in $files; do
        pandoc -f markdown $f > blog/compiled/$(basename "${f%.*}").html
        head=$(head -n10 templates/blogTemplate.txt) # first n = 7 lines 
        tail=$(tail -n2 templates/blogTemplate.txt) # last n = 2 lines
        echo $head | cat - blog/compiled/$(basename "${f%.*}").html > temp && mv temp blog/compiled/$(basename "${f%.*}").html
        echo $tail >> blog/compiled/$(basename "${f%.*}").html
    done
    echo "Markdown files compiled"
}

compileMusicPages() {
    IFS=$'\n' ## Internal File Separator. Changes from space to nl
    cd music/
    files=$(find . -name "*.mp3")
    for f in $files; do
        htmlFileName=$(echo "$f" | sed 's/mp3/html/g')
        songName=$(echo "$f" | sed 's/.mp3//g' | sed 's/.\///g') ## music\/// means replace the string "music/" (escaped  with \) with nothing "//"
        content='<div>'$songName'</div><audio controls controlsList="nodownload noplaybackrate"><source src="'$f'"/></audio>'
        touch $htmlFileName
        echo $content > $htmlFileName
    done
    echo "Music pages compiled"
}


"$@"
