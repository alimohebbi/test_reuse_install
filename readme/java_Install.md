## Java installation

1. Download the desired file
2. If it is tar file
    
    ```
    tar xvf jdk_version.tar -C /usr/lib/jvm
    ```
3. Set the config of java
    
    ```
    update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk_version/bin/java" 1
    ```

3. Set the config of javac
    
    ```
    update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk_version/bin/javac" 1
    ```

4. Update config of java
    
    ```
        update-alternatives --config java
    ```

4. Update config of javac
    
    ```
        update-alternatives --config javac
    ```
