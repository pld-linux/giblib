Summary:	Utility library used in many applications by LinuxBrit
Summary(pl):	Biblioteka narzêdziowa u¿ywana w wielu aplikacjach LinuxBrit
Name:		giblib
Version:	1.2.2
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
URL:		http://www.linuxbrit.co.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	imlib2-devel
BuildRequires:	libltdl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
giblib is a utility library used by many of the applications LinuxBrit
writes. It incorporates doubly linked lists, some string functions,
and a wrapper for imlib2. The wrapper does two things. It gives you
access to fontstyles, which can be loaded from files, saved to files
or defined dynamically through the API. It also, and more importantly,
wraps imlib2's context API to simplify calls.
			      
%description -l pl
giblib to biblioteka narzêdziowa u¿ywana w wielu aplikacjach autorstwa
LinuxBrit. Zawiera dwukierunkowe listy, funkcje do obs³ugi ci±gów
znaków i wrapper do Imlib2. Wrapper robi dwie rzeczy: dostêp do styli
fontów, które mog± byæ wczytywane z plików, zapisywane do plików lub
definiowane dynamicznie poprzez API, oraz upraszcza wywo³ania
niektórych funkcji Imlib2.

%package devel
Summary:	Header files for giblib
Summary(pl):	Pliki nag³ówkowe giblib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for giblib.

%description devel -l pl
Pliki nag³ówkowe biblioteki giblib.

%package static
Summary:	giblib static library
Summary(pl):	Statyczna biblioteka giblib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of giblib library.

%description static -l pl
Statyczna wersja biblioteki giblib.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
