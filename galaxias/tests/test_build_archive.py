import galaxias
import os
import shutil
import zipfile
from build_test_data import build_occurrences,build_events

def test_build_archive_occurrences():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_occurrences()
    galaxias.build_archive()
    archive = zipfile.ZipFile('dwca.zip')
    names = archive.namelist()
    assert all(x in names for x in ['data-publish/occurrences.csv','data-publish/meta.xml','data-publish/eml.xml'])

def test_build_archive_occurrences_xml_url():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_occurrences(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    galaxias.build_archive(print_report=True)
    archive = zipfile.ZipFile('dwca.zip')
    names = archive.namelist()
    assert all(x in names for x in ['data-publish/occurrences.csv','data-publish/meta.xml','data-publish/eml.xml'])

def test_build_archive_events():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_events()
    galaxias.build_archive()
    archive = zipfile.ZipFile('dwca.zip')
    names = archive.namelist()
    assert all(x in names for x in ['data-publish/occurrences.csv','data-publish/events.csv','data-publish/meta.xml','data-publish/eml.xml'])

def test_build_archive_events_xml_url():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_events(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    galaxias.build_archive()
    archive = zipfile.ZipFile('dwca.zip')
    names = archive.namelist()
    assert all(x in names for x in ['data-publish/occurrences.csv','data-publish/events.csv','data-publish/meta.xml','data-publish/eml.xml'])