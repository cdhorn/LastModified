# Last Modified Gramplet

This is an outgrowth of the original Latest Changes Gramplet extended to cover all object types as well as provide a Global modified list.

It only supports DBAPI managed database backends and can not be used with the BSDDB database format as it queries the tables to get the handles for the most recent changes. This is radically faster than iterating through all the tables to fetch and check each object.

A left click on any tile will launch the editor for that object. A middle click will navigate to the list view for that object.  A right click will navigate to the card view for that object and if not found fall back to the list view.
