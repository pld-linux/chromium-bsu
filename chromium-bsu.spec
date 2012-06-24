Summary:	Chromium B.S.U. is a fast paced, arcade-style space shooter
Summary(pl):	Chromium B.S.U. to szybko tocz�ca si� strzelanina
Name:		chromium
Version:	0.9.12
Release:	7
License:	Artistic
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.reptilelabour.com/software/files/chromium/%{name}-src-%{version}.tar.gz
Source1:	http://www.reptilelabour.com/software/files/chromium/%{name}-data-%{version}.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}-setup.desktop
Source4:	%{name}.png
Patch0:		%{name}-config.patch
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

%description -l pl
Jeste� kapitanem statku Chromium B.S.U, odpowiedzialnego za
dostarczenie zapas�w do oddzia��w na linii frontu. Statek ma ma��
flot� automatycznych my�liwc�w, kt�rymi mo�esz kierowa� ze statku.
- Nie pozw�l �ADNEMU wrogowi przej�� za swoje my�liwce! Ka�dy statek
  kt�ry dotrze na d� ekranu zaatakuje Chromium i stracisz my�liwca.
- U�ywaj my�liwc�w jako broni! Uderzaj we wrog�w aby zniszczy� ich
  zanim oni przedostan� si� do ciebie.
- Strategiczne samob�jstwo to dobra taktyka! Kiedy Chromium odpala
  nowego my�liwca, wytwarza du�o energii, kt�ra niszczy wszystkich
  wrog�w w zasi�gu.
- Autodestrukcja pozwala zachowa� amunicj� - przed wysadzeniem si�
  my�liwiec zwraca amunicj� tak, �e nast�pny mo�e j� przej��.

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
install -d $RPM_BUILD_ROOT{%{_applnkdir}/{Games/Arcade,Settings},%{_pixmapsdir}}

%{__make} install DESTDIR=RPM_BUILD_ROOT

install %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade/%{name}.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Settings/%{name}.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/chromium.xpm
%{_applnkdir}/Games/Arcade/*
%{_applnkdir}/Settings/*
%{_prefix}/games/chromium

%clean
rm -rf $RPM_BUILD_ROOT
