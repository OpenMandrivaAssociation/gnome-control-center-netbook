Name: gnome-control-center-netbook
Summary: Utilities to configure the netbook desktop
Version: 2.30.1
Release: %mkrel 1
Group: System/Desktop
License: GPLv2+ and GFDL
URL: https://www.gnome.org
Source0: http://download.gnome.org/sources/gnome-control-center/2.30/gnome-control-center-%{version}.tar.bz2
Source1: meego-translations.tar.bz2
Source2: gnome-appearance-properties.desktop
Source3: gnome-network-properties.desktop
Source4: gnome-settings-mouse.desktop
Source5: keyboard.desktop
Source6: gnome-control-center.desktop
Source100: gnome-control-center-netbook.yaml
Patch0: 0001-Add-new-shell-and-libgnome-control-center-extension.patch
Patch1: 0002-Add-Appearance-settings-panel.patch
Patch2: 0003-Add-Date-and-Time-panel.patch
Patch3: 0004-Add-Language-settings-panel.patch
Patch4: 0005-Add-minimal-display-capplet.patch
Patch5: 0006-Add-Keyboard-and-Shortcuts-settings-panel.patch
Patch6: 0007-Add-Pointer-settings-panel.patch
Patch7: 0008-Add-Network-settings-panel.patch
Patch8: 0009-Add-Security-settings-panel.patch
Patch9: 0010-Add-Power-settings-panel.patch
Patch10: 0011-shell-Don-t-include-both-Personal-and-Look-Feel.patch
Patch11: 0012-Don-t-build-capplets-not-used-by-MeeGo.patch
Patch12: 0013-appearance-Don-t-show-slide-show-backgrounds.patch
Requires: gnome-settings-daemon
Requires: gnome-icon-theme
Requires: gnome-menus
Requires: usermode
Requires: gnome-desktop
Requires: dbus-x11
Requires: GConf2
BuildRequires: libgtk+2-devel
BuildRequires: libglib2-devel
BuildRequires: libglade2-devel
BuildRequires: libgnome-desktop-2-devel
BuildRequires: librsvg2-devel
BuildRequires: libgnome-menu-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libpanel-applet-2
BuildRequires: libdbus-1-devel
BuildRequires: libdbus-glib-1-devel
BuildRequires: libxml2-devel
BuildRequires: libmeego-mutter-private-devel
BuildRequires: gnome-settings-daemon-devel
BuildRequires: libmetacity-private-devel
BuildRequires: libcanberra-devel
BuildRequires: libgnomekbd-devel
BuildRequires: evolution-data-server
BuildRequires: libxxf86misc-devel
BuildRequires: libxscrnsaver1-devel
BuildRequires: libgstreamer-devel
BuildRequires: libunique-devel
BuildRequires: desktop-file-utils
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: gnome-common
Provides: gnome-control-center = %{version}


%description
The GNOME control-center provides a number of extension points
for applications. This package contains directories where applications 
can install configuration files that are picked up by the control-center
utilities.



%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The control-center package contains configuration utilities for the 
GNOME desktop.

This package contains libraries and header files needed for integrating
configuration of applications such as window managers with the control-center
utilities.


%prep
%setup -a1 -n gnome-control-center-%{version}

# 0001-Add-new-shell-and-libgnome-control-center-extension.patch
%patch0 -p1
# 0002-Add-Appearance-settings-panel.patch
%patch1 -p1
# 0003-Add-Date-and-Time-panel.patch
%patch2 -p1
# 0004-Add-Language-settings-panel.patch
%patch3 -p1
# 0005-Add-minimal-display-capplet.patch
%patch4 -p1
# 0006-Add-Keyboard-and-Shortcuts-settings-panel.patch
%patch5 -p1
# 0007-Add-Pointer-settings-panel.patch
%patch6 -p1
# 0008-Add-Network-settings-panel.patch
%patch7 -p1
# 0009-Add-Security-settings-panel.patch
%patch8 -p1
# 0010-Add-Power-settings-panel.patch
%patch9 -p1
# 0011-shell-Don-t-include-both-Personal-and-Look-Feel.patch
%patch10 -p1
# 0012-Don-t-build-capplets-not-used-by-MeeGo.patch
%patch11 -p1
# 0013-appearance-Don-t-show-slide-show-backgrounds.patch
%patch12 -p1

%build
autoreconf --install
%configure2_5x \
  --disable-static \
  --disable-scrollkeeper \
  --disable-update-mimedb \
  --enable-moblin \
  --with-window-manager=mutter \
  --with-userpasswd \
  --enable-security

%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -m 0644 %{SOURCE2} %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE3} %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE4} %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE5} %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE6} %{buildroot}/%{_datadir}/applications

rm %{buildroot}%{_libdir}/control-center-1/extensions/*.la
rm %{buildroot}%{_libdir}/window-manager-settings/*.la
rm %{buildroot}%{_bindir}/gnome-typing-monitor

%find_lang gnome-control-center-2.0

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/gnome-control-center.schemas \
    > /dev/null || :
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/control-center.schemas \
    > /dev/null || :
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/fontilus.schemas \
    > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/gnome-control-center.schemas \
    > /dev/null || :
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/control-center.schemas \
    > /dev/null || :
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/fontilus.schemas \
    > /dev/null || :
fi

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/gnome-control-center.schemas  > /dev/null || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/control-center.schemas  > /dev/null || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/fontilus.schemas  > /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%postun
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :





%files -f gnome-control-center-2.0.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_datadir}/gnome-control-center/keybindings/*.xml
#%exclude %{_datadir}/gnome-control-center/default-apps/gnome-default-applications.xml
#%{_datadir}/gnome-control-center/glade
/usr/share/gnome-control-center/ui
%{_datadir}/gnome-control-center/pixmaps
%{_datadir}/applications/*.desktop
%{_datadir}/applications/mimeinfo.cache
%{_datadir}/desktop-directories/*
%{_datadir}/mime/packages/gnome-theme-package.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/gnome
%{_datadir}/omf
# list all binaries explicitly, so we notice if one goes missing
#%{_bindir}/gnome-about-me
%{_bindir}/gnome-appearance-properties
#%exclude %{_bindir}/gnome-at-mobility
#%exclude %{_bindir}/gnome-at-properties
#%exclude %{_bindir}/gnome-at-visual
%{_bindir}/gnome-control-center
#%exclude %{_bindir}/gnome-default-applications-properties
%{_bindir}/gnome-display-properties
#%exclude %{_bindir}/gnome-keybinding-properties
%{_bindir}/gnome-keyboard-properties
%{_bindir}/gnome-mouse-properties
%{_bindir}/gnome-network-properties
#%exclude %{_bindir}/gnome-window-properties
%{_bindir}/gnome-font-viewer
%{_bindir}/gnome-thumbnail-font
%{_libdir}/*.so.*
%{_sysconfdir}/gconf/schemas/gnome-control-center.schemas
%{_sysconfdir}/gconf/schemas/control-center.schemas
%{_sysconfdir}/gconf/schemas/fontilus.schemas
%{_sysconfdir}/xdg/menus/gnomecc.menu
#%exclude %{_sysconfdir}/xdg/autostart/gnome-at-session.desktop
%{_libdir}/window-manager-settings/*.so
%{_libdir}/control-center-1/extensions/*.so
%{_libexecdir}/cc-theme-thumbnailer-helper


%files devel
%defattr(-,root,root,-)
%{_includedir}/gnome-window-settings-2.0
%{_libdir}/libgnome-*.so
%{_datadir}/pkgconfig/gnome-keybindings.pc
#%exclude %{_datadir}/pkgconfig/gnome-default-applications.pc
%{_libdir}/pkgconfig/*
%{_libdir}/*.la
%{_includedir}/gnome-control-center-1

