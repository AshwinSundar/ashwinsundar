sudo apt install pandoc
sudo apt install tidy
tidy -config htmltidy.config -m index.html
bash siteScripts.sh compile