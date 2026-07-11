%global tl_name hyper
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2d
Release:	%{tl_revision}.1
Summary:	Hypertext cross referencing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hyper
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyper.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyper.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Redefines LaTeX cross-referencing commands to insert \special commands
for HyperTeX dvi viewers, such as recent versions of xdvi. The package
is now largely superseded by hyperref.

