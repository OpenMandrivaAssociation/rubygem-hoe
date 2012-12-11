# Generated from hoe-2.13.0.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	hoe

Summary:	Hoe is a rake/rubygems helper for project Rakefiles
Name:		rubygem-%{rbname}

Version:	2.13.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/seattlerb/hoe
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
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
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/sow
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/sow
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/hoe
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/hoe/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.13.1-1
+ Revision: 774438
- clean out some old junk
- new version

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.13.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Fri Jan 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.13.0-1
+ Revision: 769347
- version update 2.13.0

* Mon Sep 12 2011 Alexander Barakin <abarakin@mandriva.org> 2.9.4-1
+ Revision: 699540
- missing rdoc fix
- imported package rubygem-hoe

* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.9.1-1
+ Revision: 643499
- regenerate spec with gem2rpm5
- new release: 2.9.1

* Tue Dec 07 2010 Rémy Clouard <shikamaru@mandriva.org> 2.6.2-2mdv2011.0
+ Revision: 614533
- remove useless suggests and add corresponding provides

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.6.2-1mdv2011.0
+ Revision: 579407
- new release: 2.6.2
- don't install gem archive
- add minitest to suggests

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.5.0-1mdv2010.1
+ Revision: 500390
- import rubygem-hoe


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-1
- initial release
