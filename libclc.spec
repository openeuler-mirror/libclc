%global debug_package %{nil}

Name:           libclc
Version:        15.0.7
Release:        1
Summary:        An implementation of the library requirements of the OpenCL C
License:        BSD
URL:            https://libclc.llvm.org
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/%{name}-%{version}.src.tar.xz
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64 loongarch64
BuildRequires:  clang-devel libedit-devel llvm-devel >= 3.9 python3 zlib-devel
BuildRequires:  cmake spirv-llvm-translator-tools

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
%autosetup -n %{name}-%{version}.src -p1

%build
export CFLAGS="%{build_cflags} -D__extern_always_inline=inline"
%set_build_flags
%cmake -DCMAKE_INSTALL_DATADIR:PATH=%{_libdir}

%make_build

%install
%make_install

%check
make test ||:

%files
%license LICENSE.TXT
%doc README.TXT CREDITS.TXT
%dir %{_libdir}/clc
%{_libdir}/clc/*.bc
%{_libdir}/clc/spirv-mesa3d-.spv
%{_libdir}/clc/spirv64-mesa3d-.spv
%{_includedir}/clc

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue May 09 2023 ouuleilei <wangliu@iscas.ac.cn> - 15.0.7-1
- Upgrade libclc to 15.0.7.

* Thu Feb 16 2023 Wenlong Zhang<zhangwenlong@loongson.cn> - 12.0.1-2
- Add loongarch64 support

* Fri Mar 18 2022 yaoxin <yaoxin30@huawei.com> - 12.0.1-1
- Upgrade libclc to 12.0.1 to resolve compilation failures.

* Tue Aug 11 2020 yanan li <liyanan032@huawei.com> -0.2.0-16
- Modify python  to python3

* Thu Jul 09 2020 whoisxxx <zhangxuzhou4@huawei.com> - 0.2.0-15
- Add RISC-V arch

* Tue Dec 31 2019 Jiangping Hu <hujiangping@huawei.com> - 0.2.0-14
- Package init
