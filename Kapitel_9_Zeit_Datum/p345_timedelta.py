import os
from datetime import datetime,timedelta
geaendert = int(os.path.getmtime("p322_date.py"))
aktuelle_unixtime = int(datetime.now().timestamp())
sekunden = aktuelle_unixtime - geaendert
print("sekunden,timedelta(sekunden)",sekunden,timedelta(seconds=sekunden))
