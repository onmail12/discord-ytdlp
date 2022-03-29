git add . -f
echo -n "Commit: "
read commit
git commit -am $commit
git push heroku master