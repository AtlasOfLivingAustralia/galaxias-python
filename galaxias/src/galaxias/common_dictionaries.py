REQUIRED_DWCA_TERMS = {
    "Australia": ["scientificName", "eventDate", "basisOfRecord"], #occurrenceID, catalogNumber, recordNumber
    "ALA": ["scientificName", "eventDate", "basisOfRecord"],
}

ID_REQUIRED_DWCA_TERMS = {
    "Australia": ["occurrenceID", "catalogNumber", "recordNumber"], 
    "ALA": ["occurrenceID", "catalogNumber", "recordNumber"],
}

GEO_REQUIRED_DWCA_TERMS = {
    "Australia": ["decimalLatitude", "decimalLongitude", "geodeticDatum","coordinateUncertaintyInMeters"], 
    "ALA": ["decimalLatitude", "decimalLongitude", "geodeticDatum","coordinateUncertaintyInMeters"],
}

NAME_MATCHING_TERMS = {
    "Australia": ["scientificName","scientificNameAuthorship","rank","species","genus","family","order","classs","phylum","kingdom"],
    "ALA": ["scientificName","scientificNameAuthorship","rank","species","genus","family","order","classs","phylum","kingdom"]
}