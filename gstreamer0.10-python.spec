%define oname gst-python
%define name gstreamer0.10-python

Name:		%{name}
Version:	0.10.17
Release:	%mkrel 3
Summary:	Python bindings for GStreamer
Group:		Development/Python
License:	LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{oname}-%{version}.tar.bz2
Patch0:		gst-python-0.10.17-linkage.patch
#gw reall fix python dir (bug #54969)
Patch1: gst-python-0.10.17-fix-python-detection.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Requires: 	python
Requires: 	pygtk2.0
BuildRequires:	libgstreamer-plugins-base-devel >= 0.10.24.2
BuildRequires:	pygtk2.0-devel
%py_requires -d
#gw for the docs
#BuildRequires:	xmlto
#BuildRequires:  libxml2-utils

%description
This module contains a binding that allows GStreamer applications
to be written in Python.

%package devel
Summary:	Python bindings for GStreamer - development files
Group:		Development/Python
Requires:	%{name} = %{version}

%description devel
This module contains a binding that allows GStreamer applications
to be written in Python.

Install this to build programs depending on %{name}.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .linkage
%patch1 -p1 -b .fix-python-detection
aclocal -I common/m4
autoconf
automake

%build
%configure2_5x \
	--disable-valgrind

export XML_CATALOG_FILES=/etc/xml/catalog
%make 

%install

rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%check
export LC_ALL=C
make check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS RELEASE README
%{py_platsitedir}/gst-0.10/
%{py_platsitedir}/gstoption.so
%{py_platsitedir}/pygst*
%_libdir/gstreamer-0.10/libgstpython.so

%files devel
%defattr(-,root,root)
%doc ChangeLog
%{_datadir}/gst-python/
%{_libdir}/pkgconfig/gst-python-0.10.pc
