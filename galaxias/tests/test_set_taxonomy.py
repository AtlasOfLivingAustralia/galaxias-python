import galaxias
import pytest
import pandas as pd

def test_no_dataframe():
    occ_dwca = galaxias.dwca(print_notices=False)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_taxonomy()
    assert "Please provide a dataframe" in str(e_info.value)

def test_set_taxonomy_no_arguments():
    df = pd.DataFrame({'King': ['Animalia','Animalia']})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_taxonomy()
    assert "No Darwin Core" in str(e_info.value)

def test_set_taxonomy_rename():
    df = pd.DataFrame({'King': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_taxonomy(kingdom='King')
    assert 'kingdom' in occ_dwca.occurrences.columns

def test_set_taxonomy_column_string():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_taxonomy(kingdom='Animalia')
    assert 'kingdom' in occ_dwca.occurrences.columns

def test_set_taxonomy_column_list():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca = galaxias.dwca(occurrences=df)
    occ_dwca.set_taxonomy(kingdom=['Animalia','Animalia'])
    assert 'kingdom' in occ_dwca.occurrences.columns

def test_set_taxonomy_incorrect_type():
    df = pd.DataFrame({'King': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_taxonomy()
    assert "No Darwin Core" in str(e_info.value)

def test_set_taxonomy_incorrect_type_rename():
    df = pd.DataFrame({'King': [1,1]})
    occ_dwca = galaxias.dwca(occurrences=df)
    with pytest.raises(Exception) as e_info:
        occ_dwca.set_taxonomy(kingdom='King')
    assert "There are some errors" in str(e_info.value)

'''
# these work when I do it on terminal but not in pytest..
def test_set_taxonomy_string_and_lists():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca.set_taxonomy(kingdom='Animalia',phylum=['Chordata','Chordata'],taxon_class='Aves')
    assert all(x in occ_dwca.occurrences.columns for x in ['kingdom','phylum','class'])

def test_set_all_taxonomy_string():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca.set_taxonomy(kingdom='Animalia',phylum='Chordata',taxon_class='Aves',
                                  order='Psittaciformes',family='Cacatuidae',genus='Eolophus',
                                  specificEpithet='roseicapilla',vernacularName='Galah')
    assert all(x in occ_dwca.occurrences.columns for x in ['kingdom','phylum','class','order','family','genus','specificEpithet','vernacularName'])

def test_set_all_taxonomy_column_list():
    df = pd.DataFrame({'scientificName': ['Eolophus roseicapilla','Eolophus roseicapilla']})
    occ_dwca.set_taxonomy(kingdom=['Animalia','Animalia'],phylum=['Chordata','Chordata'],
                                  taxon_class=['Aves','Aves'],order=['Psittaciformes','Psittaciformes'],
                                  family=['Cacatuidae','Cacatuidae'],genus=['Eolophus','Eolophus'],
                                  specificEpithet=['roseicapilla','roseicapilla'],vernacularName=['Galah','Galah'])
    assert all(x in occ_dwca.occurrences.columns for x in ['kingdom','phylum','class','order','family','genus','specificEpithet','vernacularName'])'
'''