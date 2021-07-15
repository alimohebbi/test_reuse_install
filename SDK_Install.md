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
export ANDROID_SDK_ROOT = Path to your SDK folder
export ANDROID_HOME = The same as ANDROID_SDK_ROOT
```

Add to path variable

```
PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$ANDROID_SDK_ROOT/platform-tools:$ANDROID_SDK_ROOT/emulator
```

install platfrom:The platform packages are required to compile your app for the specified API level

```
sdkmanager "platforms;android-25"
sdkmanager "platforms;android-23"
sdkmanager "platforms;android-21"
```

you can see all packages as follow `sdkmanager --list`


install an image for the emulator:


```
# sdkmanager --install [image name]
sdkmanager --install "system-images;android-24;default;x86_64"
```

Check the installation by `sdkmanager --list_installed`

Uninstall by `sdkmanager --uninstall [image name]`

Install build tools: They are necessary to build your Android apps

```
sdkmanager "build-tools;25.0.3"
```

Find a proper device. "id: 9 or "Nexus 6P"" is ok.

```
avdmanager list devices

```

Create an emulator
```
# avdmanager create avd --name [emulator name] --package "[image name] -d [device name or id]"
avdmanager create avd --name emulator1 --package "system-images;android-24;default;x86_64" -d 9
```

Run the emulator
```
emulator -ports 5554,5555 -avd emulator1 -no-window -no-audio -partition-size
```

If you want to delete an emulator:

```
avdmanager delete avd -n [name of emulator]
```

### Test the setup
Check adb:
```
run adb server 
adb start-server
```


For special cases you may need to run this once
```
sudo setfacl -m u:<user>:rwx /dev/kvm
```
