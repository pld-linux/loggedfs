Summary:	Fuse-based filesystem which can log every operations
Summary(pl.UTF-8):	Bazowany na Fuse system plików logujący każdą operację
Name:		loggedfs
Version:	0.5
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/loggedfs/%{name}-%{version}.tar.bz2
# Source0-md5:	57e6cbe791c98ef287adaf9a36983067
URL:		http://loggedfs.sourceforge.net/
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
BuildRequires:	rlog-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LoggedFS is a fuse-based filesystem which can log every operations
that happens in it.

%description -l pl.UTF-8
LoggedFS to bazowany na fuse system plików logujący każda operację
jaka się na nim wydaży.

%prep
%setup -q -c

%build
%{__make} \
	CC="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}.xml
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
