# email-script

Script demands instance-info.json file in the following format:

```
{

    "InstanceIds": [ "InstanceId1", "InstanceIdN",  "" ],
    "Region": "eu-west-1",
    "Email": "someemail@domain.name"

}
```

This script will send a notification email every week starting after 24h of instance running, but that intervals may be changed by export NOTIFY_INTERVAL and INITIAL_DELAY parameters.

Also you should set SMTP_SERVER, SMTP_PORT, SMTP_LOGIN, SMTP_PASSWORD and SMTP_FROM parameters in env.
