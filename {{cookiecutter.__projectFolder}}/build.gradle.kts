plugins {
    id("java")
    id("org.owasp.dependencycheck") version "8.2.1"
}

group = "{{cookiecutter.group}}.{{cookiecutter.artifact}}"
version = "{{cookiecutter.version}}"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:{{maven_package_version_lookup("org.junit","junit-bom")}}"))
    testImplementation("org.mockito:mockito-junit-jupiter:{{maven_package_version_lookup("org.mockito", "mockito-junit-jupiter")}}'")
    testImplementation("org.mockito:mockito-junit-jupiter:{{maven_package_version_lookup("org.mockito", "mockito-inline")}}'")
}

tasks.test {
    useJUnitPlatform()
}

tasks.withType<Javadoc> {
    val javaSrcDir = project.file("src/main/java")
    source = project.files(javaSrcDir).asFileTree
    classpath += project.files(sourceSets["main"].output)
    destinationDir = project.file("docs/javadoc")
}