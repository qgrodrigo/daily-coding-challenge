# Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.

## Tests:
get_extension("document.txt") should return "txt".
get_extension("README") should return "none".
get_extension("image.PNG") should return "PNG".
get_extension(".gitignore") should return "gitignore".
get_extension("archive.tar.gz") should return "gz".
get_extension("final.draft.") should return "none".