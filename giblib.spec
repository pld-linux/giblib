Summary:	Utility library used in many applications by LinuxBrit
Summary(pl.UTF-8):	Biblioteka narzędziowa używana w wielu aplikacjach LinuxBrit
Name:		giblib
Version:	1.2.4
Release:	5
License:	MIT
Group:		X11/Libraries
Source0:	http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c810ef5389baf24882a1caca2954385e
Patch0:		%{name}-pc.patch
Patch1:		%{name}-imlib2.patch
URL:		http://www.linuxbrit.co.uk/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	imlib2-devel >= 1.0.0
BuildRequires:	libtool
Requires:	imlib2 >= 1.0.0
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
LinuxBrit. Zawiera dwukierunkowe listy, funkcje do obsługi łańcuchów
znaków i wrapper dla Imlib2. Wrapper robi dwie rzeczy: dostęp do styli
fontów, które mogą być wczytywane z plików, zapisywane do plików lub
definiowane dynamicznie poprzez API, oraz upraszcza wywołania
niektórych funkcji Imlib2.

%package devel
Summary:	Header files for giblib
Summary(pl.UTF-8):	Pliki nagłówkowe giblib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imlib2-devel >= 1.0.0

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
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgiblib.la

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libgiblib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgiblib.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/giblib-config
%attr(755,root,root) %{_libdir}/libgiblib.so
%{_includedir}/giblib
%{_pkgconfigdir}/giblib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgiblib.a
