Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes.
Summary(pl):	Narzêdzia dla programów ze wsparciem dla jêzyków narodowych
Summary(tr):	Desteði için kitaplýk ve araçlar
Name:		gettext
Version:	0.10.35
Release:	10
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--enable-shared \
	--with-included-gettext \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/bin/* || :

gzip -9nf $RPM_BUILD_ROOT/usr/share/info/* \
	ABOUT-NLS AUTHORS BUGS ChangeLog DISCLAIM NEWS README* THANKS TODO

%post
/sbin/install-info /usr/share/info/gettext.info.gz /etc/info-dir

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/share/info/gettext.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/*
/usr/share/info/*info*.gz
/usr/share/aclocal/*
/usr/share/gettext
%lang(da) /usr/share/locale/da/LC_MESSAGES/gettext.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/gettext.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/gettext.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gettext.mo
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/gettext.mo
%lang(no) /usr/share/locale/no*/LC_MESSAGES/gettext.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/gettext.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/gettext.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/gettext.mo
%lang(sl) /usr/share/locale/sl/LC_MESSAGES/gettext.mo
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/gettext.mo

%changelog
* Mon Apr 12 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.10.35-9]
- standarized {un}registering info pages (added gettext-info.patch),
- removed emacs-po_mode subpackage (it would be beter add po mode macros
  directly in [x]emacs packages).

* Sat Sep 26 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- corrected pl translation.

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- include the aclocal support files.

* Fri Sep  3 1998 Bill Nottingham <notting@redhat.com>
- remove devel package (functionality is in glibc).

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.10.35-1]
- added missing %attr in %files for emacs-po_mode.

* Fri May 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.10.35-1]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} and %%{version} macro in Buildroot,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc). 
- added making emacsc-po_mode subpackage with emac extension for editing .po
  files,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/gettext.mo files,
- added %defattr macro in %files (require rpm >= 2.4.99).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
  [0.10-5]
- translations modified for de, fr, tr

* Sun Nov 02 1997 Cristian Gafton <gafton@redhat.com>
- added info handling
- added misc-patch (skip emacs-lisp modofications)

* Sat Nov 01 1997 Erik Troan <ewt@redhat.com>
- removed locale.aliases as we get it from glibc now
- uses a buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Built against glibc
