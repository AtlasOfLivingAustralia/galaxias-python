# galaxias <a href="https://galaxias.ala.org.au/Python/"><img src="docs/source/_static/logo/logo.png" align="right" style="margin: 0px 10px 0px 10px;" alt="" height="138"/></a>

<!-- badges: start -->

[![pypi](https://img.shields.io/pypi/v/galaxias-python.svg)](https://pypi.org/project/galaxias-python/)

<!-- badges: end -->

## Overview

## Overview

`galaxias-python` is a Python package that helps users describe, package 
and share biodiversity information using the [‘Darwin Core’](https://dwc.tdwg.org)
data standard. It was created by the [Science & Decision Support
Team](https://labs.ala.org.au) at the [Atlas of Living
Australia](https://www.ala.org.au) (ALA).

The package is named for a genus of freshwater fish that is found only
in the Southern Hemisphere, and predominantly in Australia and New
Zealand. The logo shows a [Spotted
Galaxias](https://bie.ala.org.au/species/https://biodiversity.org.au/afd/taxa/e4d85845-3e34-4112-90a9-f954176721ec)
(*Galaxias truttaceus*) drawn by Ian Brennan.

If you have any comments, questions or suggestions, please [contact
us](mailto:support@ala.org.au).

## Installation

This package is under active development, and is not yet available on
PyPI. You can install the latest development version from GitHub with:

``` bash
git clone https://github.com/AtlasOfLivingAustralia/galaxias-python.git
cd galaxias-python/galaxias
pip install .
```

Load the package:

``` python
import galaxias
```

## Features

`galaxias-python` contains tools to:

- Create documents to describe the origin and structure of your data
  using `build_metadata()` and `build_schema()`.
- Zip up your data for sharing or publication using `build_archive()`.
- Check data for consistency with the Darwin Core standard, either
  locally using `check_archive()`, or via API using
  `validate_archive()`.

`galaxias-python` is part of a group of packages that help users publish data
using the Darwin Core standard. The other packages are:

- [`corella-python`](https://corella.ala.org.au/Python) for converting tibbles to the
  required column names
- [`delma-python`](https://delma.ala.org.au/Python) for converting markdown files to
  `xml`.

## Citing galaxias

The current recommended citation is:

> Buyan A & Westgate MJ (2025) galaxias: Standardise, Document and Share
> Biodiversity Data. Python Package version 0.1.0.

## Contributors

Developers who have contributed to `galaxias` are listed here (in
alphabetical order by surname):

Amanda Buyan ([@acbuyan](https://github.com/acbuyan))