# DoorDash API Python Sample

This sample is an example of how to create a JWT using Python when calling the DoorDash API. Additionally, it creates a delivery request using the JWT.

It builds a token that is valid for 30 minutes. Please obtain a set of DoorDash Credentials (Developer ID, Key ID, and Signing Secret) in the [DoorDash Developer Portal](https://developer.doordash.com/portal/integration/drive/credentials) to use in the application.

This application targets Python version [3.11.2](https://www.python.org/downloads/). The code source and build files provided in this repository are samples and not intended for production, and are not supported.

## Running Sample

Follow these steps to run the sample app:

1. Clone repository locally.
2. Open a terminal and navigate to the source folder.
3. Install the pyjwt pip package by running the ``pip3 install pyjwt`` command.
4. Install the requests pip package by running the ``pip3 install requests`` command.
5. Install the uuid pip package by running the ``pip3 install uuid`` command.
6. Open app.py in a text editor and resolve all TODO items listed in comments, save changes.
7. Run ``python3 app.py`` in the terminal from source folder.

## More About DoorDash Credentials

- [DoorDash JWT Format](https://developer.doordash.com/en-US/docs/drive/reference/JWTs/)
- [Manage DoorDash Credentials](https://developer.doordash.com/en-US/docs/drive/how_to/manage_credentials/)
- [Create DoorDash JSON Web Tokens (JWTs)](https://developer.doordash.com/en-US/docs/drive/how_to/JWTs)

## Related Utilities and Samples

- [auth0 JWT Debugger](https://jwt.io/)
- [DoorDash API JWT JSFiddle Sample](https://bit.ly/doordashapi)
- [make-doordash-jwt CLI](https://github.com/infin8x/make-doordash-jwt)
- [DoorDash API get started with Postman](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started_postman/)
- [DoorDash SDK Example Application](https://github.com/doordash-oss/doordash_sdk_example_application)

## Community

Please join the [DoorDash Developer Discord community](https://discord.com/channels/951208871828013066/951208872478113875) to provide feedback and ask questions about developing with the DoorDash API.
