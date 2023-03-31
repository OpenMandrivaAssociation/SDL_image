%define		major 0
%define		apiver 1.2
%define		libname %mklibname %{name} %{apiver} %{major}
%define		develname %mklibname %{name} -d
%define 	_disable_lto 1

Summary:	Simple DirectMedia Layer - image
Name:		SDL_image
Version:	1.2.12
Release:	17
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.libsdl.org/projects/SDL_image/index.html
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
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
%autosetup -p1

%build
# (anssi) --disable-x-shared disable dlopening, so that we link to them
# dynamically instead, and thus get correct autorequires
%configure 	--enable-bmp \
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

%make_build

%install
%make_install
install -d %{buildroot}%{_bindir}
install -m755 .libs/showimage %{buildroot}%{_bindir}/sdlshow

%files -n %{libname}-test
%{_bindir}/sdlshow

%files -n %{libname}
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%doc README CHANGES
%{_libdir}/lib*.so
%{_includedir}/SDL/*
%{_libdir}/pkgconfig/SDL_image.pc
