Summary:	Chromium B.S.U. is a fast paced, arcade-style space shooter
Summary(pl):	Chromium B.S.U. to szybko tocz±ca siê strzelanina
Name:		chromium
Version:	0.9.12
Release:	8
License:	Artistic
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry

Source0:	http://www.reptilelabour.com/software/files/chromium/%{name}-src-%{version}.tar.gz
Source1:	http://www.reptilelabour.com/software/files/chromium/%{name}-data-%{version}.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}-setup.desktop
Source4:	%{name}.png

Patch0:         chromium-fix-flags.patch
Patch1:         chromium-glibc-2.2.2.patch
Patch3:         chromium-fix-openal-configurecall.patch
Patch4:         %{name}-configure_needs_bash.patch
Patch5:         %{name}-qt.patch
Patch6:         %{name}-use_proper_CC.patch

URL:		http://www.reptilelabour.com/software/chromium/

BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.6
BuildRequires:	libogg-devel libvorbis-devel
BuildRequires:	smpeg >= 0.4.2
BuildRequires:	qt-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define         _prefix         /usr/X11R6/
%define		_mandir		%{_prefix}/man
%define		_bindir		%{_prefix}/bin
%define         _datadir	%{_prefix}/share/games
%define         _noautoreqdep   libGL.so.1 libGLU.so.1 libGLcore.so.1
%define         _noreqdep       libGL.so.1 libGLU.so.1 libGLcore.so.1


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

%description -l pl
Jeste¶ kapitanem statku Chromium B.S.U, odpowiedzialnego za
dostarczenie zapasów do oddzia³ów na linii frontu. Statek ma ma³±
flotê automatycznych my¶liwców, którymi mo¿esz kierowaæ ze statku.
- Nie pozwól ¯ADNEMU wrogowi przej¶æ za swoje my¶liwce! Ka¿dy statek
  który dotrze na dó³ ekranu zaatakuje Chromium i stracisz my¶liwca.
- U¿ywaj my¶liwców jako broni! Uderzaj we wrogów aby zniszczyæ ich
  zanim oni przedostan± siê do ciebie.
- Strategiczne samobójstwo to dobra taktyka! Kiedy Chromium odpala
  nowego my¶liwca, wytwarza du¿o energii, która niszczy wszystkich
  wrogów w zasiêgu.
- Autodestrukcja pozwala zachowaæ amunicjê - przed wysadzeniem siê
  my¶liwiec zwraca amunicjê tak, ¿e nastêpny mo¿e j± przej±æ.


%package setup
Summary:        Setup frontend for Chromium
Summary(pl):	Graficzny konfigurator Chromium
Group:          X11/Applications/Games
Requires:       %{name} = %{version}-%{release}
Requires:	qt

%description setup
This package contains the setup frontend (using QT) to ease
configuration of Chromium, especially for its playlist features.

%description setup -l pl
Ten pakiet zawiera graficzny konfigurator (napisany w QT) u³atwiaj±cy
ustalanie parametrów dla gry Chromium, szczególnie je¶li chodzi o 
listê muzyki do odtwarzania.

%prep
%setup -q -n Chromium-0.9
%patch0 -p0
%patch1 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
find . -type d -name .xvpics -exec rm -rf {} \; ||:


%build
export CFLAGS="%{rpmcflags} -fno-omit-frame-pointer -pipe"
export CXXFLAGS="%{rpmcflags} -fno-omit-frame-pointer -pipe"
export CC=%{__cc}
export CXX=%{__cc}
export LINK=%{__cc}
export DEFS="%{rpmcflags} -DGAMESBINDIR=\\\"%{_bindir}\\\" \
	    -DPKGDATADIR=\\\"%{_datadir}/Chromium-0.9\\\" -DUSE_SDL \
	    `sdl-config --cflags` -DOLD_OPENAL -DAUDIO_OPENAL -D_REENTRANT \
	    -I../../include -I../support/openal/linux/include -I../support/openal/include"
#export OPENAL_CONFIG_OPTS="./configure %{_target_platform} --with-gcc=%{__cc}"
export OPENAL_CONFIG_OPTS="./configure --with-gcc=%{__cc}"
export QTDIR=%{_prefix}
./configure --enable-vorbis
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/{Games/Arcade,Settings},%{_pixmapsdir},%{_bindir},%{_datadir}}

# It is enough to install one file
#%{__make} install DESTDIR=RPM_BUILD_ROOT
install bin/* $RPM_BUILD_ROOT/%{_bindir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade/%{name}.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Settings/%{name}.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README LICENSE

#This installs datafiles
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT/%{_datadir}
find . -type d -name CVS -exec rm -rf {} \; ||:



%files
%defattr(644,root,root,755)
%doc LICENSE.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_pixmapsdir}/chromium.png
%{_applnkdir}/Games/Arcade/*


%files setup
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/chromium-setup
%{_applnkdir}/Settings/*

%clean
rm -rf $RPM_BUILD_ROOT
