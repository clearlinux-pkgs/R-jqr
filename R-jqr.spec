#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-jqr
Version  : 1.2.3
Release  : 40
URL      : https://cran.r-project.org/src/contrib/jqr_1.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/jqr_1.2.3.tar.gz
Summary  : Client for 'jq', a 'JSON' Processor
Group    : Development/Tools
License  : MIT
Requires: R-jqr-lib = %{version}-%{release}
Requires: R-lazyeval
Requires: R-magrittr
BuildRequires : R-lazyeval
BuildRequires : R-magrittr
BuildRequires : buildreq-R
BuildRequires : jq-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-jqr package.
Group: Libraries

%description lib
lib components for the R-jqr package.


%prep
%setup -q -c -n jqr
cd %{_builddir}/jqr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647017153

%install
export SOURCE_DATE_EPOCH=1647017153
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jqr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jqr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jqr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc jqr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/jqr/DESCRIPTION
/usr/lib64/R/library/jqr/INDEX
/usr/lib64/R/library/jqr/LICENSE
/usr/lib64/R/library/jqr/Meta/Rd.rds
/usr/lib64/R/library/jqr/Meta/data.rds
/usr/lib64/R/library/jqr/Meta/features.rds
/usr/lib64/R/library/jqr/Meta/hsearch.rds
/usr/lib64/R/library/jqr/Meta/links.rds
/usr/lib64/R/library/jqr/Meta/nsInfo.rds
/usr/lib64/R/library/jqr/Meta/package.rds
/usr/lib64/R/library/jqr/NAMESPACE
/usr/lib64/R/library/jqr/NEWS.md
/usr/lib64/R/library/jqr/R/jqr
/usr/lib64/R/library/jqr/R/jqr.rdb
/usr/lib64/R/library/jqr/R/jqr.rdx
/usr/lib64/R/library/jqr/data/Rdata.rdb
/usr/lib64/R/library/jqr/data/Rdata.rds
/usr/lib64/R/library/jqr/data/Rdata.rdx
/usr/lib64/R/library/jqr/help/AnIndex
/usr/lib64/R/library/jqr/help/aliases.rds
/usr/lib64/R/library/jqr/help/jqr.rdb
/usr/lib64/R/library/jqr/help/jqr.rdx
/usr/lib64/R/library/jqr/help/paths.rds
/usr/lib64/R/library/jqr/html/00Index.html
/usr/lib64/R/library/jqr/html/R.css
/usr/lib64/R/library/jqr/tests/testthat.R
/usr/lib64/R/library/jqr/tests/testthat/helper-jqr.R
/usr/lib64/R/library/jqr/tests/testthat/test-dsl.R
/usr/lib64/R/library/jqr/tests/testthat/test-peek.R
/usr/lib64/R/library/jqr/tests/testthat/test-spec.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/jqr/libs/jqr.so
/usr/lib64/R/library/jqr/libs/jqr.so.avx2
/usr/lib64/R/library/jqr/libs/jqr.so.avx512
