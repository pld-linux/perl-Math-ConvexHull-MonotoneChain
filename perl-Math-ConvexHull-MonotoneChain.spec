#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Math
%define		pnam	ConvexHull-MonotoneChain
%include	/usr/lib/rpm/macros.perl
Summary:	Math::ConvexHull::MonotoneChain - Andrew's monotone chain algorithm for finding a convex hull in 2D
Name:		perl-Math-ConvexHull-MonotoneChain
Version:	0.01
Release:	7
License:	Perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eaac1a9350f914fea5bbce2029b95b57
URL:		http://search.cpan.org/dist/Math-ConvexHull-MonotoneChain/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is somewhat experimental still.

This (XS) module optionally exports a single function convex_hull
which calculates the convex hull of the input points and returns it.
The algorithm is O(n log n) due to having to sort the input list, but
should be somewhat faster than a plain Graham's scan (also O(n log n))
in practice since it avoids polar coordinates.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorarch}/Math/ConvexHull
%{perl_vendorarch}/Math/ConvexHull/MonotoneChain.pm
%dir %{perl_vendorarch}/auto/Math/ConvexHull
%dir %{perl_vendorarch}/auto/Math/ConvexHull/MonotoneChain
%attr(755,root,root) %{perl_vendorarch}/auto/Math/ConvexHull/MonotoneChain/MonotoneChain.so
%{_mandir}/man3/*
