%define oname gst-python
%define name gstreamer0.10-python

Name:		%name
Version: 0.10.8
Release: %mkrel 2
Summary:	Python bindings for GStreamer
Group:		Development/Python
License: 	LGPL
URL:            http://gstreamer.net/
Source: 	http://gstreamer.freedesktop.org/src/gst-python/%oname-%{version}.tar.bz2
Requires: 	python
Requires: 	pygtk2.0
BuildRequires:	libgstreamer-plugins-base-devel >= %version
BuildRequires:	pygtk2.0-devel
BuildRequires:	libpython-devel
#BuildRequires:	automake1.8
#gw for the docs
#BuildRequires:	xmlto
#BuildRequires:  libxml2-utils

%description
This module contains a binding that allows GStreamer applications
to be written in Python.

%package devel
Summary:	Python bindings for GStreamer - development files
Group:		Development/Python
Requires: %name = %version

%description devel
This module contains a binding that allows GStreamer applications
to be written in Python.

Install this to build programs depending on %name.


%prep
%setup -q -n %oname-%{version}

%build
%configure2_5x
export XML_CATALOG_FILES=/etc/xml/catalog
%make 

%install

rm -rf $RPM_BUILD_ROOT
%makeinstall_std

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc AUTHORS NEWS RELEASE README
%py_platsitedir/gst-0.10/
%py_platsitedir/pygst*

%files devel
%defattr(-,root,root,755)
%doc ChangeLog
%_datadir/gst-python/
%_libdir/pkgconfig/gst-python-0.10.pc
