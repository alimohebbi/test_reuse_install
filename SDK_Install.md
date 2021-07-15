
Download command line tools
place it at $ANDROID_SDK_ROOT/cmdline-tools/latest

give permission to download packages

```sudo chown $USER:$USER $ANDROID_HOME -R```


run at latest/bin

```
sdkmanager --licenses
./sdkmanager platform-tools emulator
```

Set environment variables in ~/.bashrc

```
ANDROID_SDK_ROOT = Path to your SDK folder
ANDROID_HOME = The same as ANDROID_SDK_ROOT
```

Add to path variable

```
ANDROID_SDK_ROOT=/opt/android-sdk
ANDROID_HOME=/opt/android-sdk
PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$ANDROID_SDK_ROOT/platform-tools:$ANDROID_SDK_ROOT/emulator
```

install platfrom:The platform packages are required to compile your app for the specified API level

```
sdkmanager "platforms;android-25"
sdkmanager "platforms;android-23"
sdkmanager "platforms;android-21"
```
install image for emulator:
you can see images by a command like `sdkmanager`

```
sdkmanager [image name]
```

install build tools: These are necessary to build your Android apps

```
sdkmanager "build-tools;25.0.3"
```

create an emulator
```
avdmanager create avd --name emulator1 --package "[image name]"
```
### Test the setup
run adb server 
adb start-server

run the emulator
```
emulator -ports 5554,5555 -avd emulator1 -no-window -no-audio 
```

For special cases you may need to run this once
```
sudo setfacl -m u:<user>:rwx /dev/kvm
```
