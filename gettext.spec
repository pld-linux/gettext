#
# Conditional build:
# _without_xemacs	without po-mode for xemacs
# _with_gcj		with Java support by gcj requires gcj 3.x, but not 3.0.4+ (broken for now))
# _with_javac		with Java support by some javac
#
%define build_java	%{?_with_gcj:1}%{!?_with_gcj:%{?_with_javac:1}%{!?_with_javac:0}}
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(es):	Utilitarios para el programa de soporte a lenguas locales
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(ja):	¥Þ¥ë¥Á¥ê¥ó¥¬¥ë¥á¥Ã¥»¡¼¥¸¤òÀ¸À®¤¹¤ë¤¿¤á¤ÎGNU ¥é¥¤¥Ö¥é¥ê/¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(pl):	Narzêdzia dla programów ze wsparciem dla jêzyków narodowych
Summary(pt_BR):	Utilitários para o programa de suporte de línguas locais
Summary(ru):	âÉÂÌÉÏÔÅËÉ É ÕÔÉÌÉÔÙ ÄÌÑ ÐÏÄÄÅÒÖËÉ ÎÁÃÉÏÎÁÌØÎÙÈ ÑÚÙËÏ×
Summary(tr):	Desteði için kitaplýk ve araçlar
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÔÁ ÕÔÉÌ¦ÔÉ ÄÌÑ Ð¦ÄÔÒÉÍËÉ ÎÁÃ¦ÏÎÁÌØÎÉÈ ÍÏ×
Name:		gettext
Version:	0.11.5
Release:	6
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/pub/gnu/gettext/%{name}-%{version}.tar.gz
Patch0:		%{name}-jbj.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-aclocal.patch
Patch3:		%{name}-killkillkill.patch
Patch4:		%{name}-pl.po-update.patch
Patch5:		%{name}-gettextize-fix.patch
Patch6:		%{name}-missing-top_builddir.patch
Patch7:		%{name}-no_docs.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?_with_gcj:BuildRequires:	gcj >= 3.0}
%{?_with_gcj:BuildRequires:	gcj < 3.0.4}
%{?_with_javac:BuildRequires:	jdk >= 1.1}
BuildRequires:	libtool >= 1.4
BuildRequires:	texinfo
%{?!_without_xemacs:BuildRequires:	xemacs}
BuildRequires:	gettext-devel
Obsoletes:	gettext-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU gettext package provides a set of tools and documentation for
producing multi-lingual messages in programs. Tools include a set of
conventions about how programs should be written to support message
catalogs, a directory and file naming organization for the message
catalogs, a runtime library which supports the retrieval of translated
messages, and stand-alone programs for handling the translatable and
the already translated strings. Gettext provides an easy to use
library and tools for creating, using, and modifying natural language
catalogs and is a powerful and simple method for internationalizing
programs.

%description -l de
Die gettext-Library enthält eine einfach anzuwendende Library und
Tools zum Erstellen, Verwenden und Ändern von
natürlichsprachigen-Kataloge. Es ist ein einfaches und
leistungsfähiges Verfahren zum Lokalisieren von Programmen.

%description -l es
La biblioteca gettext nos ofrece una biblioteca fácil de usar y
herramientas para creación, uso y modificación de catálogos de
lenguaje natural. Es un potente y sencillo método de
internacionalización de programas.

%description -l fr
La librarie gettext fournit des outils et une librairie simple à
utiliser pour manipuler, créer, et modifier des catalogues de langage
naturel. C'est une méthode simple et puissante pour internationnaliser
les programmes.

%description -l ja
GNU gettext
¥Ñ¥Ã¥±¡¼¥¸¤Ï¥×¥í¥°¥é¥àÃæ¤Ç¥Þ¥ë¥Á¥ê¥ó¥¬¥ë¥á¥Ã¥»¡¼¥¸¤òÀ¸À®¤¹¤ë
¤¿¤á¤Î¥Ä¡¼¥ë¤ÈÊ¸½ñ¤ò¶¡µë¤¹¤ë¡£¥Ä¡¼¥ë¤Ï¥á¥Ã¥»¡¼¥¸¥«¥¿¥í¥°¤ò¥µ¥Ý¡¼¥È¤¹¤ë¤¿¤á¤Ë
¥×¥í¥°¥é¥à¤¬¤É¤Î¤è¤¦¤Ë½ñ¤«¤ì¤ë¤Ù¤­¤«¤Î¿½¤·¹ç¤ï¤»¤È¡¢¥á¥Ã¥»¡¼¥¸¥«¥¿¥í¥°¤Î¤¿¤á¤Î
¥Ç¥£¥ì¥¯¥È¥ê¤È¥Õ¥¡¥¤¥ëÌ¾¤ÎÁÈ¿¥²½¤È¡¢ËÝÌõ¤µ¤ì¤¿¥á¥Ã¥»¡¼¥¸¤ÎËä¤á¹ç¤ï¤»¤ò
¥µ¥Ý¡¼¥È¤¹¤ë¤¿¤á¤Î¥é¥ó¥¿¥¤¥à¥é¥¤¥Ö¥é¥ê¤È¡¢ËÝÌõ²ÄÇ½¤Ç¤«¤Ä¤¹¤Ç¤ËËÝÌõ¤µ¤ì¤¿Ê¸»úÎó
¤ò¼è¤ê°·¤¦ÆÈÎ©¤·¤¿¥×¥í¥°¥é¥à¤ò´Þ¤ó¤Ç¤¤¤ë¡£gettext
¤Ï´ÊÃ±¤Ë»È¤¨¤ë¥é¥¤¥Ö¥é¥ê
¤È¼«Á³¸À¸ì¤Î¥«¥¿¥í¥°¤òÀ¸À®¡¢»ÈÍÑ¡¢½¤Àµ¤¹¤ë¥Ä¡¼¥ë¤È¡¢¹ñºÝ²½¥×¥í¥°¥é¥à
¤Î¤¿¤á¤Î¶¯ÎÏ¤«¤Ä¥·¥ó¥×¥ë¤ÊÊýË¡¤ò¶¡µë¤¹¤ë¡£

%description -l pl
Pakiet gettext dostarcza narzêdzi do tworzenia, u¿ywania i modyfikacji
katalogów jêzyków narodowych. To jest prosta i wydajna metoda
lokalizacji (internacjonalizacji) programów.

%description -l pt_BR
A biblioteca gettext oferece uma biblioteca fácil de usar e
ferramentas para criação, uso e modificação de catálogos de linguagem
natural. Ele é um poderoso e simples método de internacionalização de
programas.

%description -l ru
ðÁËÅÔ gettext ÓÏÄÅÒÖÉÔ ÂÉÂÌÉÏÔÅËÕ É ÐÒÏÓÔÙÅ × ÉÓÐÏÌØÚÏ×ÁÎÉÉ
ÉÎÓÔÒÕÍÅÎÔÙ ÄÌÑ ÓÏÚÄÁÎÉÑ, ÉÓÐÏÌØÚÏ×ÁÎÉÑ É ÍÏÄÉÆÉËÁÃÉÉ ËÁÔÁÌÏÇÏ×
ÎÁÃÉÏÎÁÌØÎÙÈ ÑÚÙËÏ×. üÔÏ ÐÒÏÓÔÏÊ É ÍÏÝÎÙÊ ÍÅÔÏÄ ÄÌÑ
ÉÎÔÅÒÎÁÃÉÏÎÁÌÉÚÁÃÉÉ ÐÒÏÇÒÁÍÍ.

%description -l tr
gettext, yerel dil desteðinde kullanýlan kataloglarý deðiþtirebilmek
için, kolayca kullanýlabilen kitaplýk ve araçlarý saðlar. Bu,
programlarý uluslararasýlaþtýrmak için sýkça baþvurulan, kuvvetli bir
yöntemdir.

%description -l uk
ðÁËÅÔ gettext Í¦ÓÔÉÔØ Â¦ÂÌ¦ÏÔÅËÕ ÔÁ ÐÒÏÓÔ¦ Õ ×ÉËÏÒÉÓÔÁÎÎ¦ ¦ÎÓÔÒÕÍÅÎÔÉ
ÄÌÑ ÓÔ×ÏÒÅÎÎÑ, ×ÉËÏÒÉÓÔÁÎÎÑ ÔÁ ÍÏÄÉÆ¦ËÁÃ¦§ ËÁÔÁÌÏÇ¦× ÎÁÃ¦ÏÎÁÌØÎÉÈ ÍÏ×.
ãÅ ÐÒÏÓÔÉÊ ÔÁ ÐÏÔÕÖÎÉÊ ÍÅÔÏÄ ÄÌÑ ¦ÎÔÅÒÎÁÃ¦ÏÎÁÌ¦ÚÁÃ¦§ ÐÒÏÇÒÁÍ.

%package devel
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl):	Narzêdzia dla programów ze wsparciem dla jêzyków narodowych
Summary(tr):	Desteði için kitaplýk ve araçlar
Group:		Development/Tools
Requires:	%{name} = %{version}
Requires:	autoconf >= 2.50
Requires:	iconv

%description devel
The gettext library provides an easy to use library and tools for
creating, using, and modifying natural language catalogs. It is a
powerfull and simple method for internationalizing programs.

%description devel -l pl
Pakiet gettext dostarcza narzêdzi do tworzenia, u¿ywania i modyfikacji
katalogów jêzyków narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) programów.

%package java-devel
Summary:	Classes for Java programs internationalization
Summary(pl):	Klasy do umiêdzynarodowiania programów w Javie
Group:		Development/Tools
Requires:	%{name}-devel = %{version}

%description java-devel
Classes for Java programs internationalization.

%description java-devel -l pl
Klasy do umiêdzynarodowiania programów w Javie.

%package static
Summary:	Static gettext utility libraries
Summary(pl):	Statyczne biblioteki narzêdziowe gettext
Group:		Development/Libraries

%description static
This package contains static versions of gettext utility libraries
(libgettextlib and libgettextsrc).

%description static -l pl
Ten pakiet zawiera statyczne wersje bibliotek narzêdziowych gettext
(libgettextlib i libgettextsrc).

%package -n xemacs-po-mode-pkg
Summary:	Xemacs PO-mode
Summary(es):	Facilita la edición de archivos PO (internacionalización) con emacs
Summary(pl):	Tryb PO dla Xemacsa
Summary(pt_BR):	Facilita a edição de arquivos PO (internacionalização) com o emacs
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-po-mode-pkg
Emacs PO-mode.

%description -n xemacs-po-mode-pkg -l es
Este paquete suministra las herramientas para ayudar en la edición de
archivos PO, como documentado en el manual del usuario del GNU
gettext. Mira este manual para la documentación de uso, que no se
incluye aquí.

%description -n xemacs-po-mode-pkg -l pl
Tryb edycji PO dla emacsa.

%description -n xemacs-po-mode-pkg -l pt_BR
Este pacote provê as ferramentas para ajudar na edição de arquivos PO,
como documentado no manual do usuário do GNU gettext. Veja este manual
para a documentação de uso, a qual não é incluída aqui.

%package autopoint
Summary:	gettextize replacement
Summary(pl):	Zamiennik gettextize
Group:		Development/Tools
Requires:	%{name}-devel >= 0.10.35
Requires:	cvs

%description autopoint
The `autopoint' program copies standard gettext infrastructure files
into a source package. It extracts from a macro call of the form
`AM_GNU_GETTEXT_VERSION(VERSION)', found in the package's
`configure.in' or `configure.ac' file, the gettext version used by the
package, and copies the infrastructure files belonging to this version
into the package.

%description autopoint -l pl
Program autopoint kopiuje standardowe pliki infrastruktury gettexta do
pakietu ¼ród³owego. Wyci±ga u¿yt± wersjê gettexta z wywo³ania makra w
postaci AM_GNU_GETTEXT_VERSION(VERSION) w pliku configure.in lub
configure.ac i kopiuje do pakietu pliki infrastruktury nale¿±ce do tej
wersji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
rm -f m4/libtool.m4 aclocal.m4 missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{?!_without_xemacs:--with-lispdir=%{_datadir}/xemacs-packages/lisp/po-mode} \
	--enable-nls \
	--without-included-gettext
%{__make}

%{?!_without_xemacs:cd misc}
%{?!_without_xemacs:EMACS=%{_bindir}/xemacs ./elisp-comp ./po-mode.el}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/{,n}gettext $RPM_BUILD_ROOT/bin

# static libs are removed in install-exec-clean
install lib/.libs/lib*.a src/.libs/lib*.a $RPM_BUILD_ROOT%{_libdir}

# needed by uintmax.m4 (maybe automake is too old?)
install m4/ulonglong.m4 $RPM_BUILD_ROOT%{_aclocaldir}

# not supported by glibc 2.3.1
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{en@boldquot,en@quot}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*
%{_mandir}/man1/gettext.1*
%{_mandir}/man1/ngettext.1*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog DISCLAIM NEWS README* THANKS TODO
%attr(755,root,root) %{_bindir}/*
%exclude  %{_bindir}/autopoint
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/gettext
%{_infodir}/*info*
%{_aclocaldir}/*
%dir %{_datadir}/gettext
%{_datadir}/gettext/ABOUT-NLS
%attr(755,root,root) %{_datadir}/gettext/config.rpath
%{_datadir}/gettext/gettext.h
%dir %{_datadir}/gettext/intl
%{_datadir}/gettext/intl/[^c]*
%attr(755,root,root) %{_datadir}/gettext/intl/config.charset
%{_datadir}/gettext/msgunfmt.tcl
%attr(755,root,root) %{_datadir}/gettext/mkinstalldirs
%{_datadir}/gettext/po
%dir %{_datadir}/gettext/projects
%{_datadir}/gettext/projects/index
%attr(755,root,root) %{_datadir}/gettext/projects/team-address
%dir %{_datadir}/gettext/projects/GNOME
%{_datadir}/gettext/projects/GNOME/teams.*
%attr(755,root,root) %{_datadir}/gettext/projects/GNOME/team-address
%attr(755,root,root) %{_datadir}/gettext/projects/GNOME/trigger
%dir %{_datadir}/gettext/projects/KDE
%{_datadir}/gettext/projects/KDE/teams.*
%attr(755,root,root) %{_datadir}/gettext/projects/KDE/team-address
%attr(755,root,root) %{_datadir}/gettext/projects/KDE/trigger
%dir %{_datadir}/gettext/projects/TP
%{_datadir}/gettext/projects/TP/teams.*
%attr(755,root,root) %{_datadir}/gettext/projects/TP/team-address
%attr(755,root,root) %{_datadir}/gettext/projects/TP/trigger
%{_mandir}/man1/gettextize.1*
%{_mandir}/man1/msg*.1*
%{_mandir}/man1/xgettext.1*
%{_mandir}/man3/*

%if %{build_java}
%files java-devel
%defattr(644,root,root,755)
%doc intl-java/javadoc2
%{_datadir}/gettext/gettext.jar
%{_datadir}/gettext/libintl.jar
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{?_without_xemacs:0}%{?!_without_xemacs:1}
%files -n xemacs-po-mode-pkg
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/lisp/po-mode
%{_datadir}/xemacs-packages/lisp/po-mode/*.elc
%endif

%files autopoint
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/autopoint
%{_datadir}/gettext/archive.tar.gz
%{_mandir}/man1/autopoint.1*
