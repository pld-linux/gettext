Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes.
Summary(pl):	Narzêdzia dla programów ze wsparciem dla jêzyków narodowych
Summary(tr):	Desteði için kitaplýk ve araçlar
Name:		gettext
Version:	0.10.35
Release:	12
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://alpha.gnu.org/gnu/%{name}-%{version}.tar.gz
Patch0:		gettext-jbj.patch
Patch1:		gettext-info.patch
Patch2:		gettext-arm.patch
Patch4:		gettext-Makefile.in.in.patach
Patch5:		gettext-DESTDIR.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
The gettext library provides an easy to use library and tools for creating,
using, and modifying natural language catalogs. It is a powerfull and simple
method for internationalizing programs.

%description -l de
Die gettext-Library enthält eine einfach anzuwendende Library und Tools
zum Erstellen, Verwenden und Ändern von natürlichsprachigen-Kataloge. Es ist
ein einfaches und leistungsfähiges Verfahren zum Lokalisieren von Programmen.

%description -l fr
La librarie gettext fournit des outils et une librairie simple à utiliser
pour manipuler, créer, et modifier des catalogues de langage naturel. C'est
une méthode simple et puissante pour internationnaliser les programmes.

%description -l pl
Pakiet gettext dostarcza narzêdzi do tworzenia, u¿ywania i modyfikacji
katalogów jêzyków narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) programów.

%description -l tr
gettext, yerel dil desteðinde kullanýlan kataloglarý deðiþtirebilmek için,
kolayca kullanýlabilen kitaplýk ve araçlarý saðlar. Bu, programlarý
uluslararasýlaþtýrmak için sýkça baþvurulan, kuvvetli bir yöntemdir.

%package devel
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes.
Summary(pl):	Narzêdzia dla programów ze wsparciem dla jêzyków narodowych
Summary(tr):	Desteði için kitaplýk ve araçlar
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Prereq:		/usr/sbin/fix-info-dir
Requires:	m4
Requires:	automake
Requires:	autoconf
Requires:	%{name} = %{version}

%description devel
The gettext library provides an easy to use library and tools for creating,
using, and modifying natural language catalogs. It is a powerfull and simple
method for internationalizing programs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-shared \
	--with-included-gettext 
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/bin

make install \
	DESTDIR=$RPM_BUILD_ROOT 

mv -f $RPM_BUILD_ROOT%{_bindir}/gettext $RPM_BUILD_ROOT/bin/gettext

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* \
	ABOUT-NLS AUTHORS BUGS ChangeLog DISCLAIM NEWS README* THANKS TODO
	
%find_lang %{name}

%post devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*.gz
%{_datadir}/aclocal/*
%{_datadir}/gettext
