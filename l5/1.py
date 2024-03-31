import requests

response = requests.get('https://www.whenisthenextmcufilm.com/api')

if response.ok:
    as_json = response.json()
    print(as_json['title'])
    print(as_json['overview'])
    print(f"{as_json['title']} releases in {as_json['days_until']} days")
    print(f"Release date {as_json['release_date']}")
    print(f"Production type: {as_json['type']}")
else:
    print(f'{response.status_code=}')
