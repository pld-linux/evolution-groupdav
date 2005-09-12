Summary:	evolution-groupdav - OpenGroupware.org Evolution connector
Summary(pl):	evolution-groupdav - wtyczka ³±cz±ca Evolution z OpenGroupware.org
Name:		evolution-groupdav
Version:	0.2
Release:	0.3
License:	GPL
Group:		X11/Applications
Source0:	http://noodle.yacoi.com/devel/downloads/evolution-groupdav/%{name}-%{version}.tar.gz
# Source0-md5:	c3f51aae3e851dde3ce42cfe37523692
Patch0:		%{name}-include_dir.patch
Patch1:		%{name}-pluginlib_2.4.patch
Patch2:		%{name}-confpluginlib_2.4.patch
URL:		http://noodle.yacoi.com/
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	evolution-devel >= 2.2
BuildRequires:	gconfmm-devel >= 2.6.0
BuildRequires:	glib2-devel >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	libglade-devel >= 2.4.0
BuildRequires:	libgnomecanvas-devel >= 2.6.0
BuildRequires:	libgnomeprintui-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libsoup-devel >= 2.2.0
BuildRequires:	perl-XML-Parser
Requires:	evolution >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGroupware.org Evolution connector.

%description -l pl
Wtyczka ³±cz±ca Evolution z systemem pracy grupowej OpenGroupware.org.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-1.2/camel-providers/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-1.2/extensions/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/2.2/plugins/*.la

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution-data-server-1.2/camel-providers/libcamelogo.so
%{_libdir}/evolution-data-server-1.2/camel-providers/libcamelogo.urls
%attr(755,root,root) %{_libdir}/evolution-data-server-1.2/extensions/libebookbackendogo.so
%attr(755,root,root) %{_libdir}/evolution-data-server-1.2/extensions/libecalbackendogo.so
%attr(755,root,root) %{_libdir}/evolution/2.2/plugins/liborg-opengroupware-config-eplugin.so
%{_libdir}/evolution/2.2/plugins/org-opengroupware-config-eplugin.eplug
