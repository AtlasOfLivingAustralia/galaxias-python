'''For dwca_build.py'''

def add_taxonomic_information(self):
    """
    Adds full taxonomic information (from kingdom to species) to your data for clearer identification

    Parameters
    ----------
        ``None``

    Returns
    -------
        ``None``

    Examples
    --------

    .. prompt:: python

        import galaxias
        import pandas as pd
        data = pd.read_csv("occurrences_dwc_rename.csv")
        my_dwca = galaxias.dwca(occurrences=data)
        my_dwca.add_taxonomic_information()
        my_dwca.occurrences
        
    .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc_rename.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_taxonomic_information();print(my_dwca.occurrences)"
    """

    # check for scientificName, as users should check that they have the correct column names
    if "scientificName" not in list(self.occurrences.columns):
        raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")

    # get all info     
    species_checked = self.check_species_names(return_taxa=True)
    
    # merge the taxon information with the species information the user has provided
    if type(species_checked) is tuple:
        self.occurrences = pd.merge(self.occurrences, species_checked[1], left_on='scientificName', right_on='scientificName', how='left')
        self.occurrences = self.occurrences.rename(
            columns = {
                'rank': 'taxonRank',
                'classs': 'class'
            }
        )
    else:
        raise ValueError("Some species names are not correct - please generate a report to find out which ones.")

def check_species_names(self,
                        return_taxa = False,
                        num_matches = 5,
                        include_synonyms = True):
    """
    Checks species names against your specified backbone.  Can also give you higher taxon ranks for your taxon.

    Parameters
    ----------
        ``return_taxa`` : ``logical``
            Option whether to return a dictionary object containing full taxonomic information on your species.  Default to `False`. 

    Returns
    -------
        Either ``False`` if there are incorrect taxon names, or ``True``.  A dictionary object containing species names and alternatives 
        is returned with the ``return_taxa=True`` option.

    Examples
    --------
    .. prompt:: python

        import galaxias
        import pandas as pd
        data = pd.read_csv("occurrences_dwc_rename.csv")
        my_dwca = galaxias.dwca(occurrences=data)
        my_dwca.check_species_names()

    .. program-output:: python -c "import galaxias;import pandas as pd;data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc_rename.csv\\\");my_dwca = galaxias.dwca(occurrences=data);print(my_dwca.check_species_names())"
    """

    # get configurations from user
    # configs = readConfig()

    # get atlas
    # atlas = configs["galaxiasSettings"]["atlas"]
    atlas = "Australia"

    # check for scientificName, as users should check that they have the correct column names
    if "scientificName" not in list(self.occurrences.columns):
        raise ValueError("Before checking species names, ensure all your column names comply to DwCA standard.  scientificName is the correct title for species")
    
    # make a list of all scientific names in the dataframe
    scientific_names_list = list(set(self.occurrences["scientificName"]))
    
    # initialise has_invalid_taxa
    has_invalid_taxa=False
    
    # send list of scientific names to ALA to check their validity
    payload = [{"scientificName": name} for name in scientific_names_list]
    response = requests.request("POST","https://api.ala.org.au/namematching/api/searchAllByClassification",data=json.dumps(payload))
    response_json = response.json()
    terms = ["original name"] + ["proposed match(es)"] + ["rank of proposed match(es)"] + TAXON_TERMS["Australia"]
    invalid_taxon_dict = {x: [] for x in terms}
    
    # loop over list of names and ensure we have gotten all the issues - might need to do single name search
    # to ensure we get everything
    for item in scientific_names_list:
        item_index = next((index for (index, d) in enumerate(response_json) if "scientificName" in d and d["scientificName"] == item), None)
        if item_index is None:
            # make this better
            has_invalid_taxa = True
            response_single = requests.get("https://api.ala.org.au/namematching/api/autocomplete?q={}&max={}&includeSynonyms={}".format("%20".join(item.split(" ")),num_matches,str(include_synonyms).lower()))
            response_json_single = response_single.json()
            if response_json_single:
                if response_json_single[0]['rank'] is not None:
                    invalid_taxon_dict["original name"].append(item)
                    invalid_taxon_dict["proposed match(es)"].append(response_json_single[0]['name'])
                    invalid_taxon_dict["rank of proposed match(es)"].append(response_json_single[0]['rank'])
                    for term in TAXON_TERMS["Australia"]:
                        if term in response_json_single[0]['cl']:
                            invalid_taxon_dict[term].append(response_json_single[0]['cl'][term])
                        else:
                            invalid_taxon_dict[term].append(None)
                else:

                    # check for synonyms
                    for synonym in response_json_single[0]["synonymMatch"]:
                        if synonym['rank'] is not None:
                            invalid_taxon_dict["original name"].append(item)
                            invalid_taxon_dict["proposed match(es)"].append(synonym['name'])
                            invalid_taxon_dict["rank of proposed match(es)"].append(synonym['rank'])
                            for term in TAXON_TERMS["Australia"]:
                                if term in synonym['cl']:
                                    invalid_taxon_dict[term].append(synonym['cl'][term])
                            else:
                                invalid_taxon_dict[term].append(None)
                        else:
                            print("synonym doesn't match")
            else:

                # try one last time to find a match
                response_search = requests.get("https://api.ala.org.au/namematching/api/search?q={}".format("%20".join(item.split(" "))))
                response_search_json = response_search.json()            
                if response_search_json['success']:
                    invalid_taxon_dict["original name"].append(item)
                    invalid_taxon_dict["proposed match(es)"].append(response_search_json['scientificName'])
                    invalid_taxon_dict["rank of proposed match(es)"].append(response_search_json['rank'])
                    for term in TAXON_TERMS["Australia"]:
                        if term in response_search_json:
                            invalid_taxon_dict[term].append(response_search_json[term])
                        else:
                            invalid_taxon_dict[term].append(None)
                else:
                    print("last ditch search did not work")
                    print(response_search_json)
                    import sys
                    sys.exit()
        
    # check for homonyms - if there are any, then print them out to the user so the user can disambiguate the names
    if has_invalid_taxa:
        return False,pd.DataFrame(invalid_taxon_dict)
    elif return_taxa:
        payload = [{"scientificName": name} for name in scientific_names_list]
        response = requests.request("POST","https://api.ala.org.au/namematching/api/searchAllByClassification",data=json.dumps(payload))
        response_json = response.json()
        verification_list = {"scientificName": scientific_names_list, "issues": [None for i in range(len(scientific_names_list))]}
        taxonomy = pd.DataFrame({name: [None for i in range(len(scientific_names_list))] for name in TAXON_TERMS[atlas]})
        
        # loop over list of names and ensure we have gotten all the issues - might need to do single name search
        # to ensure we get everything
        for i,item in enumerate(scientific_names_list):
            item_index = next((index for (index, d) in enumerate(response_json) if "scientificName" in d and d["scientificName"] == item), None)
            taxonomy.loc[i,"scientificName"] = item
            if item_index is not None:
                verification_list["issues"][i] = response_json[item_index]["issues"]
                if return_taxa:
                    for term in TAXON_TERMS[atlas]:
                        if term in response_json[item_index]:
                            taxonomy.loc[i,term] = response_json[item_index][term]
        return True,taxonomy
    return True