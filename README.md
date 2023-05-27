# Java Project Template #

![](https://img.shields.io/badge/CookieCutter-blue?style=flat-square&logo=cookiecutter&logoColor=lightbrown)
![](https://img.shields.io/badge/Python-grey?style=flat-square&logo=python&logoColor=lightbrown)

This is the project template on [CookieCutter](https://github.com/cookiecutter/cookiecutter) for creating Java library project.

User can use the template to create Java Maven / Gradle project and supported Java LTS version.

When rendering project, it will lookup Maven to get latest package version to prevent patching after project created.

## Prerequesties ##
1. Install CookieCutter in workspace.
```sh
sudo apt install python
pip install cookiecutter
```

## Usage ##

### Parameters ###
|Parameter|Description|Default value|
|---|---|---|
|`javaVersion`|Java version (`8`, `11`, `17`, `19`)| `17`|
|`projectType`|Project type (`gradle` / `maven`)| `gradle`|
|`projectGroup`|Package group| `io.github`|
|`javaVersion`|Package name, word seperate with `-`| `demo-library`|
|`version`|Package version| `1.0.0-SNAPSHOT`|

### Example ###
1. Command to create web client library.
```sh
cookiecutter https://github.com/smling/java.project.template
```
