apt-get install pandoc
apt-get install tidy
tidy -config htmltidy.config -m index.html
bash siteScripts.sh compile