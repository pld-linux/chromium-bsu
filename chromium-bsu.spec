Summary: Chromium B.S.U. is a fast paced, arcade-style space shooter.
Name: chromium
Version: 0.9.12
Release: 6
License: Artistic
Group: Amusements/Games
Source0: http://www.reptilelabour.com/software/files/chromium/chromium-src-%{version}.tar.gz
Source1: http://www.reptilelabour.com/software/files/chromium/chromium-data-%{version}.tar.gz
Source2: Chromium.desktop
Source3: Chromium-Setup.desktop
Source4: chromium.xpm
patch: chromium-0.9-config.patch
URL: http://www.reptilelabour.com/software/chromium/
BuildPrereq: SDL-devel >= 1.1.6 Mesa-devel XFree86-devel >= 4.0
BuildPrereq: kdelibs-sound-devel esound-devel
Buildroot: %{_tmppath}/%{name}-root

%description
You are captain of the cargo ship Chromium B.S.U., responsible for
delivering supplies to our troops on the front line. Your ship
has a small fleet of robotic fighters which you control from the
relative safety of the Chromium vessel.
- Do not let ANY enemy ships get past your fighters! Each enemy
ship that makes it past the bottom of the screen will attack
the Chromium, and you lose a fighter.
- Use your fighters as weapons! Crash into enemies to destroy them
before they can get past you.
- Strategic suicide is a powerful tactic! When the Chromium
launches a new fighter, it releases a high energy burst which
destroys all enemies in range.
- Self-destruct to preserve your ammunition! A double-right-click
will cause your current fighter to self-destruct. Before the
ship blows up, it ejects its ammunition so that the next fighter
can pick it up.

%prep
%setup -q -n Chromium-0.9 -a 1
%patch -p1 -b .config
find . -type d -name .xvpics -exec rm -rf {} \; ||:

%build
QTDIR= && source /etc/profile.d/qt.sh

CFLAGS="$RPM_OPT_FLAGS" ./configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=%{_prefix} bindir=%{_bindir}
mkdir -p $RPM_BUILD_ROOT/etc/X11/applnk/Games \
         $RPM_BUILD_ROOT/usr/share/pixmaps

install %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/applnk/Games
install %{SOURCE4} $RPM_BUILD_ROOT/usr/share/pixmaps

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/pixmaps/chromium.xpm
%attr(644,root,root) /etc/X11/applnk/Games/*
/usr/games/chromium

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 12 2001 Tim Powers <timp@redhat.com>
- rebuild with new gcc and binutils

* Wed Jul 18 2001 Karsten Hopp <karsten@redhat.de>
- add buildprereq esound-devel (#49372)

* Tue Jul 10 2001 Elliot Lee <sopwith@redhat.com>
- Rebuild to remove libXv/libXxf86dga deps

* Fri Jun 22 2001 Preston Brown <pbrown@redhat.com>
- add buildprereqs
- build for dist

* Mon May 28 2001 Karsten Hopp <karsten@redhat.de>
- remove .xvpics from png directory

* Thu May 24 2001 Than Ngo <than@redhat.com>
- update to 0.9.12

* Wed Apr 04 2001 Karsten Hopp <karsten@redhat.de>
- add icon to desktop entries

* Tue Apr 03 2001 Karsten Hopp <karsten@redhat.de>
- Fix name of chromium-setup in kde menu

* Sat Mar 31 2001 Karsten Hopp <karsten@redhat.de>
- update to version 0.9.11
- added chromium-setup
- patched paths to get rid of shell-wrappers

* Thu Jan 11 2001 Karsten Hopp <karsten@redhat.de>
- Rebuild on IA64

* Thu Jan  4 2001 Tim Powers <timp@redhat.com>
- fixed ownership of files in file list so that it isn't owned by
  prospector

* Tue Nov 28 2000 Karsten Hopp <karsten@redhat.de>
- initial RPM
