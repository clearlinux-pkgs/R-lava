#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lava
Version  : 1.6.6
Release  : 30
URL      : https://cran.r-project.org/src/contrib/lava_1.6.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lava_1.6.6.tar.gz
Summary  : Latent Variable Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-SQUAREM
Requires: R-numDeriv
BuildRequires : R-SQUAREM
BuildRequires : R-numDeriv
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
with latent variables (MLE, 2SLS, and composite likelihood
	estimators) with both continuous, censored, and ordinal

%prep
%setup -q -c -n lava

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571853175

%install
export SOURCE_DATE_EPOCH=1571853175
rm -rf %{buildroot}
export LANG=C.UTF-8
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lava
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lava
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lava
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lava || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lava/CITATION
/usr/lib64/R/library/lava/DESCRIPTION
/usr/lib64/R/library/lava/INDEX
/usr/lib64/R/library/lava/Meta/Rd.rds
/usr/lib64/R/library/lava/Meta/data.rds
/usr/lib64/R/library/lava/Meta/demo.rds
/usr/lib64/R/library/lava/Meta/features.rds
/usr/lib64/R/library/lava/Meta/hsearch.rds
/usr/lib64/R/library/lava/Meta/links.rds
/usr/lib64/R/library/lava/Meta/nsInfo.rds
/usr/lib64/R/library/lava/Meta/package.rds
/usr/lib64/R/library/lava/NAMESPACE
/usr/lib64/R/library/lava/NEWS
/usr/lib64/R/library/lava/R/lava
/usr/lib64/R/library/lava/R/lava.rdb
/usr/lib64/R/library/lava/R/lava.rdx
/usr/lib64/R/library/lava/data/bmd.rda
/usr/lib64/R/library/lava/data/bmidata.rda
/usr/lib64/R/library/lava/data/brisa.rda
/usr/lib64/R/library/lava/data/calcium.rda
/usr/lib64/R/library/lava/data/hubble.rda
/usr/lib64/R/library/lava/data/hubble2.rda
/usr/lib64/R/library/lava/data/indoorenv.rda
/usr/lib64/R/library/lava/data/missingdata.rda
/usr/lib64/R/library/lava/data/nldata.rda
/usr/lib64/R/library/lava/data/nsem.rda
/usr/lib64/R/library/lava/data/semdata.rda
/usr/lib64/R/library/lava/data/serotonin.rda
/usr/lib64/R/library/lava/data/serotonin2.rda
/usr/lib64/R/library/lava/data/twindata.rda
/usr/lib64/R/library/lava/demo/estimation.R
/usr/lib64/R/library/lava/demo/inference.R
/usr/lib64/R/library/lava/demo/lava.R
/usr/lib64/R/library/lava/demo/model.R
/usr/lib64/R/library/lava/demo/simulation.R
/usr/lib64/R/library/lava/doc/reference.pdf
/usr/lib64/R/library/lava/gof1.png
/usr/lib64/R/library/lava/help/AnIndex
/usr/lib64/R/library/lava/help/aliases.rds
/usr/lib64/R/library/lava/help/lava.rdb
/usr/lib64/R/library/lava/help/lava.rdx
/usr/lib64/R/library/lava/help/paths.rds
/usr/lib64/R/library/lava/html/00Index.html
/usr/lib64/R/library/lava/html/R.css
/usr/lib64/R/library/lava/lava1.png
/usr/lib64/R/library/lava/me1.png
/usr/lib64/R/library/lava/mediation1.png
/usr/lib64/R/library/lava/mediation2.png
/usr/lib64/R/library/lava/tests/test-all.R
/usr/lib64/R/library/lava/tests/testthat/test-constrain.R
/usr/lib64/R/library/lava/tests/testthat/test-estimate_default.R
/usr/lib64/R/library/lava/tests/testthat/test-graph.R
/usr/lib64/R/library/lava/tests/testthat/test-inference.R
/usr/lib64/R/library/lava/tests/testthat/test-misc.R
/usr/lib64/R/library/lava/tests/testthat/test-model.R
/usr/lib64/R/library/lava/tests/testthat/test-multigroup.R
/usr/lib64/R/library/lava/tests/testthat/test-plot.R
/usr/lib64/R/library/lava/tests/testthat/test-sim.R
