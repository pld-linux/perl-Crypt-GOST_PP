%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	GOST_PP
Summary:	Crypt::GOST_PP Perl module - the GOST Encryption Algorithm
Summary(pl):	Modu� Perla Crypt::GOST_PP - algorytm kodowania GOST
Name:		perl-Crypt-GOST_PP
Version:	1.10
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::GOST_PP is a pure perl implementation of GOST, a 64-bit
symmetrical block cipher with a 256-bit key from the former Soviet
Union.

%description -l pl
Modu� Crypt::GOST_PP jest czysto perlow� implementacj� GOST,
64-bitowego symetrycznego szyfru blokowego z 256-bitowym kluczem,
opracowanego w by�ym Zwi�zku Radzieckim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/GOST_PP.pm
%{_mandir}/man3/*
