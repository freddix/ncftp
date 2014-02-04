Summary:	Browser program for the File Transfer Protocol
Name:		ncftp
Version:	3.2.5
Release:	1
License:	The Clarified Artistic License
Group:		Applications/Networking
Source0:	ftp://ftp.ncftp.com/ncftp/%{name}-%{version}-src.tar.bz2
# Source0-md5:	b05c7a6d5269c04891f02f43d4312b30
URL:		http://www.ncftp.com/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NcFTP is a FTP client with many advantages over the standard one. It
includes command line editing, command histories, support for
recursive gets, automatic logins, background downloading and much
more. This version supports IPv6, too.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure2_13 \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_pixmapsdir},%{_mandir},%{_desktopdir},/var/spool/%{name}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/{CHANGELOG,FIREWALLS_AND_PROXIES,LICENSE,READLINE,what_*}.txt
%attr(755,root,root) %{_bindir}/ncftp
%attr(755,root,root) %{_bindir}/ncftpbatch
%attr(755,root,root) %{_bindir}/ncftpbookmarks
%attr(755,root,root) %{_bindir}/ncftpget
%attr(755,root,root) %{_bindir}/ncftpls
%attr(755,root,root) %{_bindir}/ncftpput
%attr(755,root,root) %{_bindir}/ncftpspooler
%{_mandir}/man1/ncftp*.1*

