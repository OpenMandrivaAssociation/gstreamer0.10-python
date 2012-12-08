%define oname gst-python
%define name gstreamer0.10-python

Name:		%{name}
Version:	0.10.22
Release:	%mkrel 1
Summary:	Python bindings for GStreamer
Group:		Development/Python
License:	LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{oname}-%{version}.tar.bz2
Patch0:		gst-python-0.10.17-linkage.patch
#gw reall fix python dir (bug #54969)
Patch1: gst-python-0.10.20-fix-python-detection.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Requires: 	python
Requires: 	pygtk2.0
BuildRequires:	libgstreamer-plugins-base-devel >= 0.10.32
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
autoreconf -fi

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
#gw currently fails:
#https://bugzilla.gnome.org/show_bug.cgi?id=624490
#make check

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
%_includedir/gstreamer-0.10/gst/pygst*


%changelog
* Sat Oct 29 2011 Götz Waschk <waschk@mandriva.org> 0.10.22-1mdv2012.0
+ Revision: 707825
- new version
- update file list

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.21-2
+ Revision: 664940
- mass rebuild

* Sat Jan 22 2011 Götz Waschk <waschk@mandriva.org> 0.10.21-1
+ Revision: 632319
- new version
- bump gstreamer dep

* Thu Dec 02 2010 Götz Waschk <waschk@mandriva.org> 0.10.20-1mdv2011.0
+ Revision: 604706
- new version
- update patch 1

* Sun Oct 31 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-2mdv2011.0
+ Revision: 590907
- rebuild

* Thu Jul 15 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-1mdv2011.0
+ Revision: 553812
- disable checks
- new version
- fix build

* Thu Feb 11 2010 Götz Waschk <waschk@mandriva.org> 0.10.18-1mdv2010.1
+ Revision: 504267
- new version

* Thu Oct 29 2009 Götz Waschk <waschk@mandriva.org> 0.10.17-3mdv2010.0
+ Revision: 459892
- really fix bug #54969 (loading of libpython)

* Wed Oct 28 2009 Götz Waschk <waschk@mandriva.org> 0.10.17-2mdv2010.0
+ Revision: 459759
- readd and rediff linking patch (bug #54969)

* Tue Oct 06 2009 Götz Waschk <waschk@mandriva.org> 0.10.17-1mdv2010.0
+ Revision: 454491
- new version
- bump gstreamer dep

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 0.10.16-1mdv2010.0
+ Revision: 409961
- new version
- update gstreamer dep
- enable checks

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.10.15-1mdv2010.0
+ Revision: 374150
- new version
- bump deps
- disable linkage patch
- update file list

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 0.10.14-2mdv2009.1
+ Revision: 333674
- partial fix linkage

* Tue Jan 20 2009 Götz Waschk <waschk@mandriva.org> 0.10.14-1mdv2009.1
+ Revision: 331779
- new version
- drop patch
- bump deps

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.10.13-3mdv2009.1
+ Revision: 318836
- rebuild for new python

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.10.13-2mdv2009.1
+ Revision: 318769
- add literal.patch: fix a string literal error
- rebuild for python 2.6

* Tue Oct 14 2008 Götz Waschk <waschk@mandriva.org> 0.10.13-1mdv2009.1
+ Revision: 293577
- new version
- update file list

* Wed Jun 18 2008 Götz Waschk <waschk@mandriva.org> 0.10.12-1mdv2009.0
+ Revision: 225667
- new version

* Fri May 30 2008 Funda Wang <fwang@mandriva.org> 0.10.11-1mdv2009.0
+ Revision: 213523
- New version 0.10.11

* Sun Feb 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.10-1mdv2008.1
+ Revision: 161771
- new version
- spec file clean

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 02 2007 Götz Waschk <waschk@mandriva.org> 0.10.8-2mdv2008.0
+ Revision: 58100
- split out devel package to reduce the deps

* Thu Aug 02 2007 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2008.0
+ Revision: 58050
- fix deps
- new version


* Thu Feb 01 2007 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdv2007.0
+ Revision: 115817
- new version
- fix buildrequires

* Wed Dec 06 2006 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2007.1
+ Revision: 91721
- new version
- depend on python-gobject only

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.10.5-2mdv2007.1
+ Revision: 88357
- Import gstreamer0.10-python

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.10.5-2mdv2007.1
- Rebuild

* Sat Jul 22 2006 G�tz Waschk <waschk@mandriva.org> 0.10.5-1mdv2007.0
- fix build
- New release 0.10.5

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2007.0
- Rebuild

* Sat Apr 29 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdk
- New release 0.10.4

* Thu Mar 23 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdk
- New release 0.10.3

* Tue Jan 24 2006 G�tz Waschk <waschk@mandriva.org> 0.10.2-2mdk
- fix build

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdk
- New release 0.10.2

* Tue Dec 27 2005 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- New release 0.10.1

* Wed Dec 07 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.10.0-2mdk
- typo fixes
- use mkrel

* Tue Dec 06 2005 G�tz Waschk <waschk@mandriva.org> 0.10.0-1mdk
- fix package naming
- New release 0.10.0
- update file list
- drop patch

* Thu Jun 23 2005 G�tz Waschk <waschk@mandriva.org> 0.8.2-1mdk
- cleanup for rpmlint
- build fix
- New release 0.8.2

* Tue May 10 2005 G�tz Waschk <waschk@mandriva.org> 0.8.1-3mdk
- fix summary

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.8.1-2mdk
- Rebuild for new python

* Mon Nov 29 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1-1mdk
- New release 0.8.1

* Mon Nov 15 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.0-1mdk
- New release 0.8.0

* Mon Nov 15 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.7.94-1mdk
- New release 0.7.94

* Tue Nov 09 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.7.93-1mdk
- requires new pygtk
- New release 0.7.93

* Thu Jun 24 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.7.92-1mdk
- reenable libtoolize
- fix source URL
- New release 0.7.92

* Thu Apr 08 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.7.91-1mdk
- fix file list
- don't run libtoolize
- new version

