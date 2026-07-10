%global tl_name arabi-add
%global tl_revision 67573

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Using hyperref and bookmark packages with arabic and farsi languages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/arabic/arabi-add
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi-add.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi-add.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package takes advantage of some of the possibilities that hyperref
and bookmark packages offer when you create a table of contents for
Arabic texts created by the arabi package.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/arabi-add
%dir %{_datadir}/texmf-dist/tex/latex/arabi-add
%doc %{_datadir}/texmf-dist/doc/latex/arabi-add/README
%doc %{_datadir}/texmf-dist/doc/latex/arabi-add/arabi-add-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arabi-add/arabi-add-example.pdf
%{_datadir}/texmf-dist/tex/latex/arabi-add/arabi-add.sty
