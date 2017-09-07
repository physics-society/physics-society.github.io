##  Physics Society Website

Export google sheet data to data.csv
remove all generated project and people yaml files
```
rm _projects/*
rm _people/*
```
generate project files
```
python generate_collections.py
```

Useful oneliners
```
mv ~/Downloads/Phy\ soc\ website\ data\ -\ Contact-Information.csv data.csv && rm -rf _projects/* _people/* && python generate_collections.py
git commit -m "data v$(epoch)"
```
