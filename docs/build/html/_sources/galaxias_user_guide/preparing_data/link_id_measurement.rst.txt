:orphan:

Linking measurements to ``eventID`` and ``occurrenceID``
=============================================================

For each measurement in an EventCore Archive, it needs to at least have an associated ``eventID``.  This is 
because there are some measurements that may be associated with the site or event you are at, such as ambient 
temperature, whether or not it was raining, etc. 

For those measurements describing specimens or live species, both an ``eventID`` and ``occurrenceID`` are 
needed for the measurement, so those accessing the data know which occurrence the measurement describes.