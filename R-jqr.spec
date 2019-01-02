#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-jqr
Version  : 1.1.0
Release  : 1
URL      : https://cran.r-project.org/src/contrib/jqr_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/jqr_1.1.0.tar.gz
Summary  : Client for 'jq', a 'JSON' Processor
Group    : Development/Tools
License  : MIT
Requires: R-jqr-lib = %{version}-%{release}
Requires: R-jsonlite
Requires: R-lazyeval
Requires: R-rlang
BuildRequires : R-jsonlite
BuildRequires : R-lazyeval
BuildRequires : R-rlang
BuildRequires : buildreq-R
BuildRequires : jq-dev

%description
jqr
=======
[![Build Status](https://travis-ci.org/ropensci/jqr.svg?branch=master)](https://travis-ci.org/ropensci/jqr)
[![Build status](https://ci.appveyor.com/api/projects/status/tfwpiaotu24sotxg?svg=true)](https://ci.appveyor.com/project/sckott/jqr)
[![Coverage Status](https://coveralls.io/repos/ropensci/jqr/badge.svg?branch=master)](https://coveralls.io/r/ropensci/jqr?branch=master)
[![cran checks](https://cranchecks.info/badges/worst/jqr)](https://cranchecks.info/pkgs/jqr)
[![rstudio mirror downloads](http://cranlogs.r-pkg.org/badges/jqr?color=0DA6CD)](https://github.com/metacran/cranlogs.app)
[![cran version](http://www.r-pkg.org/badges/version/jqr)](https://cran.r-project.org/package=jqr)

%package lib
Summary: lib components for the R-jqr package.
Group: Libraries

%description lib
lib components for the R-jqr package.


%prep
%setup -q -c -n jqr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546443348

%install
export SOURCE_DATE_EPOCH=1546443348
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jqr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jqr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jqr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library jqr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/jqr/AUTHORS.jq
/usr/lib64/R/library/jqr/COPYING.jq
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
/usr/lib64/R/library/jqr/Meta/vignette.rds
/usr/lib64/R/library/jqr/NAMESPACE
/usr/lib64/R/library/jqr/NEWS.md
/usr/lib64/R/library/jqr/R/jqr
/usr/lib64/R/library/jqr/R/jqr.rdb
/usr/lib64/R/library/jqr/R/jqr.rdx
/usr/lib64/R/library/jqr/data/Rdata.rdb
/usr/lib64/R/library/jqr/data/Rdata.rds
/usr/lib64/R/library/jqr/data/Rdata.rdx
/usr/lib64/R/library/jqr/doc/index.html
/usr/lib64/R/library/jqr/doc/jqr_vignette.R
/usr/lib64/R/library/jqr/doc/jqr_vignette.Rmd
/usr/lib64/R/library/jqr/doc/jqr_vignette.html
/usr/lib64/R/library/jqr/help/AnIndex
/usr/lib64/R/library/jqr/help/aliases.rds
/usr/lib64/R/library/jqr/help/jqr.rdb
/usr/lib64/R/library/jqr/help/jqr.rdx
/usr/lib64/R/library/jqr/help/paths.rds
/usr/lib64/R/library/jqr/html/00Index.html
/usr/lib64/R/library/jqr/html/R.css
/usr/lib64/R/library/jqr/ignore/dotcomb.R
/usr/lib64/R/library/jqr/ignore/hacking.R
/usr/lib64/R/library/jqr/ignore/rivr.R
/usr/lib64/R/library/jqr/ignore/test-rivr.R
/usr/lib64/R/library/jqr/jq_version
/usr/lib64/R/library/jqr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/jqr/libs/jqr.so
/usr/lib64/R/library/jqr/libs/jqr.so.avx2
/usr/lib64/R/library/jqr/libs/jqr.so.avx512