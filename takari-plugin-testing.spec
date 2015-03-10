Name:           takari-plugin-testing
Version:        2.1.0
Release:        1%{?dist}
Summary:        Maven plugin testing library
License:        EPL
URL:            http://takari.io/
BuildArch:      noarch

Source0:        https://github.com/takari/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(io.takari.m2e.workspace:org.eclipse.m2e.workspace.cli)
BuildRequires:  mvn(io.takari:takari:pom:)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice::no_aop:)


%description
Small, cohesive, one-stop library for developing unit and integration tests for
Maven plugins. Provides alternative to, and arguably supersedes,
maven-plugin-testing-harness and maven-verifier.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n %{name}-project-%{name}-%{version}

# disable its for now
%pom_disable_module takari-plugin-testing-its

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc readme.md

%files javadoc -f .mfiles-javadoc


%changelog
* Tue Mar 10 2015 Michael Simacek <msimacek@redhat.com> - 2.1.0-1
- Initial packaging
