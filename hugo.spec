Summary:	PC Emulator
Summary(pl):	Emulator PC
Name:		hugo
Version:	2.10
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.zeograd.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	356e7353a8c3922e6ac9fc65d4c736ee
Patch0:		%{name}-gcc.patch
URL:		http://www.zeograd.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hu-Go! PC Emulator.

%description -l pl
Hu-Go! Emulator PC.

%prep
%setup -q
%patch0 -p1

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/*
