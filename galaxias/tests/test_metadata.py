import galaxias
import pytest
import shutil
import os
import pandas as pd

# ------------------------------------
# prep for tests
# ------------------------------------
if os.path.isdir('testing'):
    shutil.rmtree('testing',ignore_errors=True)
if os.path.exists('metadata.md'):
    os.remove('metadata.md')
if os.path.exists('testing.md'):
    os.remove('testing.md')
os.mkdir('testing')

# ------------------------------------
# create_md.py
# ------------------------------------
def test_default_markdown():
    my_dwca = galaxias.dwca()
    assert os.path.isfile('{}/{}'.format(my_dwca.working_dir,'metadata.md'))

def test_rename_markdown():
    my_dwca = galaxias.dwca(metadata_md='testing.md')
    assert os.path.isfile('{}/{}'.format(my_dwca.working_dir,'testing.md'))

def test_directory():
    my_dwca = galaxias.dwca(working_dir='testing')
    assert os.path.isfile('{}/{}'.format(my_dwca.working_dir,'metadata.md'))

def test_directory_rename_markdown():
    my_dwca = galaxias.dwca(metadata_md='testing.md',working_dir='testing')
    assert os.path.isfile('testing/testing.md')

def test_xml():
    if os.path.isfile('metadata.md'):
        os.remove('metadata.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    assert os.path.isfile('metadata.md')

def test_xml_rename():
    if os.path.isfile('testing.md'):
        os.remove('testing.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    assert os.path.isfile('testing.md')

def test_xml_change_working_dir():
    if os.path.isfile('testing/metadata.md'):
        os.remove('testing/metadata.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    assert os.path.isfile('testing/metadata.md')

def test_xml_rename_change_working_dir():
    if os.path.isfile('testing/testing.md'):
        os.remove('testing/testing.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    assert os.path.isfile('testing/testing.md')

# ------------------------------------
# display_metadata_as_dataframe.py
# ------------------------------------
def test_display_metadata_as_dataframe_default():
    my_dwca = galaxias.dwca()
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_metadata_as_dataframe_specify_markdown():
    my_dwca = galaxias.dwca(metadata_md='testing.md')
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_metadata_as_dataframe_specify_directory():
    my_dwca = galaxias.dwca(working_dir='testing')
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_metadata_as_dataframe_both_markdown_directory():
    my_dwca = galaxias.dwca(working_dir='testing',metadata_md='testing.md')
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_metadata_as_dataframe_xml():
    if os.path.isfile('metadata.md'):
        os.remove('metadata.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_metadata_as_dataframe_xml_rename():
    if os.path.isfile('testing.md'):
        os.remove('testing.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_metadata_as_dataframe_xml_change_working_dir():
    if os.path.isfile('testing/metadata.md'):
        os.remove('testing/metadata.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_metadata_as_dataframe_xml_rename_change_working_dir():
    if os.path.isfile('testing/testing.md'):
        os.remove('testing/testing.md')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    df = my_dwca.display_metadata_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

# ------------------------------------
# write_eml.py
# ------------------------------------
def test_write_eml_default():
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    my_dwca = galaxias.dwca()
    my_dwca.write_eml()
    assert os.path.isfile('data-publish/eml.xml')

def test_write_eml_markdown():
    if os.path.exists('eml.xml'):
        os.remove('eml.xml')
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    my_dwca = galaxias.dwca(metadata_md='testing.md')
    my_dwca.write_eml()
    assert os.path.isfile('data-publish/eml.xml')

def test_write_eml_directory():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    my_dwca = galaxias.dwca(working_dir='testing')
    my_dwca.write_eml()
    assert os.path.isfile('data-publish/eml.xml')

def test_write_eml_markdown_directory():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('data-publish/eml.xml'):
        os.remove('data-publish/eml.xml')
    my_dwca = galaxias.dwca(working_dir='testing',metadata_md='testing.md')
    my_dwca.write_eml()
    assert os.path.isfile('data-publish/eml.xml')

def test_write_eml_directory_eml_xml():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('data-publish/testing.xml'):
        os.remove('data-publish/testing.xml')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',eml_xml='testing.xml')
    my_dwca.write_eml()
    assert os.path.isfile('data-publish/testing.xml')

def test_write_eml_markdown_eml_xml():
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    if os.path.exists('data-publish/testing.xml'):
        os.remove('data-publish/testing.xml')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md',eml_xml='testing.xml')
    my_dwca.write_eml()
    assert os.path.isfile('data-publish/testing.xml')

def test_write_eml_markdown_directory_xml_rename():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('data-publish/testing.xml'):
        os.remove('data-publish/testing.xml')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md',eml_xml='testing.xml')
    my_dwca.write_eml()
    assert os.path.isfile('data-publish/testing.xml')

# ------------------------------------
# check_metadata.py
# ------------------------------------
def test_check_metadata_default():
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    my_dwca = galaxias.dwca()
    my_dwca.write_eml()
    check = my_dwca.check_metadata()
    assert check is None

def test_check_metadata_markdown():
    if os.path.exists('eml.xml'):
        os.remove('eml.xml')
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    my_dwca = galaxias.dwca(metadata_md='testing.md')
    my_dwca.write_eml()
    check = my_dwca.check_metadata()
    assert check is None

def test_check_metadata_directory():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    my_dwca = galaxias.dwca(working_dir='testing')
    my_dwca.write_eml()
    check = my_dwca.check_metadata()
    assert check is None

def test_check_metadata_markdown_directory():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    my_dwca = galaxias.dwca(working_dir='testing',metadata_md='testing.md')
    my_dwca.write_eml()
    check = my_dwca.check_metadata()
    assert check is None

def test_check_metadata_directory_eml_xml():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    my_dwca.write_eml()
    check = my_dwca.check_metadata()
    assert check is None

def test_check_metadata_markdown_eml_xml():
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    if os.path.exists('testing.xml'):
        os.remove('testing.xml')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    my_dwca.write_eml()
    check = my_dwca.check_metadata()
    assert check is None

def test_check_metadata_markdown_directory_xml_rename():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    my_dwca = galaxias.dwca(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    my_dwca.write_eml()
    check = my_dwca.check_metadata()
    assert check is None
#'''
