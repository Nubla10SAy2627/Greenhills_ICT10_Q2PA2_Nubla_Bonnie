# Set Operators

from pyscript import document

radiant = {'yoshiiki', 'micuhz', 'lea'}
bronze = {'rhythm', 'mychal', 'gabb'}
iron = {'penguinii', 'standeth', 'aqua'}
plastic = {'tanli', 'dej', 'aj'}

members = radiant | bronze | iron | plastic

def addmember(e):
    username = document.getElementById('username').value.lower().strip()
    gamertag = document.getElementById('gamertag').value.lower().strip()

    name = username + ' ' + gamertag

    new_member = {name}
    all_members = members | new_member

    member_list = all_members
    results = f"<p>{'<br>'.join(member_list)}</p>"
    results += f"<p>Total number of members: {len(all_members)}</p>"

    document.getElementById('results').innerHTML = results
