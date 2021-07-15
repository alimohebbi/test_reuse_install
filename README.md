# Directories
Please use two different directories:

1. home-> applications: All necessary application for running test reuse
2. home-> test-reuse: All scripts including ATM & CraftDroids

# Install SDK and Emulator

Follow instructions for [installation](http://star-rep.inf.usi.ch/Mohebbi/test_reuse_install/blob/master/SDK_Install.md).



# Semantic Matching Server
1. Clone [Semantic Matching Server](http://star-rep.inf.usi.ch/Mohebbi/matching-server)
1. Change the config file. All models are already available in the server.
1. Run the server on a screen session



# ATM
## Neo4j
1. Set java version to 11. Look at [JAVA Installation](http://star-rep.inf.usi.ch/Mohebbi/test_reuse_install/blob/master/java_Install.md)
1. Download noe4j community server
1. Follow `Neo4J server` instructions on the [link](http://star-rep.inf.usi.ch/star/Alexios-Stoupis/blob/master/AppTestMigrator/Neo4j.md). Ignore the request part.

## Install gradle
1. Choose a version. Version 5.6.1 works fine.
1. Run below commands

    ```
    wget https://services.gradle.org/distributions/gradle-5.6.1 -bin.zip -P /tmp
    sudo unzip -d /opt/gradle /tmp/gradle-*.zip
    ```
1. add to the environment

    ```
    export GRADLE_HOME=/opt/gradle/gradle-5.6.1
    export PATH=${GRADLE_HOME}/bin:${PATH}
    ```


## ATM main tool
1. Download the latest version of [ATM](https://drive.google.com/file/d/1T75IhV4AGRzFU7cjeE4xOpKwcGBXwzCC/view?usp=sharing)
1. Replace modified donar test cases
1. Rename the `linux_run.sh` to `run_AppTestMigrator.sh`

## Runner project
1. Clone [ATM runner](http://star-rep.inf.usi.ch/Mohebbi/atm_runner)
1. Modify confuguration file
1. Add migrations to `migration.csv`
1. Clean the result file
2. Set java version to 8. Look at [JAVA Installation](http://star-rep.inf.usi.ch/Mohebbi/test_reuse_install/blob/master/java_Install.md).
1. Run
1. Check result file
1. Go to 6 until get migrated test for all migrated files
1. Evaluate the migrated results

# Craftdriod

## Appium
1. Install the console version
1. Run in a screen sessoin

## Craftdroid main tool

1. Clone [crafdroid](http://star-rep.inf.usi.ch/Mohebbi/Craftdroid-Modified)
1. Replace modified donar test cases
1. Modify confuguration file
1. Add migrations to `manager/migration.csv`
1. Clean the result file
1. Run
1. Check result file
1. Go to 5 until get migrated test for all migrated files
1. Evaluate the migrated results