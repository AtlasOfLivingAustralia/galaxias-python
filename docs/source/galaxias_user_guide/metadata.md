<!--
This is a metadata template in .Rmd format, which has been formatted such that 
it can render either to the `output` specified in the yaml section (above) AND 
to Ecological Metadata language (EML) using the {delma} R package. Sections can 
be added, re-arranged or removed to suit the dataset being described. Some 
features to be aware of:

- Headings are converted to camelCase for use as EML tags
- Header level sets the degree of nestedness for those tags
- Code blocks whose `label` corresponds to a supplied EML tag are used to set 
  attributes for that tag using `list()`

You can delete this section if you want. See https://delma.ala.org.au for 
software information or https://eml.ecoinformatics.org for information on EML.
-->

# Dataset

## Title
Your Title

## Creator
<!-- The 'creator' element provides the full name of the person, organization, 
or position who created the resource. The list of creators for a resource 
represent the people and organizations who should be cited for the resource.-->

### Individual Name

#### Given Name
Firstname

#### Surname
Lastname

### Address

#### Delivery Point
215 Road Street

#### City
Canberra

#### Administrative area
ACT

#### Postal code
2601

#### Country
Australia

### Electronic Mail Address
firstname.lastname@email.com

### User ID
#### directory
This is optional; however, if you would like to include ORCIDs, this is great

## Pubdate
<!-- This will be filled in when you write the eml-->

## Language
EN

## Abstract
A brief overview of the resource. This should provide enough information to help 
potential users of the data to understand if it may be of interest. Example 
content may include what the study was designed to investigate, what taxa were 
observed, and over what time period.

## Keyword Set

### Keyword
Occurrence

### Keyword Thesaurus
https://ipt.gbif.org/manual/en/ipt/latest/dwca-guide#dwc-a-components


## Licensed

### License name
Creative Commons Attribution 4.0 International

### URL
https://creativecommons.org/licenses/by/4.0/

### Identifier
CC-BY 4.0 (Int) 4.0


## Introduction
This section can include any methods you like, but should, at minimum, give a 
simple description of how the data were collected. To link to a publication with 
more complete information, add a level-2 heading called `Reference Publication` 
and add the citation to your paper.

If applicable, you can also choose to add information on data processing that 
are specific to this version of your dataset. This may include information on 
whether data on threatened species have been removed, or spatial data have been 
generalised (i.e. set to a lower spatial precision than the source dataset).


## Contact
<!-- The contact field contains contact information for this dataset. This is 
the person or institution to contact with questions about the use, 
interpretation of a data set.-->

### Individual Name

#### Given Name
Firstname

#### Surname
Lastname

### Address

#### Delivery Point
215 Road Street

#### City
Canberra

#### Administrative area
ACT

#### Postal code
2601

#### Country
Australia

### Electronic Mail Address
firstname.lastname@email.com