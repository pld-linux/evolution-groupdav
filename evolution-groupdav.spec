Summary:	evolution-groupdav - OpenGroupware Evolution connector
Summary(pl):	evolution-groupdav - wtyczka ³±cz±ca Evolution z OpenGroupware.org
Name:		evolution-groupdav
Version:	0.2
Release:	0.2
License:	GPL
Group:		X11/Applications		
Source0:	http://noodle.yacoi.com/devel/downloads/evolution-groupdav/%{name}-%{version}.tar.gz
# Source0-md5:
#Patch0:
URL:		http://noodle.yacoi.com/
BuildRequires:	evolution-data-server-devel >= 1.1
BuildRequires:	evolution-devel >= 2.1
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
Requires:	evolution >= 2.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGroupware Evolution connector.

%description -l pl
Wtyczka ³±cz±ca Evolution z systemem pracy grupowej OpenGroupware.org.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%files
