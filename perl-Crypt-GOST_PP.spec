%define		pdir	Crypt
%define		pnam	GOST_PP
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::GOST_PP Perl module - the GOST Encryption Algorithm
Summary(pl.UTF-8):	Moduł Perla Crypt::GOST_PP - algorytm kodowania GOST
Name:		perl-Crypt-GOST_PP
Version:	1.10
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d654c309c3ca199b7aa69151364bea6
URL:		http://search.cpan.org/dist/Crypt-GOST_PP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::GOST_PP is a pure perl implementation of GOST, a 64-bit
symmetrical block cipher with a 256-bit key from the former Soviet
Union.

%description -l pl.UTF-8
Moduł Crypt::GOST_PP jest czysto perlową implementacją GOST,
64-bitowego symetrycznego szyfru blokowego z 256-bitowym kluczem,
opracowanego w byłym Związku Radzieckim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Crypt/GOST_PP.pm
%{_mandir}/man3/*
