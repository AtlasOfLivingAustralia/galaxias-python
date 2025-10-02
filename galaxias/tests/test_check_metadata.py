import os
import galaxias

def test_check_metadata_default():
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    galaxias.use_metadata_template()
    galaxias.use_metadata()
    check =  galaxias.check_metadata()
    assert check is None

def test_check_metadata_markdown():
    if os.path.exists('eml.xml'):
        os.remove('eml.xml')
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    galaxias.use_metadata_template(metadata_md='testing.md')
    galaxias.use_metadata()
    check = galaxias.check_metadata()
    assert check is None

def test_check_metadata_directory():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    galaxias.use_metadata_template(working_dir='testing')
    galaxias.use_metadata()
    check = galaxias.check_metadata()
    assert check is None

def test_check_metadata_markdown_directory():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    galaxias.use_metadata_template(working_dir='testing',metadata_md='testing.md')
    galaxias.use_metadata()
    check = galaxias.check_metadata()
    assert check is None

def test_check_metadata_directory_eml_xml():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    galaxias.use_metadata()
    check = galaxias.check_metadata()
    assert check is None

def test_check_metadata_markdown_eml_xml():
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    if os.path.exists('testing.xml'):
        os.remove('testing.xml')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    galaxias.use_metadata()
    check = galaxias.check_metadata()
    assert check is None

def test_check_metadata_markdown_directory_xml_rename():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    galaxias.use_metadata_template(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    galaxias.use_metadata()
    check = galaxias.check_metadata()
    assert check is None