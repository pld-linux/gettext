#
# Conditional build:
# _without_xemacs	without po-mode for xemacs
# _with_gcj		with Java support by gcj requires gcj 3.x, but not 3.0.4+ (broken for now))
# _with_javac		with Java support by some javac
#
%define build_java	%{?_with_gcj:1}%{!?_with_gcj:%{?_with_javac:1}%{!?_with_javac:0}}
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterst�tzung
Summary(es):	Utilitarios para el programa de soporte a lenguas locales
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(ja):	�ޥ����󥬥��å��������������뤿���GNU �饤�֥��/�桼�ƥ���ƥ�
Summary(pl):	Narz�dzia dla program�w ze wsparciem dla j�zyk�w narodowych
Summary(pt_BR):	Utilit�rios para o programa de suporte de l�nguas locais
Summary(ru):	���������� � ������� ��� ��������� ������������ ������
Summary(tr):	Deste�i i�in kitapl�k ve ara�lar
Summary(uk):	��̦����� �� ���̦�� ��� Ц������� ��æ�������� ���
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
Die gettext-Library enth�lt eine einfach anzuwendende Library und
Tools zum Erstellen, Verwenden und �ndern von
nat�rlichsprachigen-Kataloge. Es ist ein einfaches und
leistungsf�higes Verfahren zum Lokalisieren von Programmen.

%description -l es
La biblioteca gettext nos ofrece una biblioteca f�cil de usar y
herramientas para creaci�n, uso y modificaci�n de cat�logos de
lenguaje natural. Es un potente y sencillo m�todo de
internacionalizaci�n de programas.

%description -l fr
La librarie gettext fournit des outils et une librairie simple �
utiliser pour manipuler, cr�er, et modifier des catalogues de langage
naturel. C'est une m�thode simple et puissante pour internationnaliser
les programmes.

%description -l ja
GNU gettext
�ѥå������ϥץ������ǥޥ����󥬥��å���������������
����Υġ����ʸ��򶡵뤹�롣�ġ���ϥ�å������������򥵥ݡ��Ȥ��뤿���
�ץ���ब�ɤΤ褦�˽񤫤��٤����ο�����碌�ȡ���å������������Τ����
�ǥ��쥯�ȥ�ȥե�����̾���ȿ����ȡ��������줿��å�����������碌��
���ݡ��Ȥ��뤿��Υ�󥿥���饤�֥��ȡ�������ǽ�Ǥ��Ĥ��Ǥ��������줿ʸ����
���갷����Ω�����ץ�����ޤ�Ǥ��롣gettext
�ϴ�ñ�˻Ȥ���饤�֥��
�ȼ�������Υ����������������ѡ���������ġ���ȡ���ݲ��ץ����
�Τ���ζ��Ϥ��ĥ���ץ����ˡ�򶡵뤹�롣

%description -l pl
Pakiet gettext dostarcza narz�dzi do tworzenia, u�ywania i modyfikacji
katalog�w j�zyk�w narodowych. To jest prosta i wydajna metoda
lokalizacji (internacjonalizacji) program�w.

%description -l pt_BR
A biblioteca gettext oferece uma biblioteca f�cil de usar e
ferramentas para cria��o, uso e modifica��o de cat�logos de linguagem
natural. Ele � um poderoso e simples m�todo de internacionaliza��o de
programas.

%description -l ru
����� gettext �������� ���������� � ������� � �������������
����������� ��� ��������, ������������� � ����������� ���������
������������ ������. ��� ������� � ������ ����� ���
������������������� ��������.

%description -l tr
gettext, yerel dil deste�inde kullan�lan kataloglar� de�i�tirebilmek
i�in, kolayca kullan�labilen kitapl�k ve ara�lar� sa�lar. Bu,
programlar� uluslararas�la�t�rmak i�in s�k�a ba�vurulan, kuvvetli bir
y�ntemdir.

%description -l uk
����� gettext ͦ����� ¦�̦����� �� ����Ԧ � ����������Φ �����������
��� ���������, ������������ �� ����Ʀ��æ� ������Ǧ� ��æ�������� ���.
�� ������� �� �������� ����� ��� �������æ���̦��æ� �������.

%package devel
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterst�tzung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl):	Narz�dzia dla program�w ze wsparciem dla j�zyk�w narodowych
Summary(tr):	Deste�i i�in kitapl�k ve ara�lar
Group:		Development/Tools
Requires:	%{name} = %{version}
Requires:	autoconf >= 2.50
Requires:	iconv

%description devel
The gettext library provides an easy to use library and tools for
creating, using, and modifying natural language catalogs. It is a
powerfull and simple method for internationalizing programs.

%description devel -l pl
Pakiet gettext dostarcza narz�dzi do tworzenia, u�ywania i modyfikacji
katalog�w j�zyk�w narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) program�w.

%package java-devel
Summary:	Classes for Java programs internationalization
Summary(pl):	Klasy do umi�dzynarodowiania program�w w Javie
Group:		Development/Tools
Requires:	%{name}-devel = %{version}

%description java-devel
Classes for Java programs internationalization.

%description java-devel -l pl
Klasy do umi�dzynarodowiania program�w w Javie.

%package static
Summary:	Static gettext utility libraries
Summary(pl):	Statyczne biblioteki narz�dziowe gettext
Group:		Development/Libraries

%description static
This package contains static versions of gettext utility libraries
(libgettextlib and libgettextsrc).

%description static -l pl
Ten pakiet zawiera statyczne wersje bibliotek narz�dziowych gettext
(libgettextlib i libgettextsrc).

%package -n xemacs-po-mode-pkg
Summary:	Xemacs PO-mode
Summary(es):	Facilita la edici�n de archivos PO (internacionalizaci�n) con emacs
Summary(pl):	Tryb PO dla Xemacsa
Summary(pt_BR):	Facilita a edi��o de arquivos PO (internacionaliza��o) com o emacs
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-po-mode-pkg
Emacs PO-mode.

%description -n xemacs-po-mode-pkg -l es
Este paquete suministra las herramientas para ayudar en la edici�n de
archivos PO, como documentado en el manual del usuario del GNU
gettext. Mira este manual para la documentaci�n de uso, que no se
incluye aqu�.

%description -n xemacs-po-mode-pkg -l pl
Tryb edycji PO dla emacsa.

%description -n xemacs-po-mode-pkg -l pt_BR
Este pacote prov� as ferramentas para ajudar na edi��o de arquivos PO,
como documentado no manual do usu�rio do GNU gettext. Veja este manual
para a documenta��o de uso, a qual n�o � inclu�da aqui.

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
pakietu �r�d�owego. Wyci�ga u�yt� wersj� gettexta z wywo�ania makra w
postaci AM_GNU_GETTEXT_VERSION(VERSION) w pliku configure.in lub
configure.ac i kopiuje do pakietu pliki infrastruktury nale��ce do tej
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
