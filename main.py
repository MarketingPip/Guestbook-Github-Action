import os
import requests, json 



Google_Form_ID="12dHNazq1AW04WG8DHy0-qKsqejpT6urRY0EgGRfPxdc"  
Google_Form_Name="Form+Responses+1"

Sign_My_GuestBookMessage = """Want to sign my guestbook? Click here <a href="github.com">Sign Here</a>"""

## Results to fetch 
MAX_RESULTS = int(os.environ.get("INPUT_SECONDS"))




Template = """
<div align="center">
<h3> Recent Guestbook Entries</h3>
<table>
<thead>
<tr>
<th>ID.</th>
<th>Name</th>
<th>Guestbook Entry</th>
</tr>
</thead>
<tbody>
"""

JSON_Data_URL = f"""https://opensheet.elk.sh/{Google_Form_ID}/{Google_Form_Name}"""
resp = requests.get(url=JSON_Data_URL)
data = resp.json()
Guestbook_Entry_Count = 0 
for i in range(0, MAX_RESULTS):
	Guestbook_Entry_Count = Guestbook_Entry_Count + 1
	Name = data[i]['Name']
	Email = data[i]['Email']
	Guestbook_Entry = data[i]['Guestbook_Entry']
	Template += f"""
<tr>   
<td>{Guestbook_Entry_Count}.</td>
<td>{Name}</td>
<td>{Guestbook_Entry}</td>
</tr>
    """
    

## Close the template
Template += f"""
</tbody>
</table>
{Sign_My_GuestBookMessage}
</div>"""
	
	
# Define the filename here you want to replace content in
FileName = "README.md"

with open(FileName, 'r') as f:
    contents = f.read()
    # Define the first line where your content will be replaced / added 
    starting_text = '<!---START OF CONTENT --->'
    # Define the second line where your content will be replaced / added 
    ending_text = '<!---END OF CONTENT --->'
    to_replace = contents[contents.find(starting_text)+len(starting_text):contents.find(ending_text)]
    contents = contents.replace(to_replace, Template)
print(Template)   
with open(FileName, 'w') as f:
    f.write(contents)   
    
