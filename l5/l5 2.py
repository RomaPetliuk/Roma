import requests
import random
page = random.randint(1, 7438)
pageSize = 1
url = f'https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}'
response = requests.get(url)
if response.ok:
    as_json = response.json()
    print({as_json['name']})
    print(f"Films: {as_json['films']}")
    print(f"Short films: {as_json['shortFilms']}")
    print(f"TV Shows: {as_json['tvShows']}")
    print(f"Video Games: {as_json['videoGames']}")
else:
    print('Щось пішло не так...')
    print(f'{response.status_code=}')
