import os;

def init_git():
    commands = [
        'git init',
        'git add .',
        'git commit -m "Initial commit"'
    ]
    try:
        for command in commands:
            os.system(command)
    except:
        print("Error occurred when init git")
        exit(1)

def init_directories():
    print("Initialize main program.")
    mainRootDirectory = "src/main/java/"+"{{cookiecutter.__projectPackageRoot}}".lower().replace(".", "/")
    os.makedirs(mainRootDirectory)
    os.rename("src/main/package-info.java", mainRootDirectory+"/package-info.java")
    os.rename("src/main/Main.java", mainRootDirectory+"/Main.java")

    print("Initialize test program.")
    testRootDirectory = "src/test/java/"+"{{cookiecutter.__projectPackageRoot}}".lower().replace(".", "/")
    os.makedirs(testRootDirectory)
    os.rename("src/test/package-info.java", testRootDirectory+"/package-info.java")
    os.rename("src/test/MainTest.java", testRootDirectory+"/MainTest.java")

    print("Clean up project.")
    match "{{cookiecutter.projectType}}":
        case "gradle":
            cleanup_maven()
        case "maven":
            cleanup_gradle()
        
def cleanup_maven():
    os.remove("pom.xml")
    os.remove(".github/workflows/CI-Maven.yaml")

def cleanup_gradle():
    os.rmdir("gradle")
    os.remove("build.gradle.kts")
    os.remove("gradlew")  
    os.remove("gradlew.bat")  
    os.remove("settings.gradle.kts")
    os.remove(".github/workflows/CI-Gradle.yaml")

def main():
    init_directories()
    init_git()

if __name__ == "__main__":
    main()