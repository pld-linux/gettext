# _without_xemacs (--without xemacs)
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(es):	Utilitarios para el programa de soporte a lenguas locales.
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl):	Narzêdzia dla programów ze wsparciem dla jêzyków narodowych
Summary(pt_BR):	Utilitários para o programa de suporte de línguas locais.
Summary(tr):	Desteði için kitaplýk ve araçlar
Name:		gettext
Version:	0.10.40
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/pub/gnu/gettext/%{name}-%{version}.tar.gz
Patch0:		%{name}-jbj.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-dml.patch
Patch3:		%{name}-aclocal.patch
Obsoletes:	gettext-base
BuildRequires:	automake
BuildRequires:	autoconf >= 2.50
BuildRequires:	libtool >= 1.4
BuildRequires:	texinfo
%{?!_without_xemacs:BuildRequires:	xemacs}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gettext library provides an easy to use library and tools for
creating, using, and modifying natural language catalogs. It is a
powerfull and simple method for internationalizing programs.

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

%description -l pl
Pakiet gettext dostarcza narzêdzi do tworzenia, u¿ywania i modyfikacji
katalogów jêzyków narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) programów.

%description -l pt_BR
A biblioteca gettext oferece uma biblioteca fácil de usar e
ferramentas para criação, uso e modificação de catálogos de linguagem
natural. Ele é um poderoso e simples método de internacionalização de
programas.

%description -l tr
gettext, yerel dil desteðinde kullanýlan kataloglarý deðiþtirebilmek
için, kolayca kullanýlabilen kitaplýk ve araçlarý saðlar. Bu,
programlarý uluslararasýlaþtýrmak için sýkça baþvurulan, kuvvetli bir
yöntemdir.

%package devel
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterstützung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl):	Narzêdzia dla programów ze wsparciem dla jêzyków narodowych
Summary(tr):	Desteði için kitaplýk ve araçlar
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f m4/libtool.m4 aclocal.m4 missing
libtoolize --copy --force
#aclocal --acdir=m4 -I $(aclocal --print-ac-dir)
aclocal -I m4
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

mv -f $RPM_BUILD_ROOT%{_bindir}/gettext $RPM_BUILD_ROOT/bin/gettext

gzip -9nf AUTHORS BUGS ChangeLog DISCLAIM NEWS README* THANKS TODO

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

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_aclocaldir}/*
%{_datadir}/gettext
%{_mandir}/man3/*

%{?!_without_xemacs:%files -n xemacs-po-mode-pkg}
%{?!_without_xemacs:%defattr(644,root,root,755)}
%{?!_without_xemacs:%dir %{_datadir}/xemacs-packages/lisp/po-mode}
%{?!_without_xemacs:%{_datadir}/xemacs-packages/lisp/po-mode/*.elc}
