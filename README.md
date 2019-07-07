# Meross plug countdown

Just a small script to implement a countdown timer on a Meross smart plug.

As an example of usage, I use it to turn off the filter of my aquarium so I have time to feed the fishes. Then the filter is automatically pushed back on at the end of the count.

## Usage

Clone the repository. Edit variables in the docker compose file to add your Meross config.

Environment variable configuration:

| Name            | Comment                                        |
|:----------------|:-----------------------------------------------|
| MEROSS_DEVICE   | Name of the device on Meross App. E.g: my_plug |
| MEROSS_CHANNEL  | Channel number on the smart plug. E.g: 4       |
| MEROSS_EMAIL    | Email of the Meross account                    |
| MEROSS_PASSWORD | Password of the Meross account                 |


Example:
```yaml
environment:
  FLASK_DEBUG: "1"
  MEROSS_DEVICE: "Aquarium"
  MEROSS_CHANNEL: "3"
  MEROSS_EMAIL: "first_name.last_name@gmail.com"
  MEROSS_PASSWORD: 'my_secret_password'
```

Run docker compose
```
docker-compose up -d
```

## Call the API

Example of call
```
curl -i -H "Content-Type: application/json" -X POST -d '{"interval":"10s"}' http://127.0.0.1:5000/countdown
```

The `interval` is composed by an integer followed by a letter "s" or "m" or "h" or "d" for second, minute, hour or day.

Example of updateInterval:

- **1d**: stop the counter after 1 day
- **4h**: stop the counter after 4 hours
- **30m**: stop the counter after 30 minutes
- **10s**: stop the counter after 10 seconds

## Add to the startup (systemd based system)

Copy the service file. (Edit path in the script if needed)
```
cp countdown.service /etc/systemd/system/countdown.service
```

Enable and start
```
systemctl daemon-reload
systemctl enable countdown
systemctl start countdown
```
