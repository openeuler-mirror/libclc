%global debug_package %{nil}

Name:           libclc
Version:        0.2.0
Release:        15
Summary:        An implementation of the library requirements of the OpenCL C
License:        BSD
URL:            https://libclc.llvm.org
Source0:        https://github.com/llvm-mirror/%{name}/archive/1ecb16dd7d8b8e9151027faab996f27b2ac508e3/%{name}-git1ecb16d.tar.gz
Patch0001:      0001-Modify-python-to-python3-with-configure.py.patch
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64
BuildRequires:  clang-devel libedit-devel llvm-devel >= 3.9 python3 zlib-devel

%description
bclc is an open source, BSD/MIT dual licensed implementation of the
library requirements of the OpenCL C programming language, as
specified by the OpenCL 1.1 Specification. The following sections
of the specification impose library requirements:

  * 6.1: Supported Data Types
  * 6.2.3: Explicit Conversions
  * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
  * 6.9: Preprocessor Directives and Macros
  * 6.11: Built-in Functions
  * 9.3: Double Precision Floating-Point
  * 9.4: 64-bit Atomics
  * 9.5: Writing to 3D image memory objects
  * 9.6: Half Precision Floating-Point

libclc is intended to be used with the Clang compiler's OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it
provides generic implementations of most library requirements,
allowing the target to override the generic implementation at the
granularity of individual functions.

libclc currently supports the AMDGCN, and R600 and NVPTX targets, but
support for more targets is welcome.

%package        devel
Summary:        Development files for libclc
Requires:       %{name} = %{version}-%{release}

%description    devel
The libclc-devel package contains libraries and header files for
developing applications that use libclc.

%prep
%autosetup -n %{name}-1ecb16dd7d8b8e9151027faab996f27b2ac508e3 -p1

%build
export CFLAGS="%{build_cflags} -D__extern_always_inline=inline"
%set_build_flags
./configure.py --prefix=%{_prefix} --libexecdir=%{_libdir}/clc/ --pkgconfigdir=%{_libdir}/pkgconfig/

%make_build

%install
%make_install

%files
%license LICENSE.TXT
%doc README.TXT CREDITS.TXT
%dir %{_libdir}/clc
%{_libdir}/clc/*.bc
%{_includedir}/clc

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 09 2020 whoisxxx <zhangxuzhou4@huawei.com> - 0.2.0-15
- Add RISC-V arch

* Tue Dec 31 2019 Jiangping Hu <hujiangping@huawei.com> - 0.2.0-14
- Package init
