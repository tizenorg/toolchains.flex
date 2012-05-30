Name:           flex
Version:        2.5.35
Release:        2
License:        BSD
Summary:        A tool for creating scanners (text pattern recognizers)
Url:            http://flex.sourceforge.net/
Group:          Development/Tools
Source:         http://prdownloads.sourceforge.net/flex/flex-%{version}.tar.bz2
Source1001:     flex.manifest 
Patch0:         flex-2.5.35-sign.patch
# borrowed from fc12
Patch1:         flex-2.5.35-hardening.patch
Patch2:         flex-2.5.35-gcc44.patch
BuildRequires:  bison
BuildRequires:  m4
Requires:       m4

%description
The flex program generates scanners.  Scanners are programs which can
recognize lexical patterns in text.  Flex takes pairs of regular
expressions and C code as input and generates a C source file as
output.  The output file is compiled and linked with a library to
produce an executable.  The executable searches through its input for
occurrences of the regular expressions.  When a match is found, it
executes the corresponding C code.  Flex was designed to work with
both Yacc and Bison, and is used by many programs as part of their
build process.

You should install flex if you are going to use your system for
application development.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp %{SOURCE1001} .
%configure --disable-dependency-tracking CFLAGS="-fPIC %{optflags}" --disable-nls
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_infodir}/*

( cd %{buildroot}
  ln -sf flex .%{_bindir}/lex
  ln -sf flex .%{_bindir}/flex++
  ln -s libfl.a .%{_libdir}/libl.a
)

%remove_docs

%files 
%manifest flex.manifest
%doc COPYING
%{_bindir}/*
%{_libdir}/*.a
%{_includedir}/FlexLexer.h

