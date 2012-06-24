# _without_xemacs (--without xemacs)
Summary:	Utilties for program national language support
Summary(de):	Utilities zum Programmieren von nationaler Sprachunterst�tzung
Summary(fr):	Utilitaires pour le support de la langue nationnalepar les programmes
Summary(pl):	Narz�dzia dla program�w ze wsparciem dla j�zyk�w narodowych
Summary(tr):	Deste�i i�in kitapl�k ve ara�lar
Name:		gettext
Version:	0.10.38
Release:	2
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://ftp.gnu.org/pub/gnu/gettext/%{name}-%{version}.tar.gz
Patch0:		%{name}-jbj.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-dml.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
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

%description -l fr
La librarie gettext fournit des outils et une librairie simple �
utiliser pour manipuler, cr�er, et modifier des catalogues de langage
naturel. C'est une m�thode simple et puissante pour internationnaliser
les programmes.

%description -l pl
Pakiet gettext dostarcza narz�dzi do tworzenia, u�ywania i modyfikacji
katalog�w j�zyk�w narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) program�w.

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
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Requires:	%{name} = %{version}

%description devel
The gettext library provides an easy to use library and tools for
creating, using, and modifying natural language catalogs. It is a
powerfull and simple method for internationalizing programs.

%description -l pl devel
Pakiet gettext dostarcza narz�dzi do tworzenia, u�ywania i modyfikacji
katalog�w j�zyk�w narodowych. To jest prosta i wydajna metoda
lokalizacji (internationalizacji) program�w.

%package -n xemacs-po-mode-pkg
Summary:	Xemacs PO-mode
Summary(pl):	Tryb PO dla Xemacsa
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	xemacs

%description -n xemacs-po-mode-pkg
Emacs PO-mode.

%description -l pl -n xemacs-po-mode-pkg
Tryb edycji PO dla emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm m4/libtool.m4
libtoolize --copy --force
aclocal -I m4
autoconf
automake -a -c
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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

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
