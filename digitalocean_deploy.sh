apt install pandoc
apt install tidy
tidy -config htmltidy.config -m index.html
bash siteScripts.sh compile