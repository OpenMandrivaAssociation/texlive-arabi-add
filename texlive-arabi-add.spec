Name:		texlive-arabi-add
Version:	37709
Release:	2
Summary:	Using hyperref and bookmark packages with arabic and farsi languages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arabi-add
License:	unknown
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi-add.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabi-add.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package takes advantage of some of the possibilities that
hyperref and bookmark packages offer when you create a table of
contents for Arabic texts created by the arabi package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/arabi-add
%doc %{_texmfdistdir}/doc/latex/arabi-add

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
