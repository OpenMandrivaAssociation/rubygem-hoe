# Generated from hoe-2.9.1.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	hoe

Summary:	Hoe is a rake/rubygems helper for project Rakefiles
Name:		rubygem-%{rbname}

Version:	2.9.1
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://rubyforge.org/projects/seattlerb/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems >= 1.4
BuildArch:	noarch

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you
manage and maintain, and release your project and includes a dynamic
plug-in system allowing for easy extensibility. Hoe ships with
plug-ins for all your usual project tasks including rdoc generation,
testing, packaging, and deployment.
See class rdoc for help. Hint: `ri Hoe` or any of the plugins listed
below.
For extra goodness, see: http://seattlerb.rubyforge.org/hoe/Hoe.pdf

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(.*.pdf|template|test)'

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/sow
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README.txt
%{ruby_gemdir}/gems/%{rbname}-%{version}/.*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/sow
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/hoe
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/hoe/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.pdf
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/template
%{ruby_gemdir}/gems/%{rbname}-%{version}/template/*
%{ruby_gemdir}/gems/%{rbname}-%{version}/template/.*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
