:orphan:

Obscuring Your Data
====================================

Sometimes when dealing with sensitive, threatened or endangered species, you don't want the 
data to get into the wrong hands.  Thus, obfuscating (or obscuring) your data is prudent.  
But how do you reflect this in your data?

Obfuscating Coordinates
----------------------------

Do this (or find out how SDS does it)

Reflecting obfuscations in your dataset
------------------------------------------

Reflecting on how you obfuscated your data is important.  Thankfully, the Darwin Core 
standard has two 

``dataGeneralizations``

This is how you obscured your data, i.e. ``Coordinates generalized from original GPS 
coordinates to the nearest half degree grid cell.``

``informationWithheld``

This contains a description about additional information that exists, but isn't shared 
in the record itself.  Examples from TDWG include ``location information not given for 
endangered species`` and ``collector identities withheld``.

