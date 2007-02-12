Summary:	Icelandic dictionary for aspell
Summary(pl.UTF-8):	Słownik islandzki dla aspella
Name:		aspell-is
Version:	0.51.1
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/is/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	1e0b6125d91d7edad710482ddcce2d23
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icelandic dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik islandzki (lista słów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
