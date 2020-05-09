# stock_price_alert_system

A script that can send alerts when a stock prices crosses a given threshold.

# Configuration
In `config_example.yml`, you can see a skeleton configuration.

Configuration consists of 2 main parts:

* ApplicationConfig
    * LogLevel: The desired verbosity of your logs
    * SlackAlert: For each object in the SlackAlert List, the script will end an alert to the Endpoint using the BotToken
    * SNSAlert: For each item in the SNSAlert List, an SMS will be sent using AWS SNS.

* Symbols
    This is the bread and butter.  You configure symbols you want to watch, set the alarm tresholds, and set the Type of bitstamp or yahoo for the datasource.
    

## Alerts

### SNS Configuration

This client can call Amazon Web Services Simple Notification Service (AWS SNS) to deliver a text message.
This requires you to configure your `aws-cli` by executing `aws configure` and configuring the default profile with a set of keys generated by AWS IAM.

### Slack Configuration

To set up the slack integration, create a slack app: `https://api.slack.com/apps`

You want to implment "Permissions" on your app, specifically you want to add the Bot Token Scope, `chat:write`.  This is done under the `https://api.slack.com/apps/{your_app_id}/oauth?` page

After you have enabled the chat:write permission, you'll install your app from the left hand menu.

Once installed, grab your Bot User OAuth Access Token, and insert it to the `config.yml` as the `BotToken` parameter

Then, configure your `Endpoint`.
If your `Endpoint` is a USER, you must feed the Slack Member ID, see here: `https://help.workast.com/hc/en-us/articles/360027461274-How-to-find-a-Slack-user-ID`

If your `Endpoint` is a channel, get the channel ID from your browser as discussed here: `https://www.wikihow.com/Find-a-Channel-ID-on-Slack-on-PC-or-Mac`

# Requirements
## Functional in Python 3.6.9

Install w/ pip: `pip3 install -r requirements.txt`

# Execution

`python tracker_v2.py`

# Optional Parameters

`--config [FILENAME]` defines an alertnate configuration file.  Default is config.yml

`--sleep` amount of seconds to sleep between loops, if `--loop` is enabled.

`--loop` causes the program to stay in an infinite loop.  requires a `--sleep` parameter

## Example

`python tracker_v2.py --loop --sleep 3600` to sleep 30 minutes between checks.
