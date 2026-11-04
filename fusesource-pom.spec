Name:             fusesource-pom
Version:          1.12
Release:          1
Summary:          Parent POM for FuseSource Maven projects
Group:            Development/Java
License:          ASL 2.0
URL:              https://fusesource.com/
Source0:          http://repo1.maven.org/maven2/org/fusesource/fusesource-pom/%{version}/fusesource-pom-%{version}.pom
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch
BuildSystem:	maven


BuildRequires:	javapackages-tools
%description
This is a shared POM parent for FuseSource Maven projects

%prep
cp %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_remove_plugin :clirr-maven-plugin

# WebDAV wagon is not available in Fedora.
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"

%files -f .mfiles
%doc LICENSE
