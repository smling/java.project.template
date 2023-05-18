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
    testImplementation(platform("org.junit:junit-bom:5.10.0-M1"))
    testImplementation("org.junit.jupiter:junit-jupiter")
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