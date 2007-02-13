Summary:	PC Emulator
Summary(pl.UTF-8):	Emulator PC
Name:		hugo
Version:	2.12
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.zeograd.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	1256ab47592413d12789166da23c00fc
URL:		http://www.zeograd.com/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hu-Go! PC Emulator.

%description -l pl.UTF-8
Hu-Go! Emulator PC.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO doc
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/*
