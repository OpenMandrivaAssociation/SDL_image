%define major 0
%define apiver 1.2
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %{name} -d

Summary:	Simple DirectMedia Layer - image
Name:		SDL_image
Version:	1.2.10
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.libsdl.org/projects/SDL_image/index.html
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz

BuildRequires:	libalsa-devel
BuildRequires:	X11-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libSDL-devel >= 1.2.10
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
Requires:	libSDL-devel
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
		--enable-ppm \
		--enable-tif \
		--enable-xpm \
		--disable-jpg-shared \
		--disable-png-shared \
		--disable-tif-shared

%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -d %{buildroot}%{_bindir}
install -m755 .libs/showimage %{buildroot}%{_bindir}/sdlshow

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}-test
%defattr(-,root,root)
%{_bindir}/sdlshow

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README CHANGES
%{_libdir}/*a
%{_libdir}/lib*.so
%{_includedir}/SDL/*
%{_libdir}/pkgconfig/SDL_image.pc
