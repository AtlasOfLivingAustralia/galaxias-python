import os
import galaxias


'''
def use_metadata(metadata_md='metadata.md',
                 working_dir='./',
                 publishing_dir='./data-publish',
                 eml_xml='eml.xml'):
                 '''

def test_write_eml_default():
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    galaxias.use_metadata_template()
    galaxias.use_metadata()
    assert os.path.isfile('data-publish/eml.xml')

def test_write_eml_markdown():
    if os.path.exists('eml.xml'):
        os.remove('eml.xml')
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    galaxias.use_metadata_template(metadata_md='testing.md')
    galaxias.use_metadata(metadata_md='testing.md')
    assert os.path.isfile('data-publish/eml.xml')

def test_write_eml_directory():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    galaxias.use_metadata_template(working_dir='testing')
    galaxias.use_metadata(working_dir='testing')
    assert os.path.isfile('./data-publish/eml.xml')

def test_write_eml_markdown_directory():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('data-publish/eml.xml'):
        os.remove('data-publish/eml.xml')
    galaxias.use_metadata_template(working_dir='testing',metadata_md='testing.md')
    galaxias.use_metadata(working_dir='testing',metadata_md='testing.md')
    assert os.path.isfile('./data-publish/eml.xml')

def test_write_eml_markdown_directory_publish():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('data-publish/eml.xml'):
        os.remove('data-publish/eml.xml')
    galaxias.use_metadata_template(working_dir='testing',metadata_md='testing.md')
    galaxias.use_metadata(working_dir='testing',metadata_md='testing.md',publishing_dir='test-publish')
    assert os.path.isfile('./test-publish/eml.xml')

def test_write_eml_directory_eml_xml():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('data-publish/testing.xml'):
        os.remove('data-publish/testing.xml')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    galaxias.use_metadata(working_dir='testing',eml_xml='testing.xml')
    assert os.path.isfile('data-publish/testing.xml')

def test_write_eml_markdown_eml_xml():
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    if os.path.exists('data-publish/testing.xml'):
        os.remove('data-publish/testing.xml')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    galaxias.use_metadata(metadata_md='testing.md',eml_xml='testing.xml')
    assert os.path.isfile('data-publish/testing.xml')

def test_write_eml_markdown_directory_xml_rename():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('data-publish/testing.xml'):
        os.remove('data-publish/testing.xml')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    galaxias.use_metadata(working_dir='testing',metadata_md='testing.md',eml_xml='testing.xml')
    assert os.path.isfile('data-publish/testing.xml')

def test_write_eml_markdown_directory_xml_rename_pubdir():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('test-publish/testing.xml'):
        os.remove('test-publish/testing.xml')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    galaxias.use_metadata(working_dir='testing',metadata_md='testing.md',eml_xml='testing.xml',publishing_dir='test-publish')
    assert os.path.isfile('test-publish/testing.xml')