import galaxias
import os
import shutil
import zipfile
from build_test_data import build_occurrences,build_events

def test_check_directory_occurrences():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_occurrences()
    galaxias.build_archive()
    result = galaxias.check_directory(print_report=True)
    assert result is True

#'''
def test_check_directory_occurrences_xml_url():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    build_occurrences(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    galaxias.build_archive()
    result = galaxias.check_directory(print_report=True)
    assert result is True
#'''
#'''
def test_check_directory_events():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_events()
    galaxias.build_archive()
    result = galaxias.check_directory()
    assert result is True
#'''
def test_check_directory_events_xml_url():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_events(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    galaxias.build_archive()
    result = galaxias.check_directory()
    assert result is True
#'''