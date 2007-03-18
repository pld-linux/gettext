#
# Conditional build:
%bcond_without	asprintf	# without libasprintf C++ library
%bcond_without	xemacs		# without po-mode for xemacs
%bcond_without	gcj		# with Java support by gcj (preferred over javac)
%bcond_with	javac		# with Java support by some javac
%bcond_without	dotnet		# without .NET support
#

%{?with_dotnet:%include	/usr/lib/rpm/macros.mono}

%ifnarch %{ix86} %{x8664} arm hppa ppc s390 s390x
%undefine with_dotnet
%endif
%ifarch i386
# plain i386 is not supported; mono uses cmpxchg/xadd which require i486
%undefine with_dotnet
%endif

%undefine with_xemacs

%define build_java	%{?with_gcj:1}%{!?with_gcj:%{?with_javac:1}%{!?with_javac:0}}
Summary:	Utilties for program national language support
Summary(de.UTF-8):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(es.UTF-8):	Utilitarios para el programa de soporte a lenguas locales
Summary(fr.UTF-8):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(ja.UTF-8):	マルチリンガルメッセージを生成するためのGNU ライブラリ/ユーティリティ
Summary(pl.UTF-8):	Narzędzia dla programów ze wsparciem dla języków narodowych
Summary(pt_BR.UTF-8):	Utilitários para o programa de suporte de línguas locais
Summary(ru.UTF-8):	Библиотеки и утилиты для поддержки национальных языков
Summary(tr.UTF-8):	Desteği için kitaplık ve araçlar
Summary(uk.UTF-8):	Бібліотеки та утиліти для підтримки національних мов
Name:		gettext
Version:	0.16.1
Release:	7
License:	LGPL (runtime), GPL (tools)
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.gz
# Source0-md5:	3d9ad24301c6d6b17ec30704a13fe127
Patch0:		%{name}-info.patch
Patch1:		%{name}-killkillkill.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-no_docs.patch
Patch4:		%{name}-ac.patch
Patch5:		%{name}-libintl_by_gcj.patch
URL:		http://www.gnu.org/software/gettext/
BuildRequires:	autoconf >= 2.59
# after dropping -ac.patch:
#BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
%{?with_gcj:BuildRequires:	gcj >= 3.0}
%{?with_javac:BuildRequires:	jdk >= 1.1}
BuildRequires:	libgomp-devel
%{?with_asprintf:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool >= 1:1.4.2-9
%{?with_dotnet:BuildRequires:	mono-csharp}
BuildRequires:	texinfo
%{?with_xemacs:BuildRequires:	xemacs}
Obsoletes:	gettext-base
Conflicts:	intltool < 0.28
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

%description -l de.UTF-8
Die gettext-Library enthält eine einfach anzuwendende Library und
Tools zum Erstellen, Verwenden und Ändern von
natürlichsprachigen-Kataloge. Es ist ein einfaches und
leistungsfähiges Verfahren zum Lokalisieren von Programmen.

%description -l es.UTF-8
La biblioteca gettext nos ofrece una biblioteca fácil de usar y
herramientas para creación, uso y modificación de catálogos de
lenguaje natural. Es un potente y sencillo método de
internacionalización de programas.

%description -l fr.UTF-8
La librarie gettext fournit des outils et une librairie simple à
utiliser pour manipuler, créer, et modifier des catalogues de langage
naturel. C'est une méthode simple et puissante pour internationnaliser
les programmes.

%description -l ja.UTF-8
GNU gettext
パッケージはプログラム中でマルチリンガルメッセージを生成する
ためのツールと文書を供給する。ツールはメッセージカタログをサポートするために
プログラムがどのように書かれるべきかの申し合わせと、メッセージカタログのための
ディレクトリとファイル名の組織化と、翻訳されたメッセージの埋め合わせを
サポートするためのランタイムライブラリと、翻訳可能でかつすでに翻訳された文字列
を取り扱う独立したプログラムを含んでいる。gettext
は簡単に使えるライブラリ
と自然言語のカタログを生成、使用、修正するツールと、国際化プログラム
のための強力かつシンプルな方法を供給する。

%description -l pl.UTF-8
Pakiet gettext dostarcza narzędzi do tworzenia, używania i modyfikacji
katalogów języków narodowych. To jest prosta i wydajna metoda
lokalizacji (internacjonalizacji) programów.

%description -l pt_BR.UTF-8
A biblioteca gettext oferece uma biblioteca fácil de usar e
ferramentas para criação, uso e modificação de catálogos de linguagem
natural. Ele é um poderoso e simples método de internacionalização de
programas.

%description -l ru.UTF-8
Пакет gettext содержит библиотеку и простые в использовании
инструменты для создания, использования и модификации каталогов
национальных языков. Это простой и мощный метод для
интернационализации программ.

%description -l tr.UTF-8
gettext, yerel dil desteğinde kullanılan katalogları değiştirebilmek
için, kolayca kullanılabilen kitaplık ve araçları sağlar. Bu,
programları uluslararasılaştırmak için sıkça başvurulan, kuvvetli bir
yöntemdir.

%description -l uk.UTF-8
Пакет gettext містить бібліотеку та прості у використанні інструменти
для створення, використання та модифікації каталогів національних мов.
Це простий та потужний метод для інтернаціоналізації програм.

%package devel
Summary:	Utilties for program national language support
Summary(de.UTF-8):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(fr.UTF-8):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl.UTF-8):	Narzędzia dla programów ze wsparciem dla języków narodowych
Summary(tr.UTF-8):	Desteği için kitaplık ve araçlar
License:	GPL
Group:		Development/Tools
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name} = %{version}-%{release}
Requires:	iconv
Conflicts:	autoconf < 2.52

%description devel
The gettext library provides an easy to use library and tools for
creating, using, and modifying natural language catalogs. It is a
powerfull and simple method for internationalizing programs.

%description devel -l pl.UTF-8
Pakiet gettext dostarcza narzędzi do tworzenia, używania i modyfikacji
katalogów języków narodowych. To jest prosta i wydajna metoda
lokalizacji (internacjonalizacji) programów.

%package static
Summary:	Static gettext utility libraries
Summary(pl.UTF-8):	Statyczne biblioteki narzędziowe gettext
License:	GPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static versions of gettext utility libraries
(libgettextlib, libgettextsrc and libgettextpo).

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne wersje bibliotek narzędziowych gettext
(libgettextlib, libgettextsrc i libgettextpo).

%package -n libasprintf
Summary:	GNU libasprintf - automatic formatted output to strings in C++
Summary(pl.UTF-8):	GNU libasprintf - automatyczne formatowanie wyjścia do łańcuchów w C++
License:	LGPL
Group:		Libraries

%description -n libasprintf
This package makes the C formatted output routines (`fprintf' et al.)
usable in C++ programs, for use with the `<string>' strings and the
`<iostream>' streams.

%description -n libasprintf -l pl.UTF-8
Ten pakiet czyni funkcje C formatujące wyjście (fprintf i inne)
używalnymi w programach w C++, z łańcuchami <string> i strumieniami
<iostream>.

%package -n libasprintf-devel
Summary:	Header file and documentation for libasprintf
Summary(pl.UTF-8):	Plik nagłówkowy i dokumentacja dla libasprintf
License:	LGPL
Group:		Development/Libraries
Requires:	libasprintf = %{version}-%{release}

%description -n libasprintf-devel
Header file and documentation for libasprintf.

%description -n libasprintf-devel -l pl.UTF-8
Plik nagłówkowy i dokumentacja dla libasprintf.

%package -n libasprintf-static
Summary:	Static libasprintf library
Summary(pl.UTF-8):	Statyczna biblioteka libasprintf
License:	LGPL
Group:		Development/Libraries
Requires:	libasprintf-devel = %{version}-%{release}

%description -n libasprintf-static
Static libasprintf library.

%description -n libasprintf-static -l pl.UTF-8
Statyczna biblioteka libasprintf.

%package java
Summary:	Runtime classes for Java programs internationalization
Summary(pl.UTF-8):	Klasy do uruchamiania umiędzynarodowionych programów w Javie
License:	LGPL
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description java
Runtime classes for Java programs internationalization.

%description java -l pl.UTF-8
Klasy do uruchamiania umiędzynarodowionych programów w Javie.

%package java-devel
Summary:	Development classes for Java programs internationalization
Summary(pl.UTF-8):	Klasy do umiędzynarodowiania programów w Javie dla programistów
License:	GPL
Group:		Development/Tools
Requires:	%{name}-devel = %{version}-%{release}

%description java-devel
Development classes for Java programs internationalization.

%description java-devel -l pl.UTF-8
Klasy do umiędzynarodowiania programów w Javie dla programistów.

%package -n xemacs-po-mode-pkg
Summary:	Xemacs PO-mode
Summary(es.UTF-8):	Facilita la edición de archivos PO (internacionalización) con emacs
Summary(pl.UTF-8):	Tryb PO dla Xemacsa
Summary(pt_BR.UTF-8):	Facilita a edição de arquivos PO (internacionalização) com o emacs
License:	GPL
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-po-mode-pkg
Emacs PO-mode.

%description -n xemacs-po-mode-pkg -l es.UTF-8
Este paquete suministra las herramientas para ayudar en la edición de
archivos PO, como documentado en el manual del usuario del GNU
gettext. Mira este manual para la documentación de uso, que no se
incluye aquí.

%description -n xemacs-po-mode-pkg -l pl.UTF-8
Tryb edycji PO dla emacsa.

%description -n xemacs-po-mode-pkg -l pt_BR.UTF-8
Este pacote provê as ferramentas para ajudar na edição de arquivos PO,
como documentado no manual do usuário do GNU gettext. Veja este manual
para a documentação de uso, a qual não é incluída aqui.

%package autopoint
Summary:	gettextize replacement
Summary(pl.UTF-8):	Zamiennik gettextize
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

%description autopoint -l pl.UTF-8
Program autopoint kopiuje standardowe pliki infrastruktury gettexta do
pakietu źródłowego. Wyciąga użytą wersję gettexta z wywołania makra w
postaci AM_GNU_GETTEXT_VERSION(VERSION) w pliku configure.in lub
configure.ac i kopiuje do pakietu pliki infrastruktury należące do tej
wersji.

%package -n dotnet-gettext
Summary:	GNU gettext for C#
Summary(pl.UTF-8):	GNU gettext dla C#
Group:		Development/Tools

%description -n dotnet-gettext
GNU gettext for C#.

%description -n dotnet-gettext -l pl.UTF-8
GNU gettext dla C#.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# patch not finished yet
#%patch3 -p1
%patch4 -p1
%patch5 -p1

%{__perl} -pi -e 's/ no / nb /' gettext-runtime/po/LINGUAS gettext-tools/po/LINGUAS
mv -f gettext-runtime/po/{no,nb}.po
mv -f gettext-runtime/po/{no,nb}.gmo
mv -f gettext-tools/po/{no,nb}.po
mv -f gettext-tools/po/{no,nb}.gmo
rm -f gettext-tools/po/stamp-po

%build
%{__libtoolize}
cd autoconf-lib-link
%{__aclocal} -I m4 -I ../m4
%{__autoconf}
%{__automake}
cd ../gettext-runtime
%{__aclocal} -I m4 -I gnulib-m4 -I ../autoconf-lib-link/m4 -I ../m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd libasprintf
%{__aclocal} -I ../m4 -I ../../m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../../gettext-tools
%{__aclocal} -I m4 -I gnulib-m4 -I libgettextpo/gnulib-m4 -I ../autoconf-lib-link/m4 -I ../gettext-runtime/m4 -I ../m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_xemacs:--with-lispdir=%{_datadir}/xemacs-packages/lisp/po-mode} \
	--enable-nls \
	%{!?with_dotnet:--disable-csharp} \
	%{?with_dotnet:--enable-csharp=mono} \
	--without-included-gettext
%{__make}

# msgfmt has been built, so now we can update pl.gmos
%{__make} pl.gmo -C gettext-runtime/po \
	GMSGFMT=`pwd`/gettext-tools/src/msgfmt
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
install gettext-tools/gnulib-lib/.libs/libgettextlib.a \
	gettext-tools/src/.libs/libgettextsrc.a $RPM_BUILD_ROOT%{_libdir}

rm -r $RPM_BUILD_ROOT%{_docdir}/gettext

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
%dir %{_libdir}/gettext
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
%attr(755,root,root) %{_libdir}/gettext/hostname
%attr(755,root,root) %{_libdir}/gettext/project-id
%attr(755,root,root) %{_libdir}/gettext/urlget
%attr(755,root,root) %{_libdir}/gettext/user-email
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
%attr(755,root,root) %{_libdir}/gettext/gnu.gettext.DumpResource
%attr(755,root,root) %{_libdir}/gettext/gnu.gettext.GetURL
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

%if %{with dotnet}
%files -n dotnet-gettext
%defattr(644,root,root,755)
%{_libdir}/GNU.Gettext.dll
%{_libdir}/gettext/msgfmt.net.exe
%{_libdir}/gettext/msgunfmt.net.exe
%endif
