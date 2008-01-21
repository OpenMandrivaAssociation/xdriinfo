Name: xdriinfo
Version: 1.0.2
Release: %mkrel 2
Summary: Query configuration information of DRI drivers
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libx11-devel		>= 1.1.3
BuildRequires: libmesagl-devel		>= 7.0.2

%description
Driinfo can be used to query configuration information of direct rendering
drivers (DRI).

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xdriinfo
%{_mandir}/man1/xdriinfo.*


