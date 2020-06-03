# tidyid
Sample IDs that are easy to read and write.

Tidy IDs are integer values encoded using a simplified 
alphabet. They're much shorter than basic numeric IDs,
and only use characters that are not easily confused 
when reading or writing. Additionally, zero is not part
of the alphabet, so it can be used to pad the IDs without 
adding confusion. 

Confusing IDs like: 00100001, 00100002, 00100003
Become Tidy IDs: 0C-MKY, 0C-MM1, 0C-MM2

# Generate IDs with Python

Use the tidyid.py Python script to generate IDs:

```shell
$ python tidyid.py 10 --start 1000000
63-YG2
63-YG3
63-YG4
63-YG5
63-YG6
63-YG7
63-YG8
63-YG9
63-YGA
63-YGC
```

See `tidyid.py -h` for more help with the command-line interface


Or, import tidyid and use in your scripts

```python
import tidyid

ids = list(tidyid.gen_ids(10, 1000000))

```


# Generate IDs via API

Tidyid is also deployed on AWS Lambda with an API Gateway, so 
you can generate IDs programmtically, or directly in your browser:

https://9xvwr2k2t6.execute-api.us-west-2.amazonaws.com/default/tidyid

The following options can be given as URL parameters:

- n - the number of IDs to generate
- pad - pad the IDs with leading zeros so that they are this many characters long
- split - split IDs into groups of this many characters
- start - integer value of the first ID to generate


Examples:

https://9xvwr2k2t6.execute-api.us-west-2.amazonaws.com/default/tidyid?n=20&start=100&pad=7

https://9xvwr2k2t6.execute-api.us-west-2.amazonaws.com/default/tidyid?n=5&start=42&pad=0

https://9xvwr2k2t6.execute-api.us-west-2.amazonaws.com/default/tidyid?n=20&start=100000



