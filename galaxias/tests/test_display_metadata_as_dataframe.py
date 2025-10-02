import os
import galaxias
import pandas as pd

'''
def display_metadata_as_dataframe(metadata_md='metadata.md',
                                  working_dir='./'):
'''

def test_display_metadata_as_dataframe_default():
    galaxias.use_metadata_template()
    df = galaxias.display_metadata_as_dataframe()
    assert isinstance(df,pd.DataFrame)

def test_display_metadata_as_dataframe_specify_markdown():
    galaxias.use_metadata_template(metadata_md='testing.md')
    df = galaxias.display_metadata_as_dataframe(metadata_md='testing.md')
    assert isinstance(df,pd.DataFrame)

def test_display_metadata_as_dataframe_specify_directory():
    galaxias.use_metadata_template(working_dir='testing')
    df = galaxias.display_metadata_as_dataframe(working_dir='testing')
    assert isinstance(df,pd.DataFrame)

def test_display_metadata_as_dataframe_both_markdown_directory():
    galaxias.use_metadata_template(working_dir='testing',metadata_md='testing.md')
    df = galaxias.display_metadata_as_dataframe(working_dir='testing',metadata_md='testing.md')
    assert isinstance(df,pd.DataFrame)

def test_display_metadata_as_dataframe_xml():
    if os.path.isfile('metadata.md'):
        os.remove('metadata.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    df = galaxias.display_metadata_as_dataframe()
    assert isinstance(df,pd.DataFrame)

def test_display_metadata_as_dataframe_xml_rename():
    if os.path.isfile('testing.md'):
        os.remove('testing.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    df = galaxias.display_metadata_as_dataframe(metadata_md='testing.md')
    assert isinstance(df,pd.DataFrame)

def test_display_metadata_as_dataframe_xml_change_working_dir():
    if os.path.isfile('testing/metadata.md'):
        os.remove('testing/metadata.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    df = galaxias.display_metadata_as_dataframe(working_dir='testing')
    assert isinstance(df,pd.DataFrame)

def test_display_metadata_as_dataframe_xml_rename_change_working_dir():
    if os.path.isfile('testing/testing.md'):
        os.remove('testing/testing.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    df = galaxias.display_metadata_as_dataframe(working_dir='testing',metadata_md='testing.md')
    assert isinstance(df,pd.DataFrame)