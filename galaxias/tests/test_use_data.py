import galaxias
import os
import shutil
import pandas as pd

def test_use_data_mkdir():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    galaxias.use_data()
    assert os.path.isdir('./data-publish')

def test_use_data_write_occurrences():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    occurrences = pd.read_csv('../../docs/source/galaxias_user_guide/data/dummy-dataset-sb.csv')
    galaxias.use_data(occurrences=occurrences)
    assert os.path.isfile('./data-publish/occurrences.csv')

def test_use_data_write_occurrences_check_same():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    occurrences = pd.read_csv('../../docs/source/galaxias_user_guide/data/dummy-dataset-sb.csv')
    galaxias.use_data(occurrences=occurrences)
    occurrences2 = pd.read_csv('./data-publish/occurrences.csv')
    assert occurrences.equals(occurrences2)

def test_use_data_write_occurrences_rename():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    occurrences = pd.read_csv('../../docs/source/galaxias_user_guide/data/dummy-dataset-sb.csv')
    galaxias.use_data(occurrences=occurrences,occurrences_filename='test.csv')
    assert os.path.isfile('./data-publish/test.csv')

def test_use_data_write_events():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    sites = pd.read_csv('../../docs/source/galaxias_user_guide/data/sites.csv')
    galaxias.use_data(events=sites)
    assert os.path.isfile('./data-publish/events.csv')

def test_use_data_write_events_rename():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    sites = pd.read_csv('../../docs/source/galaxias_user_guide/data/sites.csv')
    galaxias.use_data(events=sites,events_filename='test.csv')
    assert os.path.isfile('./data-publish/test.csv')

def test_use_data_write_events_check_same():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    sites = pd.read_csv('../../docs/source/galaxias_user_guide/data/sites.csv')
    galaxias.use_data(events=sites)
    sites2 = pd.read_csv('./data-publish/events.csv')
    assert sites.equals(sites2)

def test_use_data_write_occurrences_events():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    sites = pd.read_csv('../../docs/source/galaxias_user_guide/data/sites.csv')
    observations = pd.read_csv('../../docs/source/galaxias_user_guide/data/observations.csv')
    galaxias.use_data(events=sites,occurrences=observations)
    assert os.path.isfile('./data-publish/events.csv') and os.path.isfile('./data-publish/occurrences.csv')

def test_use_data_write_occurrences_events_rename():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    sites = pd.read_csv('../../docs/source/galaxias_user_guide/data/sites.csv')
    observations = pd.read_csv('../../docs/source/galaxias_user_guide/data/observations.csv')
    galaxias.use_data(events=sites,events_filename='test.csv',occurrences=observations,occurrences_filename='test2.csv')
    assert os.path.isfile('./data-publish/test.csv') and os.path.isfile('./data-publish/test2.csv')
    
def test_use_data_write_occurrences_events_check_same():
    if os.path.exists('./data-publish'):
        shutil.rmtree('./data-publish')
    sites = pd.read_csv('../../docs/source/galaxias_user_guide/data/sites.csv')
    observations = pd.read_csv('../../docs/source/galaxias_user_guide/data/observations.csv')
    galaxias.use_data(events=sites,occurrences=observations)
    sites2 = pd.read_csv('./data-publish/events.csv')
    observations2 = pd.read_csv('./data-publish/occurrences.csv')
    assert sites.equals(sites2) and observations.equals(observations2)