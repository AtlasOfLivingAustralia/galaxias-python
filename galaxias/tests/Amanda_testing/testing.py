import galaxias

my_dwca = galaxias.dwca(occurrences='occurrences_dwc_clean.csv')

my_dwca.make_eml_xml()
my_dwca.make_meta_xml()

my_dwca.create_dwca()