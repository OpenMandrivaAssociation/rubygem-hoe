%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname hoe
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary:	Hoe is a simple rake/rubygems helper for project Rakefiles
Name:		rubygem-%{gemname}
Version:	2.9.4
Release:	%mkrel 1
Group:		Development/Ruby 
License:	MIT
URL:		http://rubyforge.org/projects/seattlerb/
Source0:	http://rubygems.org/gems/%{gemname}-%{version}.gem
# Rescue Hoe.spec task when Manifest.txt
Patch0:		hoe-2.6.2-rescue-missing-Manifest.patch
# Fix test order due to glob order issue
Patch1:		rubygem-hoe-2.9.4-test-glob-order.patch
# Fix place to include Rake::DSL (for newer rake)
Patch2:		rubygem-hoe-2.9.4-rake-dsl-include.patch
Requires:	ruby(abi) = 1.8
Requires:	rubygems >= 1.3.6
Requires:	rubygem(rubyforge) >= 2.0.4
Requires:	rubygem(rake)	>= 0.8.7
#Requires:	rubygem(minitest) >= 1.7.0
BuildRequires:	rubygems >= 1.3.6
# % % check
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(rubyforge)
BuildArch:	noarch
Provides:	rubygem(%{gemname}) = %{version}

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps generate
rubygems and includes a dynamic plug-in system allowing for easy
extensibility. Hoe ships with plug-ins for all your usual project
tasks including rdoc generation, testing, packaging, and deployment.
Plug-ins Provided:
* Hoe::Clean
* Hoe::Debug
* Hoe::Deps
* Hoe::Flay
* Hoe::Flog
* Hoe::Inline
* Hoe::Package
* Hoe::Publish
* Hoe::RCov
* Hoe::Signing
* Hoe::Test
See class rdoc for help. Hint: ri Hoe

%package	doc
Summary:	Documentation for %{name}
Group:		Development/Ruby
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install \
	--local \
	-V \
	--install-dir .%{gemdir} \
	--force \
	--rdoc \
	%{SOURCE0}

pushd .%{geminstdir}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
	%{buildroot}%{gemdir}/

chmod 0644 %{buildroot}%{gemdir}/cache/*gem

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}/%{gemdir}/bin
find %{buildroot}/%{geminstdir}/bin -type f | xargs chmod 0755

chmod 0755 %{buildroot}/%{geminstdir}/template/bin/file_name.erb
# Don't remove template files
#rm -f % {buildroot}/ % {geminstdir}/template/.autotest.erb

%check
pushd .%{geminstdir}

# Make sure that hoe currently building are loaded
export RUBYLIB=$(pwd)/lib

rake test -v --trace
popd

%files
%defattr(-, root, root, -)
%{_bindir}/sow
%dir %{geminstdir}/
%{geminstdir}/bin/
%{geminstdir}/lib/
%{geminstdir}/template/
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%doc %{geminstdir}/[A-Z]*

%files	doc
%defattr(-,root,root,-)
%{geminstdir}/.autotest
%{geminstdir}/.gemtest
%{geminstdir}/test/
%{gemdir}/doc/%{gemname}-%{version}
