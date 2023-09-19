# galaxias

Code repository for the galaxias-python package, which will create Darwin Core Archives and ship them to the ALA

## Installation

```bash
$ pip install galaxias
```

## Usage

```
from galaxias import CsvFileType
from galaxias import DwcaHandler
core_csv = CsvFileType(files=['/tmp/occurrence.csv'], type='occurrence', keys=['occurrenceID'])
ext_csvs = [CsvFileType(files=['/tmp/multimedia.csv'], type='multimedia')]

DwcaHandler.create_dwca(core_csv=core_csv, ext_csv_list=ext_csvs, output_dwca_path='/tmp/dwca.zip')
```


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`galaxias` was created by Atlas of Living Australia. It is licensed under the terms of the GNU General Public License v3.0 license.

## Credits

`galaxias` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
