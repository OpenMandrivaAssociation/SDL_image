%define		major 0
%define		apiver 1.2
%define		libname %mklibname %{name} %{apiver} %{major}
%define		develname %mklibname %{name} -d

Summary:	Simple DirectMedia Layer - image
Name:		SDL_image
Version:	1.2.12
Release:	12
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.libsdl.org/projects/SDL_image/index.html
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(sdl) >= 1.2.10

%description
This is a simple library to load images of various formats as SDL surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

This package contains the binary `sdlshow' to test the library.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}SDL_image1.2 < 1.2.6-2

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(sdl) >= 1.2.10
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}%{major}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}SDL_image1.2-devel < 1.2.6-2

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n %{libname}-test
Summary:	Test binary for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}SDL_image1.2-test < 1.2.6-2

%description -n %{libname}-test
This package contains binary to test the associated library.

%prep
%setup -q

%build
# (anssi) --disable-x-shared disable dlopening, so that we link to them
# dynamically instead, and thus get correct autorequires
%configure2_5x 	--enable-bmp \
		--enable-gif \
		--enable-jpg \
		--enable-pcx \
		--enable-png \
		--enable-tif \
		--enable-xpm \
		--disable-jpg-shared \
		--disable-png-shared \
		--disable-tif-shared \
		--disable-static

%make

%install
%makeinstall_std
%__install -d %{buildroot}%{_bindir}
%__install -m755 .libs/showimage %{buildroot}%{_bindir}/sdlshow

%files -n %{libname}-test
%{_bindir}/sdlshow

%files -n %{libname}
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%doc README CHANGES
%{_libdir}/lib*.so
%{_includedir}/SDL/*
%{_libdir}/pkgconfig/SDL_image.pc


%changelog
* Mon Mar 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.12-1mdv2012.0
+ Revision: 785489
- New version 1.2.12, don't build static lib, update file list

* Thu Dec 22 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-8
+ Revision: 744390
- rebuilt against libtiff.so.5

* Mon Dec 19 2011 Andrey Bondrov <abondrov@mandriva.org> 1.2.10-7
+ Revision: 743797
- Rebuild to remove .la files

* Thu Sep 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.10-6
+ Revision: 701824
- rebuild for new libpng15

  + Alexander Barakin <abarakin@mandriva.org>
    - imported package SDL_image

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-4
+ Revision: 671970
- mass rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.2.10-3
+ Revision: 634985
- rebuild
- tighten BR

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-2mdv2011.0
+ Revision: 488741
- rebuilt against libjpeg v8

  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 1.2.10

* Sat Nov 07 2009 Anssi Hannula <anssi@mandriva.org> 1.2.7-5mdv2010.1
+ Revision: 462310
- remove dependency hacks added by Funda Wang and just disable dlopening,
  using direct linking instead

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 1.2.7-4mdv2010.1
+ Revision: 461722
- rebuild for new libtiff

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 1.2.7-3mdv2010.1
+ Revision: 460568
- hard requires shared libs

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-2mdv2010.0
+ Revision: 413009
- rebuild

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1.2.7-1mdv2009.1
+ Revision: 308496
- New version 1.2.7
  security patches merged upstream

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-6mdv2009.0
+ Revision: 265683
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Feb 05 2008 Frederik Himpe <fhimpe@mandriva.org> 1.2.6-5mdv2008.1
+ Revision: 162830
- Add 2 patches from Fedora fixing CVE-2007-6697 and CVE-2008-0544

  + Funda Wang <fwang@mandriva.org>
    - Revert previous change ( it should be fixed on downstream packages)
    - libpackage should provide package name

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - obsolete old test subpackage

* Sun Jan 13 2008 Anssi Hannula <anssi@mandriva.org> 1.2.6-3mdv2008.1
+ Revision: 151076
- obsolete old library name
- provide %%name-devel
- versionize obsoletes
- do not provide old -devel name

* Sun Jan 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.6-2mdv2008.1
+ Revision: 150945
- new license policy
- new devel library policy
- drop not needed buildrequire on esound-devel (?)
- spec file clean
- correct libification

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Thu Jul 26 2007 Funda Wang <fwang@mandriva.org> 1.2.6-1mdv2008.0
+ Revision: 55750
- New version 1.2.6

* Wed Jun 06 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.2.5-4mdv2008.0
+ Revision: 36086
- Rebuild with libslang2.

* Sat May 26 2007 Funda Wang <fwang@mandriva.org> 1.2.5-3mdv2008.0
+ Revision: 31378
- Build against directfb 1.0


* Sat Feb 24 2007 Giuseppe GhibÃ² <ghibo@mandriva.com> 1.2.5-2mdv2007.0
+ Revision: 125366
- Rebuilt against latest libggi|libgii.
- Import SDL_image

* Sun Jun 25 2006 Götz Waschk <waschk@mandriva.org> 1.2.5-1mdv2007.0
- bump deps
- new version

* Thu Jun 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.4-4mdk
- Rebuild
- use mkrel

* Tue May 16 2006 Stefan van der Eijk <stefan@eijk.nu> 1.2.4-3mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.2.4-2mdk
- Rebuild

* Wed Mar 23 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.2.4-1mdk
- Release: 1.2.4.

* Wed Mar 23 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.2.3-4mdk
- Rebuilt.

