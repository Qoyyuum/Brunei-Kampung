# List of Brunei Kampung, Mukims and Districts (Daerah)

[![Netlify Status](https://api.netlify.com/api/v1/badges/e618f8f4-09aa-41d1-b299-31bfbb7eb03f/deploy-status)](https://app.netlify.com/sites/brunei-kampung/deploys)

I've done this project several times before when building Brunei systems and I keep finding myself in the situation "**WHY ISN'T THERE A PROPER BRUNEI KAMPUNG JSON YET!?**". This is the embodiment of that situation.

## How to Use

There is no other methods than **GET**. You can find the full API documentation [here](https://documenter.getpostman.com/view/1580936/UVBzpAZ7)

The API endpoint uses URL chaining and allows partial matching in the following order: `https://tulusbn.herokuapp.com/api/DISTRICT/MUKIM/KAMPONG/POSTCODE`. Each parameter is optional but have to be in that order.
## Brief examples
### With cURL

```bash
curl --location --request GET 'https://tulusbn.herokuapp.com/api/Tutong'
```


### cURL Sample Response

```json
{
  "response": [
    {
      "Code": "TG2345",
      "District": "Tutong",
      "Kampong": "Peti Surat Persendirian (Pejabat Pos Lamunin)",
      "Mukim": "Daerah Tutong",
      "Number": 112
    },
    {
      "Code": "TC1145",
      "District": "Tutong",
      "Kampong": "Peti Surat Persendirian (Pejabat Pos Telisai)",
      "Mukim": "Daerah Tutong",
      "Number": 111
    },
    ...
}
```

### With Python3 Requests

```python
import requests

url = "https://tulusbn.herokuapp.com/api/Temb/Bang/Ujong"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

### Python3 Sample Response

```json
{
    "response": [
        {
            "Code": "PA3951",
            "District": "Temburong",
            "Kampong": "Kampong Ujong Jalan",
            "Mukim": "Mukim Bangar",
            "Number": 522
        }
    ]
}
```

## License

Feel free to fork and contribute. This little sideproject has no license so you can do whatever you want with it.

## Credits

Thanks to [Brunei Post Office](http://www.post.gov.bn) for the data.

Thanks to [Tim @TheWheat](https://gist.github.com/thewheat/560e3b60d0ea2be1c4dd8d95fa37d33d) for manually grabbing all of the postcodes.
