# Modem USB Huawei HTTP API client in Python

This is a python lib to interact with Modem USB Huawei HTTP API. I tested it with:

* E5180
* E8372

Please let me know if you tested it successfully with other modems as well.

## Currently Supported

* webserver
   * SesTokInfo: gets a session token to use
* user
   * login: creates a new session on the HTTP API
* sms
   * get_sms: get information from boxes: inbox, outbox
   * send_sms: sends an SMS through device's modem
   * delete_sms: deletes an sms from one of their boxes
   * sms_count: get the sms count on each box
* ussd
   * status: get status of ussd. This will tell you if there are ussd messages available to read
   * send: sends a ussd message
   * get: retrieves a ussd message

### Prerequisites

Only [`requests`](https://github.com/requests/requests) library (and its dependencies) is required.

This is `requirements.txt` content:

```
certifi==2018.1.18
chardet==3.0.4
idna==2.6
requests==2.0.0
```

### Installing

Todo: make it a `pip install` option for this package.

## Built With

* [requests](https://github.com/requests/requests) - Python HTTP Requests for Humans™

## Contributing

Send me a PM if you want to contribute. 

## Authors

* **Pablo Santa Cruz** - *Initial work* - [pablo](https://github.com/pablo)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

