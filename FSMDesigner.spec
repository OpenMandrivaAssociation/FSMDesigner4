%define name FSMDesigner4
%define version 1.1
%define release %mkrel 3

Summary: A Finite State Machine (FSM) design tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: %{name}-locate.patch
License: GPL
Group: Development/Other
Url: http://sourceforge.net/projects/fsmdesigner/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel, xerces-c-devel, python-devel, swig-devel, mlocate

%description
FSMDesigner4 is a C++ based implementation for a Finite State Machine (FSM)
design tool with integrated Hardware Description Language (HDL) generation.
FSMDesigner4 uses the Simple-Moore FSM model guaranteeing efficient fast
complex control circuits.

%prep
%setup -q
%patch0 -p0

%build
%configure --with-xerces-lib="-lxerces-c"
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS INSTALL ChangeLog
%{_bindir}/createf4tbar
%{_bindir}/createmmap
%{_bindir}/createtestbench
%{_bindir}/fsmdesigner4
%{_bindir}/fsmmin
%{_bindir}/fsmverification
%{_bindir}/fsmveriloggeneration
%{_bindir}/fsmvhdlgeneration
%{_libdir}/fsmdesigner.py

