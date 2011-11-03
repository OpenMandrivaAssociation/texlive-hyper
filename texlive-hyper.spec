# revision 17357
# category Package
# catalog-ctan /macros/latex/contrib/hyper
# catalog-date 2010-03-06 16:54:30 +0100
# catalog-license lppl
# catalog-version 4.2d
Name:		texlive-hyper
Version:	4.2d
Release:	1
Summary:	Hypertext cross referencing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hyper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyper.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyper.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Redefines LaTeX cross-referencing commands to insert \special
commands for HyperTeX dvi viewers, such as recent versions of
xdvi. The package is now largely superseded by hyperref.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hyper/amsart.hyp
%{_texmfdistdir}/tex/latex/hyper/amsbook.hyp
%{_texmfdistdir}/tex/latex/hyper/amsdtx.hyp
%{_texmfdistdir}/tex/latex/hyper/amsldoc.hyp
%{_texmfdistdir}/tex/latex/hyper/amsmath.hyp
%{_texmfdistdir}/tex/latex/hyper/amsproc.hyp
%{_texmfdistdir}/tex/latex/hyper/amstex.hyp
%{_texmfdistdir}/tex/latex/hyper/amsthm.hyp
%{_texmfdistdir}/tex/latex/hyper/article.hyp
%{_texmfdistdir}/tex/latex/hyper/book.hyp
%{_texmfdistdir}/tex/latex/hyper/cweb.hyp
%{_texmfdistdir}/tex/latex/hyper/doc.hyp
%{_texmfdistdir}/tex/latex/hyper/fancyheadings.hyp
%{_texmfdistdir}/tex/latex/hyper/ftnright.hyp
%{_texmfdistdir}/tex/latex/hyper/hxt-bc.sty
%{_texmfdistdir}/tex/latex/hyper/hyper.sty
%{_texmfdistdir}/tex/latex/hyper/leqno.hyp
%{_texmfdistdir}/tex/latex/hyper/letter.hyp
%{_texmfdistdir}/tex/latex/hyper/longtable.hyp
%{_texmfdistdir}/tex/latex/hyper/ltnews.hyp
%{_texmfdistdir}/tex/latex/hyper/ltxdoc.hyp
%{_texmfdistdir}/tex/latex/hyper/ltxguide.hyp
%{_texmfdistdir}/tex/latex/hyper/natbib.hyp
%{_texmfdistdir}/tex/latex/hyper/proc.hyp
%{_texmfdistdir}/tex/latex/hyper/report.hyp
%{_texmfdistdir}/tex/latex/hyper/slides.hyp
%{_texmfdistdir}/tex/latex/hyper/subeqnarray.hyp
%{_texmfdistdir}/tex/latex/hyper/theorem.hyp
%{_texmfdistdir}/tex/latex/hyper/upref.hyp
%{_texmfdistdir}/tex/latex/hyper/xr.hyp
%doc %{_texmfdistdir}/doc/latex/hyper/README
%doc %{_texmfdistdir}/doc/latex/hyper/TODO
%doc %{_texmfdistdir}/doc/latex/hyper/contrib/README
%doc %{_texmfdistdir}/doc/latex/hyper/contrib/harvard-to.hyp
%doc %{_texmfdistdir}/doc/latex/hyper/defpattern.sty
%doc %{_texmfdistdir}/doc/latex/hyper/hyper.pdf
%doc %{_texmfdistdir}/doc/latex/hyper/scontrib/README
%doc %{_texmfdistdir}/doc/latex/hyper/scontrib/harvard.hyp
#- source
%doc %{_texmfdistdir}/source/latex/hyper/Makefile-MSDos
%doc %{_texmfdistdir}/source/latex/hyper/Makefile-Unix
%doc %{_texmfdistdir}/source/latex/hyper/backcite.dtx
%doc %{_texmfdistdir}/source/latex/hyper/dvi2pdf.pl
%doc %{_texmfdistdir}/source/latex/hyper/hyper.dtx
%doc %{_texmfdistdir}/source/latex/hyper/hyper.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
