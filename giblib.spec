Summary:	-
Summary(pl):	-
Name:		giblib
Version:	1.2.2
Release:	1
License:	GPL
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

%description -l pl

%package devel
Summary:	-
Summary(pl):	-
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel

%description devel -l pl

%package static
Summary:	-
Summary(pl):	-
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static

%description static -l pl

%prep
%setup -q

%build
aclocal
autoconf
automake -a -c -f
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
