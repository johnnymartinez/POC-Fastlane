fastlane documentation
================
# Installation

Make sure you have the latest version of the Xcode command line tools installed:

```
xcode-select --install
```

Install _fastlane_ using
```
[sudo] gem install fastlane -NV
```
or alternatively using `brew cask install fastlane`

# Available Actions
## iOS
### ios get_dev_certs
```
fastlane ios get_dev_certs
```
Automate management of development certificates - This will check if any of the available signing certificates is installed on your local machine.
        sigh can create, renew, download and repair provisioning profiles (with one command). 
        It supports App Store, Ad Hoc, Development and Enterprise profiles and supports nice features, like auto-adding all test devices.
### ios bootstrap_code_signing
```
fastlane ios bootstrap_code_signing
```
Re-obtain match code-signing credentials after switching to a Beginning or Ending project folder
### ios sync_device_info
```
fastlane ios sync_device_info
```
Update iOS UDID's on the Developer Portal
### ios sync_signing_assets
```
fastlane ios sync_signing_assets
```
Sync team Code-Signing assets
### ios build_appstore
```
fastlane ios build_appstore
```
Compiles app for App Store submission
### ios build_adhoc
```
fastlane ios build_adhoc
```
Compiles app for Ad Hoc submission. Distribute app to testers on registered devices only. Apps expire in a few days and will stop working.
### ios distribute_to_appstore
```
fastlane ios distribute_to_appstore
```
Calls on build_appstore, which then will increment build number and compiles app along with distributing to TestFlight. App expires after 90 days.
### ios release
```
fastlane ios release
```

### ios lint
```
fastlane ios lint
```

### ios new_app
```
fastlane ios new_app
```

### ios eric_test
```
fastlane ios eric_test
```


----

This README.md is auto-generated and will be re-generated every time [fastlane](https://fastlane.tools) is run.
More information about fastlane can be found on [fastlane.tools](https://fastlane.tools).
The documentation of fastlane can be found on [docs.fastlane.tools](https://docs.fastlane.tools).
