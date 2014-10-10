%define realname Catalyst-Plugin-Authentication-Store-Htpasswd
%define abbrevname Catalyst-P-A-Store-Htpasswd
%define name	perl-%{abbrevname}
%define	modprefix Catalyst

%define version 0.02
%define release 12

Summary:	Authentication database in $c->config
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Authen::Htpasswd) >= 0.13
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.01
BuildRequires:	perl(Module::Build)
Provides:	perl-%realname
Obsoletes:	perl-%realname
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This plugin uses Authen::Htpasswd to let your application use
.htpasswd files for it's authentication storage.


%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}





%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.02-11mdv2011.0
+ Revision: 680726
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.02-10mdv2011.0
+ Revision: 430269
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-9mdv2009.0
+ Revision: 255548
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-7mdv2008.1
+ Revision: 136674
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-7mdv2008.0
+ Revision: 85929
- rebuild


* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 02:05:44 (54303)
- Rebuild, spec file cleanup

* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 02:01:38 (54295)
- import perl-Catalyst-P-A-Store-Htpasswd-0.02-5mdk

* Wed May 17 2006 Scott Karns <scottk@mandriva.org> 0.02-5mdk
- Updated BuildRequires

* Thu Apr 27 2006 Scott Karns <scottk@mandriva.org> 0.02-4mdk
- Added Provides/Obsoletes:	perl-Catalyst-Plugin-Authentication-Store-Htpasswd

* Thu Apr 27 2006 Scott Karns <scottk@mandriva.org> 0.02-3mdk
- Abbreviate rpm name to fit in the 64 char limit

* Wed Feb 08 2006 Scott Karns <scott@karnstech.com> 0.02-2mdk
- Built from CPAN

* Sat Jan 14 2006 Scott Karns <scott@karnstech.com> 0.02-1mdk
- Initial Mdv RPM

