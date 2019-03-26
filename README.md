# Nyan Cat Pipeline Protector

Simple python code to watch some CI/CD build and call for the nyan cat to brace yourselfs

## Install
* pip install -r requirements.txt

## Configuration
### Bitbucket

#### Create App Password

1. Select Avatar > Bitbucket settings.
2. Click App passwords in the Access management section.
3. Click Create app password.
4. Give the app password a name related to the application that will use the password.
5. Select the specific access and permissions you want this application password to have. Likely you only need pipeline read access for this application.
6. Copy the generated password and either record or paste it into the application you want to give access. The password is only displayed this one time.

#### Generate Base64 String
Go to this page: https://www.base64encode.org/
Place `<username>:<app_passowrd>` and generate a Base64 String

#### Config.ini file
Just replace the config.ini values with your preferences
```
[BASE]
# Options: bitbucket
git_service=bitbucket

[BITBUCKET]
authorization_base64=<your_key>
repository_name=<repository_name>
repository_username=<repository_username>
```