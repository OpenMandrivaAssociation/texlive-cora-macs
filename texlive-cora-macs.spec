%global tl_name cora-macs
%global tl_revision 76540

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for continuous sets and neural networks in the context of cyber-physic...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cora-macs
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cora-macs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cora-macs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package has been designed to assist in the representation and
manipulation of continuous sets, operations, neural networks, and color
schemes tailored for use in the context of cyber-physical systems. It
provides a comprehensive set of macros that streamline the process of
documenting complex mathematical objects and operations.

