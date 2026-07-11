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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package takes advantage of some of the possibilities that hyperref
and bookmark packages offer when you create a table of contents for
Arabic texts created by the arabi package.

