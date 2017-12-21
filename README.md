#diablo3-api

You will need to add some details in the script for your account
apikey="<insert here>"
profileEndpoint="https://eu.api.battle.net/d3/profile/<insert here>"

You get the API key from https://dev.battle.net/

Use -h for options see below example usage and output:

./d3API.py -h
usage: d3API.py [-h] [-a] [-l] [-c CHARACTER]

optional arguments:
  -h, --help            show this help message and exit
  -a, --account         account stats
  -l, --listall         list characters
  -c CHARACTER, --character CHARACTER
                        character detail for <heroID>

./d3API.py -l
+----------+------------+--------------+-------+----------+----------+
|    id    | Character  |    Class     | Level | Hardcore | Seasonal |
+----------+------------+--------------+-------+----------+----------+
| 91672329 | Bernadette | demon-hunter |   70  |  False   |  False   |
| 91672326 |   Eldoon   |  barbarian   |   70  |  False   |  False   |
| 91672321 |  Bernard   | witch-doctor |   70  |  False   |  False   |
| 91672550 |  Eldaria   |    wizard    |   70  |  False   |  False   |
| 91672327 |  Berdina   |   crusader   |   70  |  False   |  False   |
| 97025154 |   Eldarn   | necromancer  |   70  |  False   |  False   |
| 91672324 | Bernardine |    wizard    |   70  |  False   |  False   |
| 91672323 |  Bernardo  |     monk     |   70  |  False   |  False   |
| 91672328 |   Bardan   |   crusader   |   22  |   True   |  False   |
+----------+------------+--------------+-------+----------+----------+

