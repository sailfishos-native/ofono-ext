Name:       ofono-ext
Summary:    oFono extension APIs
Version:    1.0
Release:    1
License:    GPLv2
URL:        https://github.com/webOS-ports/ofono-ext
Source:     %{name}-%{version}.tar.bz2
Patch0:     0001-fix-libdir.patch
Requires:       ofono
BuildRequires:  ofono-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  libglibutil-devel

%description
oFono extension APIs for SailfishOS

%package devel
Summary:    Headers for oFono-ext
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for ofono extension APIs

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
make %{_smp_mflags}

%install
%make_install

%files
%{_libdir}/libofonoext.so*
%{_libdir}/ofono/plugins/ofonoextplugin.so

%files devel
%{_includedir}/ofono/
%{_libdir}/pkgconfig/
