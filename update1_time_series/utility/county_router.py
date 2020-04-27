import json
import itertools
import csv
import re


with open("4-23-20.csv", "r") as counties:

    reader = csv.DictReader(counties)

    file = open("output.txt", "w")

    for row in reader:
        if row["Country_Region"] == "US":
            comb_key = row["Combined_Key"]
            comb_key = re.sub(', US','',comb_key)
            #file.write(comb_key)
            file.write("<Route path=\"/" + row["Province_State"] + ", " + row["Admin2"] +"\"render={(props) => <ColumnChartCounties info=\"" + comb_key + "\" isAuthed={true} />}/>")
            file.write("\n")
    file.close()


