Summary:	A Finite State Machine (FSM) design tool
Name:		FSMDesigner4
Version:	4.2
Release:	%{mkrel 1}
Source0:	http://downloads.sourceforge.net/fsmdesigner/%{name}-%{version}.tar.gz
Patch10:	FSMDesigner4-4.2-link.patch
License:	GPLv2+
Group:		Development/Other
URL:		http://sourceforge.net/projects/fsmdesigner/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel
BuildRequires:	xerces-c-devel
BuildRequires:	python-devel
BuildRequires:	mlocate
BuildRequires:	swig
BuildRequires:	autoconf-archive

%description
FSMDesigner4 is a C++ based implementation for a Finite State Machine (FSM)
design tool with integrated Hardware Description Language (HDL) generation.
FSMDesigner4 uses the Simple-Moore FSM model guaranteeing efficient fast
complex control circuits.

%prep
%setup -q
%patch10 -p0 -b .link

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS INSTALL ChangeLog
%{_bindir}/createf4tbar
%{_bindir}/createmmap
%{_bindir}/createtestbench
%{_bindir}/dnfinvert
%{_bindir}/fsmdesigner4
%{_bindir}/fsmmin
%{_bindir}/fsmverification
%{_bindir}/fsmveriloggeneration
%{_bindir}/fsmvhdlgeneration
%{_libdir}/fsmdesigner.py

