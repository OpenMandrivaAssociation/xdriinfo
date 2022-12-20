Name:		xdriinfo
Version:	1.0.7
Release:	1
Summary:	Query configuration information of DRI drivers
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(gl)

%description
Driinfo can be used to query configuration information of direct rendering
drivers (DRI).

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xdriinfo
%doc %{_mandir}/man1/xdriinfo.*
