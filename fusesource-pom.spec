%{?_javapackages_macros:%_javapackages_macros}
Name:             fusesource-pom
Version:          1.9
Release:          9.3
Summary:          Parent POM for FuseSource Maven projects
Group:            Development/Java
License:          ASL 2.0
URL:              https://fusesource.com/
Source0:          http://repo1.maven.org/maven2/org/fusesource/fusesource-pom/%{version}/fusesource-pom-%{version}.pom
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local

%description
This is a shared POM parent for FuseSource Maven projects

%prep
cp %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_remove_plugin :clirr-maven-plugin

# WebDAV wagon is not available in Fedora.
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-4
- Remove wagon-webdav-jackrabbit from POM
- Resolves: rhbz#911552

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.9-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Sep 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.9-1
- Upstream release 1.9
- Removed Requires

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-5
- Install LICENSE file
- Convert patch to POM macro

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Tomas Radej <tradej@redhat.com> - 1.5-2
- Changed R on plexus-maven-plugin to component-metadata
- Guidelines fixes

* Fri May 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.5-1
- Initial packaging

