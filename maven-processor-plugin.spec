%_javapackages_macros
Name:          maven-processor-plugin
Version:       2.1.1
Release:       4.0%{?dist}
Summary:       Maven Processor Plugin
# some classes and pom file are annotated with ASL 2.0
# and the site here it is hosted says "GNU Lesser GPL"
# contacted the project owner (available in POM) and clarified the license status in LGPLv3
License:       LGPLv3 and ASL 2.0
Url:           http://code.google.com/p/maven-annotation-plugin/
# git clone https://code.google.com/p/maven-annotation-plugin/ maven-processor-plugin-2.1.1
# (cd maven-processor-plugin-2.1.1/ && git archive --format=tar --prefix=maven-processor-plugin-2.1.1/ maven-processor-plugin-2.1.1 | xz > ../maven-processor-plugin-2.1.1-src-git.tar.xz)
Source0:       %{name}-%{version}-src-git.tar.xz

BuildRequires: java-devel

# main deps
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

# test deps
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch

%description
A maven plugin to process annotation for jdk6 at compile time

This plugin helps to use from maven the new annotation processing
provided by JDK6 integrated in java compiler

This plugin could be considered the 'alter ego' of maven apt plugin.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_xpath_remove pom:project/pom:profiles
%pom_xpath_remove pom:build/pom:extensions

cp -p src/main/resources/COPYING.LESSER .

%build

%mvn_file :%{name} %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc COPYING.LESSER

%files javadoc -f .mfiles-javadoc
%doc COPYING.LESSER
