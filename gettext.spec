#
# Conditional build:
%bcond_without	asprintf	# libasprintf C++ library
%bcond_with	xemacs		# po-mode for xemacs
%bcond_without	d		# D support
%bcond_without	java		# convenience bcond to disable Java (any)
%bcond_with	gcj		# Java support by gcj (preferred over javac)
%bcond_without	javac		# Java support by some javac
%bcond_without	modula2		# Modula-2 support
%bcond_without	dotnet		# .NET support package
%bcond_with	bootstrap	# no system GLib, libcroco, libxml2 (for bootstrap)

%ifnarch %{ix86} %{x8664} %{arm} hppa ppc s390 s390x
%undefine with_dotnet
%endif
%ifarch i386
# plain i386 is not supported; mono uses cmpxchg/xadd which require i486
%undefine with_dotnet
%endif
%if %{with javac}
%undefine with_gcj
%define min_jdk_version 8
%{?use_default_jdk}
%endif
%if %{without java}
%undefine with_gcj
%undefine with_javac
%endif

%define build_java	%{?with_gcj:1}%{!?with_gcj:%{?with_javac:1}%{!?with_javac:0}}
%define	build_javaexe	%{?with_gcj:1}%{!?with_gcj:0}
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
Version:	0.25.1
Release:	2
License:	LGPL v2.1+ (libintl), GPL v3+ (tools)
Group:		Development/Tools
Source0:	https://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.lz
# Source0-md5:	f6cf89b61cc29a1f097d4766f2342f56
Patch0:		%{name}-info.patch
Patch1:		%{name}-killkillkill.patch
Patch2:		%{name}-smack.patch
Patch3:		%{name}-libdir.patch
URL:		http://www.gnu.org/software/gettext/
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.13
# also possible ldc, dmd, egdc (but gdc suppors more platforms)
%{?with_d:BuildRequires:	gcc-d}
%{?with_gcj:BuildRequires:	gcc-java >= 3.0}
%{?with_modula2:BuildRequires:	gcc-m2}
%{!?with_bootstrap:BuildRequires:	glib2-devel >= 2.0}
%{?with_gcj:BuildRequires:	jar}
%{?with_javac:%buildrequires_jdk}
%{!?with_bootstrap:BuildRequires:	libcroco-devel >= 0.6.1}
%if "%{cc_version}" >= "4.2"
BuildRequires:	libgomp-devel
%endif
BuildRequires:	libselinux-devel
%{?with_asprintf:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool >= 2:2
BuildRequires:	libunistring-devel
%{!?with_bootstrap:BuildRequires:	libxml2-devel}
BuildRequires:	lzip
%{?with_dotnet:BuildRequires:	mono-csharp}
BuildRequires:	ncurses-devel
%{?with_java:BuildRequires:	rpm-javaprov}
BuildRequires:	rpmbuild(macros) >= 2.021
BuildRequires:	sed >= 4.0
BuildRequires:	smack-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
%{?with_xemacs:BuildRequires:	xemacs}
Obsoletes:	gettext-base
Conflicts:	intltool < 0.28
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# adjust -f when needed (e.g. 0.18.3.x used ABI 0.18.3, 0.19.5.x uses full version)
%define		intabi	%(echo %{version} | cut -d. -f1-3)
# similarly for its data
%define		dataver	%(echo %{version} | cut -d. -f1-3)

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

%package tools
Summary:	Utilties for program national language support
Summary(de.UTF-8):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(fr.UTF-8):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl.UTF-8):	Narzędzia dla programów ze wsparciem dla języków narodowych
Summary(tr.UTF-8):	Desteği için kitaplık ve araçlar
License:	GPL v3+
Group:		Development/Tools
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	iconv
Conflicts:	autoconf < 2.52
Conflicts:	rpm-build-macros < 1.744

%description tools
This package contains tools for creating and modifying natural
language catalogs.

%description tools -l pl.UTF-8
Ten pakiet zawiera narzędzia do tworzenia i modyfikowania katalogów
z obsługą języków naturalnych.

%package demo
Summary:	Demo for gettext
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu gettext
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description demo
Demonstrations and samples for gettext.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu gettext.

%package libs
Summary:	Shared gettext utility libraries
Summary(pl.UTF-8):	Współdzielone biblioteki narzędziowe gettexta
License:	GPL v3+
Group:		Development/Libraries
# relaxed to allow newer package from libtextstyle.spec
Requires:	libtextstyle >= %{version}-%{release}

%description libs
This package contains shared versions of gettext utility libraries
(libgettextlib, libgettextsrc and libgettextpo).

%description libs -l pl.UTF-8
Ten pakiet zawiera współdzielone wersje bibliotek narzędziowych
gettext (libgettextlib, libgettextsrc i libgettextpo).

%package devel
Summary:	Development files for gettext libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek gettexta
License:	GPL v3+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# relaxed to allow newer package from libtextstyle.spec
Requires:	libtextstyle-devel >= %{version}-%{release}

%description devel
Development files for gettext libraries.

%description devel -l pl.UTF-8
Pliki programistyczne bibliotek gettexta.

%package static
Summary:	Static gettext utility libraries
Summary(pl.UTF-8):	Statyczne biblioteki narzędziowe gettext
License:	GPL v3+
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
License:	LGPL v2.1+
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
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libasprintf = %{version}-%{release}

%description -n libasprintf-devel
Header file and documentation for libasprintf.

%description -n libasprintf-devel -l pl.UTF-8
Plik nagłówkowy i dokumentacja dla libasprintf.

%package -n libasprintf-static
Summary:	Static libasprintf library
Summary(pl.UTF-8):	Statyczna biblioteka libasprintf
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	libasprintf-devel = %{version}-%{release}

%description -n libasprintf-static
Static libasprintf library.

%description -n libasprintf-static -l pl.UTF-8
Statyczna biblioteka libasprintf.

%package -n libtextstyle
Summary:	GNU libtextstyle - Text styling library
Summary(pl.UTF-8):	GNU libtextstyle - biblioteka do obsługi stylu tekstu
License:	GPL v3+

%description -n libtextstyle
This library provides an easy way to add styling to programs that
produce output to a console or terminal emulator window.

libtextstyle is for you if your application produces text that is more
readable when it is accompanied with styling information, such as
color, font attributes (weight, posture), or underlining.

%description -n libtextstyle -l pl.UTF-8
Ta biblioteka zapewnia łatwy sposób dodawania styli do programów
produkujących wyjście na konsoli lub w oknie emulatora terminala.

libtextstyle ma zastosowanie tam, gdzie aplikacja produkuje tekst,
który jest bardziej czytelny, jeśli jest wzbogacony o informacje o
stylu, takie jak kolor, atrybuty czcionek (grubość, nachylenie) lub
podkreślenie.

%package -n libtextstyle-devel
Summary:	Header files for libtextstyle library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtextstyle
License:	GPL v3+
Group:		Development/Libraries
Requires:	libtextstyle = %{version}-%{release}
Requires:	ncurses-devel

%description -n libtextstyle-devel
Header files for libtextstyle library.

%description -n libtextstyle-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtextstyle.

%package -n libtextstyle-static
Summary:	Static libtextstyle library
Summary(pl.UTF-8):	Statyczna biblioteka libtextstyle
License:	GPL v3+
Group:		Development/Libraries
Requires:	libtextstyle-devel = %{version}-%{release}

%description -n libtextstyle-static
Static libtextstyle library.

%description -n libtextstyle-static -l pl.UTF-8
Statyczna biblioteka libtextstyle.

%package d-devel
Summary:	Development library for D programs internationalization
Summary(pl.UTF-8):	Biblioteka programistyczna do umiędzynarodowiania programów w języku D
License: 	Boost v1.0
Group:		Development/Languages
#Requires:	d-compiler (dmd|gcc-d|ldc)

%description d-devel
Development library for D programs internationalization.

%description d-devel -l pl.UTF-8
Biblioteka programistyczna do umiędzynarodowiania programów w języku
D.

%package java
Summary:	Runtime classes for Java programs internationalization
Summary(pl.UTF-8):	Klasy do uruchamiania umiędzynarodowionych programów w Javie
License:	LGPL v2.1+
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description java
Runtime classes for Java programs internationalization.

%description java -l pl.UTF-8
Klasy do uruchamiania umiędzynarodowionych programów w Javie.

%package java-devel
Summary:	Development classes for Java programs internationalization
Summary(pl.UTF-8):	Klasy do umiędzynarodowiania programów w Javie dla programistów
License:	GPL v3+
Group:		Development/Tools
Requires:	%{name}-devel = %{version}-%{release}

%description java-devel
Development classes for Java programs internationalization.

%description java-devel -l pl.UTF-8
Klasy do umiędzynarodowiania programów w Javie dla programistów.

%package m2
Summary:	Runtime library for Modula-2 programs internationalization
Summary(pl.UTF-8):	Biblioteka do uruchamiania umiędzynarodowionych programów w języku Modula-2
License:	LGPL v2.1+
Group:		Libraries

%description m2
Runtime classes for Java programs internationalization.

%description m2 -l pl.UTF-8
Klasy do uruchamiania umiędzynarodowionych programów w Javie.

%package m2-devel
Summary:	Development library for Modula-2 programs internationalization
Summary(pl.UTF-8):	Biblioteka programistyczna do umiędzynarodowiania programów w języku Modula-2
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-m2 = %{version}-%{release}
Requires:	gcc-m2

%description m2-devel
Development library for Modula-2 programs internationalization.

%description m2-devel -l pl.UTF-8
Biblioteka programistyczna do umiędzynarodowiania programów w języku
Modula-2.

%package m2-static
Summary:	Static library for Modula-2 programs internationalization
Summary(pl.UTF-8):	Biblioteka statyczna do umiędzynarodowiania programów w języku Modula-2
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-m2-devel = %{version}-%{release}

%description m2-static
Static library for Modula-2 programs internationalization.

%description m2-static -l pl.UTF-8
Biblioteka statyczna do umiędzynarodowiania programów w języku
Modula-2.

%package -n xemacs-po-mode-pkg
Summary:	Xemacs PO-mode
Summary(es.UTF-8):	Facilita la edición de archivos PO (internacionalización) con emacs
Summary(pl.UTF-8):	Tryb PO dla Xemacsa
Summary(pt_BR.UTF-8):	Facilita a edição de arquivos PO (internacionalização) com o emacs
License:	GPL v2+
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
License:	GPL v3+
Group:		Development/Tools
Requires:	%{name}-devel >= 0.10.35
Requires:	xz

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
License:	LGPL v2.1+ (GNU.Gettext library), GPL v3+ (tools)
Group:		Development/Tools

%description -n dotnet-gettext
GNU gettext for C#.

%description -n dotnet-gettext -l pl.UTF-8
GNU gettext dla C#.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%{__sed} -i \
	-e 's@m4_esyscmd(\[build-aux/git-version-gen \.tarball-version\])@[%{version}]@' \
	configure.ac
%{__sed} -i \
	-e 's@m4_esyscmd(\[\.\./build-aux/git-version-gen \.\./\.tarball-version\])@[%{version}]@' \
	gettext-runtime/configure.ac \
	gettext-tools/configure.ac

%if %{without bootstrap}
%{__sed} -i -e '/gl_LIBCROCO\|gl_LIBGLIB\|gl_LIBXML/s/(\[yes\])//' libtextstyle/gnulib-m4/gnulib-comp.m4
%endif

%build
cd gettext-runtime
%{__libtoolize}
%{__aclocal} -I m4 -I ../m4 -I gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd intl
%{__libtoolize}
%{__aclocal} -I ../../m4 -I ../m4 -I gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../libasprintf
%{__aclocal} -I ../../m4 -I ../m4 -I gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../../libtextstyle
%{__libtoolize}
%{__aclocal} -I m4 -I gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../gettext-tools
%{__aclocal} -I m4 -I ../gettext-runtime/m4 -I ../m4 -I gnulib-m4 -I libgrep/gnulib-m4 -I libgettextpo/gnulib-m4 -I tests/gnulib-m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd examples
%{__aclocal} -I ../../gettext-runtime/m4 -I ../../m4
%{__autoconf}
%{__automake}
cd ../..
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gcj:GCJ=none} \
        %{?with_javac:JAVA="%{java_home}/bin/java" JAVAC="%{java_home}/bin/javac" JAR="%{java_home}/bin/jar"} \
	%{?with_xemacs:--with-lispdir=%{_datadir}/xemacs-packages/lisp/po-mode} \
	%{!?with_xemacs:--without-emacs} \
	--enable-csharp=%{?with_dotnet:mono}%{!?with_dotnet:no} \
	%{!?with_d:--disable-d} \
%if !%{build_java}
	--disable-java \
%endif
	%{!?with_modula2:--disable-modula2} \
	--enable-nls \
	--disable-silent-rules \
	--without-bzip2 \
	--without-git \
	--without-included-gettext \
	--with-xz
%{__make} \
	GMSGFMT=`pwd`/gettext-tools/src/msgfmt

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
install -d $RPM_BUILD_ROOT{/bin,%{_datadir}/gettext/its}

%{__make} install \
	examplesdir=%{_examplesdir}/%{name}-%{version} \
	examplesbuildauxdir=%{_examplesdir}/%{name}-%{version}/build-aux \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/{,n}gettext $RPM_BUILD_ROOT/bin

# these static libs are removed in install-exec-clean
cp -a gettext-tools/gnulib-lib/.libs/libgettextlib.a \
	gettext-tools/src/.libs/libgettextsrc.a $RPM_BUILD_ROOT%{_libdir}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gettext
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libasprintf
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libtextstyle
%{__rm} -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}-runtime
%find_lang %{name}-tools

%clean
rm -rf $RPM_BUILD_ROOT

%post	tools -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	tools -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n libasprintf -p /sbin/ldconfig
%postun	-n libasprintf -p /sbin/ldconfig

%post	-n libasprintf-devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n libasprintf-devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n libtextstyle -p /sbin/ldconfig
%postun	-n libtextstyle -p /sbin/ldconfig

%post	-n libtextstyle-devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n libtextstyle-devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	m2 -p /sbin/ldconfig
%postun	m2 -p /sbin/ldconfig

%files -f %{name}-runtime.lang
%defattr(644,root,root,755)
%attr(755,root,root) /bin/gettext
%attr(755,root,root) /bin/ngettext
%attr(755,root,root) %{_bindir}/envsubst
%attr(755,root,root) %{_bindir}/gettext.sh
%{_mandir}/man1/envsubst.1*
%{_mandir}/man1/gettext.1*
%{_mandir}/man1/ngettext.1*
%dir %{_libdir}/gettext
%dir %{_datadir}/gettext

%files tools
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/gettextize
%attr(755,root,root) %{_bindir}/msg*
%attr(755,root,root) %{_bindir}/recode-sr-latin
%attr(755,root,root) %{_bindir}/xgettext
%attr(755,root,root) %{_libdir}/preloadable_libintl.so
%dir %{_libexecdir}/gettext
%attr(755,root,root) %{_libexecdir}/gettext/cldr-plurals
%attr(755,root,root) %{_libexecdir}/gettext/hostname
%attr(755,root,root) %{_libexecdir}/gettext/project-id
%attr(755,root,root) %{_libexecdir}/gettext/urlget
%attr(755,root,root) %{_libexecdir}/gettext/user-email
%{_datadir}/gettext/ABOUT-NLS
%attr(755,root,root) %{_datadir}/gettext/config.rpath
%{_datadir}/gettext/disclaim-translations.txt
%{_datadir}/gettext/gettext.h
%dir %{_datadir}/gettext/its
%dir %{_datadir}/gettext/m4
%{_datadir}/gettext/m4/build-to-host.m4
%{_datadir}/gettext/m4/gettext.m4
%{_datadir}/gettext/m4/host-cpu-c-abi.m4
%{_datadir}/gettext/m4/iconv.m4
%{_datadir}/gettext/m4/intlmacosx.m4
%{_datadir}/gettext/m4/lib-ld.m4
%{_datadir}/gettext/m4/lib-link.m4
%{_datadir}/gettext/m4/lib-prefix.m4
%{_datadir}/gettext/m4/nls.m4
%{_datadir}/gettext/m4/po.m4
%{_datadir}/gettext/m4/progtest.m4
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
%{_datadir}/gettext/schema
%{_datadir}/gettext/styles
%dir %{_datadir}/gettext-%{dataver}
%{_datadir}/gettext-%{dataver}/its
%{_aclocaldir}/nls.m4
%{_infodir}/gettext.info*
%{_mandir}/man1/gettextize.1*
%{_mandir}/man1/msg*.1*
%{_mandir}/man1/recode-sr-latin.1*
%{_mandir}/man1/xgettext.1*
%{_mandir}/man3/bind_textdomain_codeset.3*
%{_mandir}/man3/bindtextdomain.3*
%{_mandir}/man3/dcgettext.3*
%{_mandir}/man3/dcngettext.3*
%{_mandir}/man3/dgettext.3*
%{_mandir}/man3/dngettext.3*
%{_mandir}/man3/gettext.3*
%{_mandir}/man3/ngettext.3*
%{_mandir}/man3/textdomain.3*

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files libs -f %{name}-tools.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgettextlib-%{intabi}.so
%attr(755,root,root) %{_libdir}/libgettextsrc-%{intabi}.so
%attr(755,root,root) %{_libdir}/libgettextpo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgettextpo.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgettextlib.so
%attr(755,root,root) %{_libdir}/libgettextsrc.so
%attr(755,root,root) %{_libdir}/libgettextpo.so
%{_libdir}/libgettextlib.la
%{_libdir}/libgettextsrc.la
%{_libdir}/libgettextpo.la
%{_includedir}/gettext-po.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgettextlib.a
%{_libdir}/libgettextsrc.a
%{_libdir}/libgettextpo.a

%if %{with asprintf}
%files -n libasprintf
%defattr(644,root,root,755)
%doc gettext-runtime/libasprintf/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/libasprintf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libasprintf.so.0

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

%files -n libtextstyle
%defattr(644,root,root,755)
%doc libtextstyle/{AUTHORS,NEWS,README}
%attr(755,root,root) %{_libdir}/libtextstyle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtextstyle.so.0

%files -n libtextstyle-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtextstyle.so
%{_libdir}/libtextstyle.la
%{_includedir}/textstyle.h
%{_includedir}/textstyle
%{_infodir}/libtextstyle.info*

%files -n libtextstyle-static
%defattr(644,root,root,755)
%{_libdir}/libtextstyle.a

%if %{with d}
%files d-devel
%{_libdir}/libintl_d.a
# XXX: shared (dmd, ...)
%dir %{_includedir}/d
%dir %{_includedir}/d/gnu
%{_includedir}/d/gnu/libintl
%endif

%if %{build_java}
%files java
%defattr(644,root,root,755)
%{_datadir}/gettext/libintl.jar

%files java-devel
%defattr(644,root,root,755)
%doc gettext-runtime/intl-java/javadoc2
%if %{build_javaexe}
%attr(755,root,root) %{_libdir}/gettext/gnu.gettext.DumpResource
%attr(755,root,root) %{_libdir}/gettext/gnu.gettext.GetURL
%else
%{_datadir}/gettext/gettext.jar
%endif
%{_datadir}/gettext/javaversion.class
%endif

%if %{with modula2}
%files m2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libintl_m2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libintl_m2.so.0

%files m2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libintl_m2.so
%{_libdir}/libintl_m2.la
# XXX: common dir for Modula-2 headers
%dir %{_includedir}/m2
%{_includedir}/m2/Libintl.def

%files m2-static
%defattr(644,root,root,755)
%{_libdir}/libintl_m2.a
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
%{_datadir}/gettext/archive.dir.tar.xz
%{_mandir}/man1/autopoint.1*

%if %{with dotnet}
%files -n dotnet-gettext
%defattr(644,root,root,755)
%{_libdir}/GNU.Gettext.dll
%{_libdir}/gettext/GNU.Gettext.dll
%{_libdir}/gettext/msgfmt.net.exe
%{_libdir}/gettext/msgunfmt.net.exe
%endif
