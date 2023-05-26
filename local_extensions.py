from jinja2.ext import Extension
import urllib.request
import xml.etree.ElementTree as ET

repository_url = "https://repo.maven.apache.org/maven2/"

class MavenPackageVersionLookupExtension(Extension):
    def __init__(self, environment):
        super(MavenPackageVersionLookupExtension, self).__init__(environment)

        def maven_package_version_lookup(group_id, artifact_id):
            package_name = group_id + "." + artifact_id
            metadata_url = repository_url + package_name.replace('.', '/') + "/maven-metadata.xml"
            # Send a GET request and retrieve the XML content
            with urllib.request.urlopen(metadata_url) as response:
                xml_content = response.read()

            # Parse the XML content using ElementTree
            root = ET.fromstring(xml_content)

            # Extract the latest version from the parsed XML
            version_tags = root.findall("./versioning/versions/version")
            latest_version = version_tags[-1].text  # The last version is considered the latest

            # Print the latest version
            print("Latest version of", package_name, "is", latest_version)
            return latest_version
        
        environment.globals.update(maven_package_version_lookup = maven_package_version_lookup)
            