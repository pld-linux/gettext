#
# Conditional build:
%bcond_without	asprintf	# without libasprintf C++ library
%bcond_without	xemacs		# without po-mode for xemacs
%bcond_with	gcj		# with Java support by gcj requires gcj 3.x, but not 3.0.4+ (broken for now))
%bcond_with	javac		# with Java support by some javac
#

%undefine with_xemacs

%define build_java	%{?with_gcj:1}%{!?with_gcj:%{?with_javac:1}%{!?with_javac:0}}
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
Version:	0.13
Release:	0.1
License:	LGPL (runtime), GPL (tools)
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/pub/gnu/gettext/%{name}-%{version}.tar.gz
# Source0-md5:	318e266ca3a5d26946ce3684db5bf2cf
Patch0:		%{name}-info.patch
Patch1:		%{name}-killkillkill.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-no_docs.patch
URL:		http://www.gnu.org/software/gettext/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.7.5
%{?with_gcj:BuildRequires:	gcj >= 3.0}
%{?with_gcj:BuildRequires:	gcj < 3.0.4}
%{?with_javac:BuildRequires:	jdk >= 1.1}
%{?with_asprintf:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	texinfo
%{?with_xemacs:BuildRequires:	xemacs}
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
License:	GPL
Group:		Development/Tools
Requires(post,postun):	/sbin/ldconfig
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

%package static
Summary:	Static gettext utility libraries
Summary(pl):	Statyczne biblioteki narz�dziowe gettext
License:	GPL
Group:		Development/Libraries

%description static
This package contains static versions of gettext utility libraries
(libgettextlib, libgettextsrc and libgettextpo).

%description static -l pl
Ten pakiet zawiera statyczne wersje bibliotek narz�dziowych gettext
(libgettextlib, libgettextsrc i libgettextpo).

%package -n libasprintf
Summary:	GNU libasprintf - automatic formatted output to strings in C++
Summary(pl):	GNU libasprintf - automatyczne formatowanie wyj�cia do �a�cuch�w w C++
License:	LGPL
Group:		Libraries

%description -n libasprintf
This package makes the C formatted output routines (`fprintf' et al.)
usable in C++ programs, for use with the `<string>' strings and the
`<iostream>' streams.

%description -n libasprintf -l pl
Ten pakiet czyni funkcje C formatuj�ce wyj�cie (fprintf i inne)
u�ywalnymi w programach w C++, z �a�cuchami <string> i strumieniami
<iostream>.

%package -n libasprintf-devel
Summary:	Header file and documentation for libasprintf
Summary(pl):	Plik nag��wkowy i dokumentacja dla libasprintf
License:	LGPL
Group:		Development/Libraries
Requires:	libasprintf = %{version}

%description -n libasprintf-devel
Header file and documentation for libasprintf.

%description -n libasprintf-devel -l pl
Plik nag��wkowy i dokumentacja dla libasprintf.

%package -n libasprintf-static
Summary:	Static libasprintf library
Summary(pl):	Statyczna biblioteka libasprintf
License:	LGPL
Group:		Development/Libraries
Requires:	libasprintf-devel = %{version}

%description -n libasprintf-static
Static libasprintf library.

%description -n libasprintf-static -l pl
Statyczna biblioteka libasprintf.

%package java
Summary:	Runtime classes for Java programs internationalization
Summary(pl):	Klasy do uruchamiania umi�dzynarodowionych program�w w Javie
License:	LGPL
Group:		Development/Languages/Java
Requires:	%{name} = %{version}

%description java
Runtime classes for Java programs internationalization.

%description java -l pl
Klasy do uruchamiania umi�dzynarodowionych program�w w Javie.

%package java-devel
Summary:	Development classes for Java programs internationalization
Summary(pl):	Klasy do umi�dzynarodowiania program�w w Javie dla programist�w
License:	GPL
Group:		Development/Tools
Requires:	%{name}-devel = %{version}

%description java-devel
Development classes for Java programs internationalization.

%description java-devel -l pl
Klasy do umi�dzynarodowiania program�w w Javie dla programist�w.

%package -n xemacs-po-mode-pkg
Summary:	Xemacs PO-mode
Summary(es):	Facilita la edici�n de archivos PO (internacionalizaci�n) con emacs
Summary(pl):	Tryb PO dla Xemacsa
Summary(pt_BR):	Facilita a edi��o de arquivos PO (internacionaliza��o) com o emacs
License:	GPL
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
License:	GPL
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
# patch3 not finished yet
#%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd gettext-runtime
%{__libtoolize}
%{__aclocal} -I m4 -I ../autoconf-lib-link/m4 -I ../gettext-tools/m4 -I ../config/m4
%{__autoconf}
%{__automake}
cd ../gettext-tools
%{__libtoolize}
%{__aclocal} -I m4 -I ../gettext-runtime/m4 -I ../autoconf-lib-link/m4 -I ../config/m4
%{__autoconf}
%{__automake}
cd ..
%configure \
	%{?with_xemacs:--with-lispdir=%{_datadir}/xemacs-packages/lisp/po-mode} \
	--enable-nls \
	--without-included-gettext
%{__make}

# msgfmt has been built, so now we can update pl.gmos
%{__make} pl.gmo -C gettext-tools/po \
	GMSGFMT=`pwd`/gettext-tools/src/msgfmt

%if %{with xemacs}
cd gettext-tools/misc
EMACS=%{_bindir}/xemacs ./elisp-comp ./po-mode.el
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/{,n}gettext $RPM_BUILD_ROOT/bin

# these static libs are removed in install-exec-clean
install gettext-tools/lib/.libs/libgettextlib.a \
	gettext-tools/src/.libs/libgettextsrc.a $RPM_BUILD_ROOT%{_libdir}

# not supported by glibc 2.3.1
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{en@boldquot,en@quot}

%find_lang %{name}-runtime
%find_lang %{name}-tools

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post	-n libasprintf -p /sbin/ldconfig
%postun	-n libasprintf -p /sbin/ldconfig

%post -n libasprintf-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n libasprintf-devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}-runtime.lang
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/envsubst
%{_mandir}/man1/envsubst.1*
%{_mandir}/man1/gettext.1*
%{_mandir}/man1/ngettext.1*
%dir %{_datadir}/gettext

%files devel -f %{name}-tools.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/autopoint
%exclude %{_bindir}/envsubst
%attr(755,root,root) %{_libdir}/libgettext*.so
%{_libdir}/libgettext*.la
# libgettextpo is for other programs, not used by gettext tools themselves
%attr(755,root,root) %{_libdir}/libgettextpo.so.*.*.*
%attr(755,root,root) %{_libdir}/preloadable_libintl.so
%attr(755,root,root) %{_libdir}/gettext
%{_includedir}/gettext-po.h
%{_aclocaldir}/*
%{_infodir}/gettext*.info*
%{_mandir}/man1/gettextize.1*
%{_mandir}/man1/msg*.1*
%{_mandir}/man1/xgettext.1*
%{_mandir}/man3/*

%{_datadir}/gettext/ABOUT-NLS
%attr(755,root,root) %{_datadir}/gettext/config.rpath
%{_datadir}/gettext/gettext.h
%dir %{_datadir}/gettext/intl
%{_datadir}/gettext/intl/[!c]*
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libgettext*.a

%if %{with asprintf}
%files -n libasprintf
%defattr(644,root,root,755)
%doc gettext-runtime/libasprintf/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/libasprintf.so.*.*.*

%files -n libasprintf-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasprintf.so
%{_libdir}/libasprintf.la
%{_includedir}/autosprintf.h
%{_infodir}/autosprintf.info*

%files -n libasprintf-static
%defattr(644,root,root,755)
%{_libdir}/libasprintf.a
%endif

%if %{build_java}
%files java
%defattr(644,root,root,755)
%{_datadir}/gettext/libintl.jar

%files java-devel
%defattr(644,root,root,755)
%doc gettext-runtime/intl-java/javadoc2
%{_datadir}/gettext/gettext.jar
%endif

%if %{with xemacs}
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
