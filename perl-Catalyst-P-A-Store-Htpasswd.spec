%define realname Catalyst-Plugin-Authentication-Store-Htpasswd
%define abbrevname Catalyst-P-A-Store-Htpasswd
%define name	perl-%{abbrevname}
%define	modprefix Catalyst

%define version 0.02
%define release %mkrel 7

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



