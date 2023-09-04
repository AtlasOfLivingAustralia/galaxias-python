# galaxias-python
Code repository for the galaxias-python package, which will create Darwin Core Archives and ship them to the ALA

# workflow

data.csv
metadata.md

Processing data:

1. Check for duplicates
2. Check for correct column names; provide suggestions if column names incorrect and rename
3. Check format for data in each column; change it according to DwC standards
4. Write meta.xml based on polished data.csv
5. Check eml metadata and if all required fields are there
6. Write eml.xml
7. Create the DwCA itself
8. Post data to ALA (optional?)

# install development version (after pulling from repo)

poetry install .