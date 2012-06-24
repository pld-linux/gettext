# _without_xemacs (--without xemacs)
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterst�tzung
Summary(es):	Utilitarios para el programa de soporte a lenguas locales.
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl):	Narz�dzia dla program�w ze wsparciem dla j�zyk�w narodowych
Summary(pt_BR):	Utilit�rios para o programa de suporte de l�nguas locais.
Summary(tr):	Deste�i i�in kitapl�k ve ara�lar
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

%description -l pl
Pakiet gettext dostarcza narz�dzi do tworzenia, u�ywania i modyfikacji
katalog�w j�zyk�w narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) program�w.

%description -l pt_BR
A biblioteca gettext oferece uma biblioteca f�cil de usar e
ferramentas para cria��o, uso e modifica��o de cat�logos de linguagem
natural. Ele � um poderoso e simples m�todo de internacionaliza��o de
programas.

%description -l tr
gettext, yerel dil deste�inde kullan�lan kataloglar� de�i�tirebilmek
i�in, kolayca kullan�labilen kitapl�k ve ara�lar� sa�lar. Bu,
programlar� uluslararas�la�t�rmak i�in s�k�a ba�vurulan, kuvvetli bir
y�ntemdir.

%package devel
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterst�tzung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl):	Narz�dzia dla program�w ze wsparciem dla j�zyk�w narodowych
Summary(tr):	Deste�i i�in kitapl�k ve ara�lar
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
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
