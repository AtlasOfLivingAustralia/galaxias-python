import galaxias
import os
import shutil
import pandas as pd
from build_test_data import build_events,build_occurrences

def test_use_schema_occurrences():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_occurrences()
    galaxias.use_schema()
    assert os.path.isfile('./data-publish/meta.xml')
#'''
def test_use_schema_occurrences_rename():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_occurrences()
    galaxias.use_schema(schema='test.xml')
    assert os.path.isfile('./data-publish/test.xml')

def test_use_schema_events():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_events()
    # now write schema
    galaxias.use_schema()
    assert os.path.isfile('./data-publish/meta.xml')

def test_use_schema_events_rename():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    if os.path.exists('dwca.zip'):
        os.remove('dwca.zip')
    build_events()
    # now write schema
    galaxias.use_schema(schema='test.xml')
    assert os.path.isfile('./data-publish/test.xml')
#'''