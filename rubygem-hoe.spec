%define	oname	hoe

Summary:	A rake/rubygems helper for project Rakefiles
Name:		rubygem-%{oname}
Version:	2.6.2
Release:	%mkrel 2
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby-rake >= 0.8.7 rubygem-gemcutter >= 0.2.1
Requires:	rubygem-rubyforge >= 2.0.3
Provides:	rubygem(%{oname}) = %{version}
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

%prep

%build

%install
rm -rf %{buildroot}
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

chmod u+w -R %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/sow
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
