Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterst�tzung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes.
Summary(pl):	Narz�dzia dla program�w ze wsparciem dla j�zyk�w narodowych
Summary(tr):	Deste�i i�in kitapl�k ve ara�lar
Name:		gettext
Version:	0.10.35
Release:	10
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narz�dzia
Source:		ftp://alpha.gnu.org/gnu/%{name}-%{version}.tar.gz
Patch0:		gettext-jbj.patch
Patch1:		gettext-info.patch
Patch2:		gettext-arm.patch
Patch4:		gettext-Makefile.in.in.patach
Prereq:		/sbin/install-info
Requires:	m4
Requires:	automake
Requires:	autoconf
Buildroot:	/tmp/%{name}-%{version}-root

%description
The gettext library provides an easy to use library and tools for creating,
using, and modifying natural language catalogs. It is a powerfull and simple
method for internationalizing programs.

%description -l de
Die gettext-Library enth�lt eine einfach anzuwendende Library und Tools
zum Erstellen, Verwenden und �ndern von nat�rlichsprachigen-Kataloge. Es ist
ein einfaches und leistungsf�higes Verfahren zum Lokalisieren von Programmen.

%description -l fr
La librarie gettext fournit des outils et une librairie simple � utiliser
pour manipuler, cr�er, et modifier des catalogues de langage naturel. C'est
une m�thode simple et puissante pour internationnaliser les programmes.

%description -l pl
Pakiet gettext dostarcza narz�dzi do tworzenia, u�ywania i modyfikacji
katalog�w j�zyk�w narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) program�w.

%description -l tr
gettext, yerel dil deste�inde kullan�lan kataloglar� de�i�tirebilmek i�in,
kolayca kullan�labilen kitapl�k ve ara�lar� sa�lar. Bu, programlar�
uluslararas�la�t�rmak i�in s�k�a ba�vurulan, kuvvetli bir y�ntemdir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

%build
autoconf
%configure \
	--enable-shared \
	--with-included-gettext \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	SUBDIRS="doc lib src po m4 misc"

strip $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* \
	ABOUT-NLS AUTHORS BUGS ChangeLog DISCLAIM NEWS README* THANKS TODO
	
%find_lang %{name}

%post
/sbin/install-info %{_infodir}/gettext.info.gz /etc/info-dir

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/gettext.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*.gz
%{_datadir}/aclocal/*
%{_datadir}/gettext

%changelog
* Tue May 25 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.10.35-10]
- based on RH spec,
- rewrited by PLD team,
- pl translation by Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>.
