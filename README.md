# List of Brunei Kampung, Mukims and Districts (Daerah)

[![Netlify Status](https://api.netlify.com/api/v1/badges/e618f8f4-09aa-41d1-b299-31bfbb7eb03f/deploy-status)](https://app.netlify.com/sites/brunei-kampung/deploys)

I've done this project several times before when building Brunei systems and I keep finding myself in the situation "**WHY ISN'T THERE A PROPER BRUNEI KAMPUNG JSON YET!?**". This is the embodiment of that situation.

## How to Use

There is no other methods than **GET**

### With cURL

`curl https://brunei-kampung.netlify.com/brunei-kampung.json`

### With Python3 Requests

```python
import requests

url = "https://brunei-kampung.netlify.com/brunei-kampung.json"
response = requests.get(url)
```

## License

Feel free to fork and contribute. This little sideproject has no license so you can do whatever you want with it.

## Credits

Thanks to [Brunei Post Office](www.post.gov.bn) for the data.

Thanks to [Tim @TheWheat](https://gist.github.com/thewheat/560e3b60d0ea2be1c4dd8d95fa37d33d) for manually grabbing all of the postcodes.
