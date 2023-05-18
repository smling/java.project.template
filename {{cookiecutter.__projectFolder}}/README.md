# {{cookiecutter.artifact.capitalize().replace(".", " ")}} #

{% if cookiecutter.projectType == "maven" %}
![](https://img.shields.io/badge/Project-Maven-green?style=flat-square&logo=apachemaven&logoColor=red)
{% endif %}
{% if cookiecutter.projectType == "gradle" %}
![](https://img.shields.io/badge/Project-Gradle-green?style=flat-square&logo=gradle&logoColor=blue)
{% endif %}
![](https://img.shields.io/badge/Language-Java_{{cookiecutter.javaVersion}}-green?style=flat-square&logo=java&logoColor=red)

## Description ##

This repository contains source code of {{cookiecutter.artifact}}.

The code within this pipeline triggers the job for `CI.Maven` which builds the java package and published to Nexus OSS.

## Change History ##

See [CHAGELOG.md](CHANGELOG.md) for more details.

## Installation ##

### Maven ###

Copy code below inside tag `<dependencies>` in `pom.xml`.

```xml
<dependency>
    <groupId>{{cookiecutter.group}}</groupId>
    <artifactId>{{cookiecutter.artifact}}</artifactId>
    <version>{{cookiecutter.version}}</version>
</dependency>
```

### Gradle ###

Copy code below in `build.gradle`.

```kotlin
dependencies {
    implementation("{{cookiecutter.group}}:{{cookiecutter.artifact}}:0.0.1")
}
```

## Usage ##

Sample code to call API as below:
```java
/**
 * Sample application.
 */
public class Application {
	
	static final Logger logger = LoggerFactory.getLogger(Application.class);

	public static void main(String[] args) {

    }
}
```

## Development ##

Suggest read this session before start develop in this repository.

### Project Structure ###

| Folder / File Name  | Description  |
|---|---|
| :open_file_folder: `docs/` | API document. |
| :open_file_folder: `src/` | This contains source code and test code. |
| :open_file_folder: `src/main` | This contains main source code. |
| :open_file_folder: `src/test` | This contains unit test code. |
{% if cookiecutter.projectType == "maven" %}
| :clipboard: `pom.xml` | Contains project information required by maven. |
{% endif %}
{% if cookiecutter.projectType == "gradle" %}
| :clipboard: `build.gradle.kts` | Contains project information required by gradle. |
{% endif %}
| :clipboard: `README.md` | This file. |
| :clipboard: `CHANGELOG.md` | High level information about version changed.
{% if cookiecutter.projectType == "gradle" %}
| :open_file_folder: `gradle` | Gradle wrapper class. |
| :computer: `gradlew` | Gradle wrapper for Linux. |
| :computer: `gradlew.bat` | Gradle wrapper for Windows. |
{% else %}
{% endif %}

### Employed Packages ###

#### Libraries ####

| Name |Version | Purpose |
|---|---|---|
| :envelope: `mockito-junit-jupiter` | `3.9.0` | Unit tests |
| :envelope: `mockito-inline` | `3.9.0` | Unit tests |
| :envelope: `mockito-core` | `3.9.0` | Unit tests |

