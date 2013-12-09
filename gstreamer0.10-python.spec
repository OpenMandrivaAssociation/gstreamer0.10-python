%define oname	gst-python
%define api	0.10
%define bname	gstreamer%{api}

Name:		%{bname}-python
Version:	0.10.22
Release:	5
Summary:	Python bindings for GStreamer
Group:		Development/Python
License:	LGPLv2+
Url:            http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{oname}-%{version}.tar.bz2
Patch0:		gst-python-0.10.17-linkage.patch
#gw reall fix python dir (bug #54969)
Patch1: gst-python-0.10.20-fix-python-detection.patch
Patch2:		gst-python-automake-1.13.patch

BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api})
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	python-devel
Requires: 	python
Requires: 	pygtk2.0

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
%setup -qn %{oname}-%{version}
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-valgrind

export XML_CATALOG_FILES=/etc/xml/catalog
%make 

%install
%makeinstall_std

%check
export LC_ALL=C
#gw currently fails:
#https://bugzilla.gnome.org/show_bug.cgi?id=624490
#make check

%files
%doc AUTHORS NEWS RELEASE README
%{py_platsitedir}/gst-%{api}/
%{py_platsitedir}/gstoption.so
%{py_platsitedir}/pygst*
%{_libdir}/gstreamer-%{api}/libgstpython.so

%files devel
%doc ChangeLog
%{_datadir}/gst-python/
%{_libdir}/pkgconfig/gst-python-%{api}.pc
%{_includedir}/gstreamer-%{api}/gst/pygst*

