Name:		xdriinfo
Version:	1.0.6
Release:	1
Summary:	Query configuration information of DRI drivers
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(gl)

%description
Driinfo can be used to query configuration information of direct rendering
drivers (DRI).

%prep
%setup -q

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xdriinfo
%{_mandir}/man1/xdriinfo.*
