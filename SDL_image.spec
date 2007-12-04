%define name SDL_image
%define version 1.2.6
%define release %mkrel 1
%define lib_name_orig libSDL_image
%define lib_major 1.2
%define lib_name %mklibname %name %lib_major

Summary: Simple DirectMedia Layer - image
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.bz2
License: LGPL
URL: http://www.libsdl.org/projects/SDL_image/index.html
Group: System/Libraries
BuildRequires: alsa-lib-devel
BuildRequires: X11-devel
BuildRequires: esound-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libSDL-devel >= 1.2.10
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a simple library to load images of various formats as SDL surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

This package contains the binary `sdlshow' to test the library.

%package -n %{lib_name}
Summary: Main library for %{name}
Group: System/Libraries
Obsoletes: %{name}
Provides: %{name}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name}-devel
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Requires: libSDL-devel
Provides: %{lib_name_orig}-devel = %{version}-%{release}
Provides: %{name}%{lib_major}-devel = %{version}-%{release}
Obsoletes: %{name}-devel
Provides: %{name}-devel

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n %{lib_name}-test
Summary: Test binary for %{name}
Group: System/Libraries

%description -n %{lib_name}-test
This package contains binary to test the associated library.

%prep
%setup -q

%build
%configure2_5x 	--enable-bmp \
		--enable-gif \
		--enable-jpg \
		--enable-pcx \
		--enable-png \
		--enable-ppm \
		--enable-tif \
		--enable-xpm
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 .libs/showimage $RPM_BUILD_ROOT%{_bindir}/sdlshow

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}-test
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/sdlshow

%files -n %{lib_name}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc README COPYING CHANGES
%{_libdir}/*a
%{_libdir}/lib*.so
%{_includedir}/SDL/*
