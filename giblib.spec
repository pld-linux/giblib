Summary:	Utility library used in many applications by LinuxBrit
Summary(pl.UTF-8):	Biblioteka narzędziowa używana w wielu aplikacjach LinuxBrit
Name:		giblib
Version:	1.2.4
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c810ef5389baf24882a1caca2954385e
URL:		http://www.linuxbrit.co.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
giblib is a utility library used by many of the applications LinuxBrit
writes. It incorporates doubly linked lists, some string functions,
and a wrapper for imlib2. The wrapper does two things. It gives you
access to fontstyles, which can be loaded from files, saved to files
or defined dynamically through the API. It also, and more importantly,
wraps imlib2's context API to simplify calls.

%description -l pl.UTF-8
giblib to biblioteka narzędziowa używana w wielu aplikacjach autorstwa
LinuxBrit. Zawiera dwukierunkowe listy, funkcje do obsługi ciągów
znaków i wrapper do Imlib2. Wrapper robi dwie rzeczy: dostęp do styli
fontów, które mogą być wczytywane z plików, zapisywane do plików lub
definiowane dynamicznie poprzez API, oraz upraszcza wywołania
niektórych funkcji Imlib2.

%package devel
Summary:	Header files for giblib
Summary(pl.UTF-8):	Pliki nagłówkowe giblib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for giblib.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki giblib.

%package static
Summary:	giblib static library
Summary(pl.UTF-8):	Statyczna biblioteka giblib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of giblib library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki giblib.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
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
