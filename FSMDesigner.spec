Summary:	A Finite State Machine (FSM) design tool
Name:		FSMDesigner4
Version:	1.2
Release:	%{mkrel 1}
Source0:	http://downloads.sourceforge.net/fsmdesigner/%{name}-%{version}.tar.gz
# Don't check for locate, it doesn't use it - AdamW 2008/12
Patch0:		FSMDesigner4-1.2-locate.patch
# Fix the Python check - AdamW 2008/12
Patch1:		FSMDesigner4-1.2-pythoncheck.patch
# Fix build with GCC 4.3 - AdamW 2008/12
Patch2:		FSMDesigner4-1.2-gcc43.patch
# @XERCES_CFLAGS@ doesn't actually exist at this point - AdamW 2008/12
Patch3:		FSMDesigner4-1.2-badflags.patch
# Fix underlinking (against xerces) - AdamW 2008/12
Patch4:		FSMDesigner4-1.2-link.patch
# Fix a missing include - AdamW 2008/12
Patch5:		FSMDesigner4-1.2-include.patch
License:	GPLv2+
Group:		Development/Other
URL:		http://sourceforge.net/projects/fsmdesigner/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel
BuildRequires:	xerces-c-devel
BuildRequires:	swig
BuildRequires:	python-devel

%description
FSMDesigner4 is a C++ based implementation for a Finite State Machine (FSM)
design tool with integrated Hardware Description Language (HDL) generation.
FSMDesigner4 uses the Simple-Moore FSM model guaranteeing efficient fast
complex control circuits.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoreconf -i
%configure2_5x --with-xerces-lib="-lxerces-c"
%make

%install
rm -rf %{buildroot}
%makeinstall

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

