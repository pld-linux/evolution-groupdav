
Summary:	evolution-groupdav - OpenGroupware Evolution Connector
Summary(pl):	evolution-groupdav - Wtyczka ³±cz±ca z OpenGroupware
Name:		evolution-groupdav
Version:	0.1
Release:	0.1
License:	GPL
#Group:		
Source0:	http://noodle.yacoi.com/devel/downloads/evolution-groupdav/%{name}-%{version}.tar.gz
# Source0-md5:
#Patch0:
URL:		http://noodle.yacoi.com/
BuildRequires:	perl-XML-Parser
BuildRequires:	glib2-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	libgnomecanvas-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libglade-devel >= 2.4.0
BuildRequires:  libgnomeprintui-devel >= 2.6.0
BuildRequires:  gnome-vfs2-devel >= 2.6.0
BuildRequires:  gconfmm-devel >= 2.6.0
BuildRequires:  libsoup-devel >= 2.2.0
#BuildRequires:  libecal >= 1.1
#BuildRequires:  libedata-cal >= 1.1
BuildRequires:  evolution-data-server-devel >= 1.1
#BuildRequires:  libebook >= 1.1
#BuildRequires:  camel-provider >= 1.1
BuildRequires:  evolution-devel >=2.1
Requires:	evolution >= 2.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGroupware Evolution Connector

%description -l pl
Wtyczka ³±cz±ca Evolution z systemem pracy grupowej
OpenGroupware.org

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%files

$Log: evolution-groupdav.spec,v $
Revision 1.1  2005-01-16 23:45:44  wolvverine
- NFY
- new PLD spec
