# TODO:
#  cvs cp chromium chromium-bsu
#
Summary:	Chromium B.S.U. is a fast paced, arcade-style space shooter
Summary(pl.UTF-8):	Chromium B.S.U. to szybko tocząca się strzelanina
Name:		chromium
Version:	0.9.14
Release:	0.1
License:	Artistic
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/chromium-bsu/%{name}-bsu-%{version}.tar.gz
# Source0-md5:	26df69b13e2ca370b6b45ac8e9efddd5
Patch0:		%{name}-bashizm.patch
URL:		http://www.reptilelabour.com/software/chromium/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.6
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freealut-devel
BuildRequires:	ftgl-devel >= 2.1.3
BuildRequires:	gettext-devel
BuildRequires:	libglpng-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	smpeg-devel >= 0.4.2
BuildRequires:	zlib-devel
Obsoletes:	chromium-setup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

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

%description -l pl.UTF-8
Jesteś kapitanem statku Chromium B.S.U, odpowiedzialnego za
dostarczenie zapasów do oddziałów na linii frontu. Statek ma małą
flotę automatycznych myśliwców, którymi możesz kierować ze statku.
- Nie pozwól ŻADNEMU wrogowi przejść za swoje myśliwce! Każdy statek
  który dotrze na dół ekranu zaatakuje Chromium i stracisz myśliwca.
- Używaj myśliwców jako broni! Uderzaj we wrogów aby zniszczyć ich
  zanim oni przedostaną się do ciebie.
- Strategiczne samobójstwo to dobra taktyka! Kiedy Chromium odpala
  nowego myśliwca, wytwarza dużo energii, która niszczy wszystkich
  wrogów w zasięgu.
- Autodestrukcja pozwala zachować amunicję - przed wysadzeniem się
  myśliwiec zwraca amunicję tak, że następny może ją przejąć.

%prep
%setup -q -n %{name}-bsu-%{version}
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-bsu

%find_lang %{name}-bsu

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-bsu.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README TODO data/doc/images data/doc/{faq,info}.htm
%attr(755,root,root) %{_bindir}/chromium-bsu
%{_datadir}/%{name}-bsu
%{_pixmapsdir}/chromium-bsu.png
%{_desktopdir}/%{name}-bsu.desktop
%{_mandir}/man6/*.6*
