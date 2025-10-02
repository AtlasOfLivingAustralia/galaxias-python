import os
import galaxias

def test_default_markdown():
    galaxias.use_metadata_template()
    assert os.path.isfile('metadata.md')

def test_rename_markdown():
    galaxias.use_metadata_template(metadata_md='testing.md')
    assert os.path.isfile('testing.md')

def test_directory():
    galaxias.use_metadata_template(working_dir='testing')
    assert os.path.isfile('{}/{}'.format('./testing','metadata.md'))

def test_directory_rename_markdown():
    galaxias.use_metadata_template(metadata_md='testing.md',working_dir='testing')
    assert os.path.isfile('testing/testing.md')

def test_xml():
    if os.path.isfile('metadata.md'):
        os.remove('metadata.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    assert os.path.isfile('metadata.md')

def test_xml_rename():
    if os.path.isfile('testing.md'):
        os.remove('testing.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    assert os.path.isfile('testing.md')

def test_xml_change_working_dir():
    if os.path.isfile('testing/metadata.md'):
        os.remove('testing/metadata.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    assert os.path.isfile('testing/metadata.md')

def test_xml_rename_change_working_dir():
    if os.path.isfile('testing/testing.md'):
        os.remove('testing/testing.md')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    assert os.path.isfile('testing/testing.md')