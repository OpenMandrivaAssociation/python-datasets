Name:		python-datasets
Version:	5.0.1
Release:	2
Summary:	Hugging Face community library of datasets
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/huggingface/datasets
Source0:	https://files.pythonhosted.org/packages/source/d/datasets/datasets-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)

Requires:	python%{pyver}dist(filelock)
Requires:	python%{pyver}dist(numpy)
Requires:	python%{pyver}dist(pyarrow)
Requires:	python%{pyver}dist(dill)
Requires:	python%{pyver}dist(pandas)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(httpx)
Requires:	python%{pyver}dist(tqdm)
Requires:	python%{pyver}dist(xxhash)
Requires:	python%{pyver}dist(multiprocess)
Requires:	python%{pyver}dist(fsspec)
Requires:	python%{pyver}dist(huggingface-hub)
Requires:	python%{pyver}dist(packaging)
Requires:	python%{pyver}dist(pyyaml)

%description
Access and share datasets for audio, computer vision, and NLP. Used by
TRL (ORPO, DPO, SFT) and other Hugging Face training tools.

%prep -a
# Cooker fsspec is 2026.7.0; upstream still caps at 2026.6.0.
python - <<'PY'
from pathlib import Path
p = Path("setup.py")
t = p.read_text()
t = t.replace(
    '"fsspec[http]>=2023.1.0,<=2026.6.0"',
    '"fsspec[http]>=2023.1.0"',
)
p.write_text(t)
print("patched datasets setup.py fsspec pin")
PY

# pip writes .pyc then touches .py; extra tests treat that as
# python-bytecode-inconsistent-mtime.
%install -a
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find %{buildroot} -name '*.pyc' -delete

%files
%doc README.md
%license LICENSE
%{_bindir}/datasets-cli
%{py_sitedir}/datasets
%{py_sitedir}/datasets-*.*-info
