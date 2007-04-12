%define oname gst-python
%define name gstreamer0.10-python
%define pygobject 2.11.2

Name:		%name
Version: 0.10.7
Release: %mkrel 1
Summary:	Python bindings for GStreamer
Group:		Development/Python
License: 	LGPL
URL:            http://gstreamer.net/
Source: 	http://gstreamer.freedesktop.org/src/gst-python/%oname-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Requires: 	python
Requires: 	python-gobject >= %pygobject
BuildRequires:	libgstreamer-plugins-base-devel >= %version
BuildRequires:	python-gobject >= %pygobject
BuildRequires:	libpython-devel
BuildRequires:	automake1.8
#gw for the docs
#BuildRequires:	xmlto
#BuildRequires:  libxml2-utils

%description
This module contains a binding that allows GStreamer applications
to be written in Python.

%prep
%setup -q -n %oname-%{version}
aclocal-1.8 -I common/m4
autoconf
automake-1.8

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
%doc AUTHORS ChangeLog NEWS RELEASE README
%py_platsitedir/gst-0.10/
%py_platsitedir/pygst*
%_datadir/gst-python/
%_libdir/pkgconfig/gst-python-0.10.pc


