Summary:	Chromium B.S.U. is a fast paced, arcade-style space shooter
Name:		chromium
Version:	0.9.12
Release:	7
License:	Artistic
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.reptilelabour.com/software/files/chromium/%{name}-src-%{version}.tar.gz
Source1:	http://www.reptilelabour.com/software/files/chromium/%{name}-data-%{version}.tar.gz
Source2:	Chromium.desktop
Source3:	Chromium-Setup.desktop
Source4:	%{name}.xpm
Patch0:		%{name}-0.9-config.patch
URL:		http://www.reptilelabour.com/software/chromium/
BuildPrereq:	SDL-devel >= 1.1.6
BuildRequires:	OpenGL-devel
#BuildPrereq:	kdelibs-sound-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
You are captain of the cargo ship Chromium B.S.U., responsible for
delivering supplies to our troops on the front line. Your ship has a
small fleet of robotic fighters which you control from the relative
safety of the Chromium vessel.
- Do not let ANY enemy ships get past your fighters! Each enemy ship
  that makes it past the bottom of the screen will attack the Chromium,
  and you lose a fighter.
- Use your fighters as weapons! Crash into enemies to destroy them
  before they can get past you.
- Strategic suicide is a powerful tactic! When the Chromium launches a
  new fighter, it releases a high energy burst which destroys all
  enemies in range.
- Self-destruct to preserve your ammunition! A double-right-click will
  cause your current fighter to self-destruct. Before the ship blows up,
  it ejects its ammunition so that the next fighter can pick it up.

%prep
%setup -q -n Chromium-0.9 -a 1
%patch -p1
find . -type d -name .xvpics -exec rm -rf {} \; ||:

%build
CFLAGS="%{rpmcflags}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games \
         $RPM_BUILD_ROOT%{_datadir}/pixmaps

install %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Games
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/chromium.xpm
%{_applnkdir}/Games/*
%{_prefix}/games/chromium

%clean
rm -rf $RPM_BUILD_ROOT
