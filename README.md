# Heroku Config Vars Formatter
When `ssh`'ing onto a running Heroku instance you have to manually set the
config vars as they aren't auto-populated. This tool helps you doing so:

1. Copy the variables from the UI
1. Run `format_heroku_config`
1. Paste the output into the ssh shell
