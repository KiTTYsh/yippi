#Yippi! 
Yippi is an e621 API wrapper for Python, to make everyone's life simplier.

#Requirements 
+ Python 3.x
+ urllib
+ json

#Installation 
Clone this repository, and type this down 
```bash
$ pip install -e .``` 

#Example 
```python
results = yippi.search(['girly', 'male', 'fox']) # Searches e621 with "girly male fox" as query
results.file_url # Get the image/file's URL``` 
This is only a basic example, I'll add further documentation later.