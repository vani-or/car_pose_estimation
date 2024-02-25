```python
# EXECUTE THE FOLLOWING STATEMENTS ONLY IF YOU ARE RUNNING ON AWS SAGEMAKER STUDIO
!cd .. && make install_on_sagemaker
```

    pip3 install pipenv
    Collecting pipenv
      Using cached pipenv-2022.7.4-py2.py3-none-any.whl (3.7 MB)
    Requirement already satisfied: setuptools>=36.2.1 in /usr/local/lib/python3.8/dist-packages (from pipenv) (62.2.0)
    Collecting virtualenv
      Using cached virtualenv-20.15.1-py2.py3-none-any.whl (10.1 MB)
    Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from pipenv) (2019.11.28)
    Collecting virtualenv-clone>=0.2.5
      Using cached virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
    Requirement already satisfied: pip>=22.0.4 in /usr/local/lib/python3.8/dist-packages (from pipenv) (22.1)
    Requirement already satisfied: six<2,>=1.9.0 in /usr/lib/python3/dist-packages (from virtualenv->pipenv) (1.14.0)
    Collecting platformdirs<3,>=2
      Using cached platformdirs-2.5.2-py3-none-any.whl (14 kB)
    Collecting filelock<4,>=3.2
      Using cached filelock-3.7.1-py3-none-any.whl (10 kB)
    Collecting distlib<1,>=0.3.1
      Using cached distlib-0.3.5-py2.py3-none-any.whl (466 kB)
    Installing collected packages: distlib, virtualenv-clone, platformdirs, filelock, virtualenv, pipenv
    Successfully installed distlib-0.3.5 filelock-3.7.1 pipenv-2022.7.4 platformdirs-2.5.2 virtualenv-20.15.1 virtualenv-clone-0.5.7
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m[33mWARNING: There was an error checking the latest version of pip.[0m[33m
    [0mpipenv install
    [39m[1mInstalling dependencies from Pipfile.lock (bb774e)...[39m[22m
      🐍   [32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m[32m[1m▉[39m[22m 0/0 — [30m[22m00:00:00[39m[22m
    To activate this project's virtualenv, run [33m[22mpipenv shell[39m[22m.
    Alternatively, run a command inside the virtualenv with [33m[22mpipenv run[39m[22m.
    [0mpipenv lock -r > /tmp/pipenv-requirements.txt
    [33mWarning: The lock flag -r/--requirements will be deprecated in a future version
    of pipenv in favor of the new requirements command. For more info see
    https://pipenv.pypa.io/en/latest/advanced/#generating-a-requirements-txt
    NOTE: the requirements command parses Pipfile.lock directly without performing any
    locking operations. Updating packages should be done by running pipenv lock.[0m
    pip3 install -r /tmp/pipenv-requirements.txt
    Collecting absl-py==1.2.0
      Using cached absl_py-1.2.0-py3-none-any.whl (123 kB)
    Collecting albumentations==1.2.1
      Using cached albumentations-1.2.1-py3-none-any.whl (116 kB)
    Collecting alembic==1.8.1
      Using cached alembic-1.8.1-py3-none-any.whl (209 kB)
    Collecting antlr4-python3-runtime==4.9.3
      Using cached antlr4_python3_runtime-4.9.3-py3-none-any.whl
    Requirement already satisfied: argon2-cffi-bindings==21.2.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 13)) (21.2.0)
    Requirement already satisfied: argon2-cffi==21.3.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 14)) (21.3.0)
    Requirement already satisfied: asttokens==2.0.5 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 15)) (2.0.5)
    Requirement already satisfied: astunparse==1.6.3 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 16)) (1.6.3)
    Requirement already satisfied: attrs==21.4.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 17)) (21.4.0)
    Collecting autopage==0.5.1
      Using cached autopage-0.5.1-py3-none-any.whl (29 kB)
    Requirement already satisfied: backcall==0.2.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 19)) (0.2.0)
    Requirement already satisfied: beautifulsoup4==4.11.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 20)) (4.11.1)
    Collecting bleach==5.0.1
      Using cached bleach-5.0.1-py3-none-any.whl (160 kB)
    Collecting boto3==1.24.34
      Using cached boto3-1.24.34-py3-none-any.whl (132 kB)
    Collecting botocore==1.27.34
      Using cached botocore-1.27.34-py3-none-any.whl (9.0 MB)
    Collecting cachetools==5.2.0
      Using cached cachetools-5.2.0-py3-none-any.whl (9.3 kB)
    Collecting certifi==2022.6.15
      Using cached certifi-2022.6.15-py3-none-any.whl (160 kB)
    Collecting cffi==1.15.1
      Using cached cffi-1.15.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (442 kB)
    Collecting charset-normalizer==2.1.0
      Using cached charset_normalizer-2.1.0-py3-none-any.whl (39 kB)
    Collecting cliff==3.10.1
      Using cached cliff-3.10.1-py3-none-any.whl (81 kB)
    Collecting cloudpickle==2.1.0
      Using cached cloudpickle-2.1.0-py3-none-any.whl (25 kB)
    Collecting cmaes==0.8.2
      Using cached cmaes-0.8.2-py3-none-any.whl (15 kB)
    Collecting cmd2==2.4.2
      Using cached cmd2-2.4.2-py3-none-any.whl (147 kB)
    Collecting colorlog==6.6.0
      Using cached colorlog-6.6.0-py2.py3-none-any.whl (11 kB)
    Requirement already satisfied: cycler==0.11.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 33)) (0.11.0)
    Collecting debugpy==1.6.2
      Using cached debugpy-1.6.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.8 MB)
    Requirement already satisfied: decorator==5.1.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 35)) (5.1.1)
    Requirement already satisfied: defusedxml==0.7.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 36)) (0.7.1)
    Collecting dm-tree==0.1.7
      Using cached dm_tree-0.1.7-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (142 kB)
    Requirement already satisfied: entrypoints==0.4 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 38)) (0.4)
    Requirement already satisfied: executing==0.8.3 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 39)) (0.8.3)
    Collecting fastjsonschema==2.16.1
      Using cached fastjsonschema-2.16.1-py3-none-any.whl (22 kB)
    Requirement already satisfied: flatbuffers==2.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 41)) (2.0)
    Collecting fonttools==4.34.4
      Using cached fonttools-4.34.4-py3-none-any.whl (944 kB)
    Collecting gast==0.5.3
      Using cached gast-0.5.3-py3-none-any.whl (19 kB)
    Requirement already satisfied: google-auth-oauthlib==0.4.6 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 44)) (0.4.6)
    Collecting google-auth==2.9.1
      Using cached google_auth-2.9.1-py2.py3-none-any.whl (167 kB)
    Requirement already satisfied: google-pasta==0.2.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 46)) (0.2.0)
    Collecting greenlet==1.1.2
      Using cached greenlet-1.1.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (156 kB)
    Collecting grpcio==1.47.0
      Using cached grpcio-1.47.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.5 MB)
    Collecting h5py==3.7.0
      Using cached h5py-3.7.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (4.5 MB)
    Collecting hydra-core==1.2.0
      Using cached hydra_core-1.2.0-py3-none-any.whl (151 kB)
    Collecting idna==3.3
      Using cached idna-3.3-py3-none-any.whl (61 kB)
    Collecting imageio==2.19.5
      Using cached imageio-2.19.5-py3-none-any.whl (3.4 MB)
    Collecting importlib-metadata==4.12.0
      Using cached importlib_metadata-4.12.0-py3-none-any.whl (21 kB)
    Collecting importlib-resources==5.8.0
      Using cached importlib_resources-5.8.0-py3-none-any.whl (28 kB)
    Collecting ipykernel==6.15.1
      Using cached ipykernel-6.15.1-py3-none-any.whl (132 kB)
    Requirement already satisfied: ipython-genutils==0.2.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 56)) (0.2.0)
    Collecting ipython==8.4.0
      Using cached ipython-8.4.0-py3-none-any.whl (750 kB)
    Collecting jedi==0.18.1
      Using cached jedi-0.18.1-py2.py3-none-any.whl (1.6 MB)
    Requirement already satisfied: jinja2==3.1.2 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 59)) (3.1.2)
    Collecting jmespath==1.0.1
      Using cached jmespath-1.0.1-py3-none-any.whl (20 kB)
    Requirement already satisfied: joblib==1.1.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 61)) (1.1.0)
    Collecting jsonschema==4.7.2
      Using cached jsonschema-4.7.2-py3-none-any.whl (81 kB)
    Collecting jupyter-client==7.3.4
      Using cached jupyter_client-7.3.4-py3-none-any.whl (132 kB)
    Collecting jupyter-core==4.11.1
      Using cached jupyter_core-4.11.1-py3-none-any.whl (88 kB)
    Requirement already satisfied: jupyterlab-pygments==0.2.2 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 65)) (0.2.2)
    Requirement already satisfied: keras-preprocessing==1.1.2 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 66)) (1.1.2)
    Collecting keras==2.8.0
      Using cached keras-2.8.0-py2.py3-none-any.whl (1.4 MB)
    Collecting kiwisolver==1.4.4
      Using cached kiwisolver-1.4.4-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.2 MB)
    Requirement already satisfied: libclang==14.0.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 69)) (14.0.1)
    Collecting mako==1.2.1
      Using cached Mako-1.2.1-py3-none-any.whl (78 kB)
    Collecting markdown==3.4.1
      Using cached Markdown-3.4.1-py3-none-any.whl (93 kB)
    Requirement already satisfied: markupsafe==2.1.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 72)) (2.1.1)
    Requirement already satisfied: matplotlib-inline==0.1.3 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 73)) (0.1.3)
    Requirement already satisfied: matplotlib==3.5.2 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 74)) (3.5.2)
    Requirement already satisfied: mistune==0.8.4 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 75)) (0.8.4)
    Collecting nbclient==0.6.6
      Using cached nbclient-0.6.6-py3-none-any.whl (71 kB)
    Requirement already satisfied: nbconvert==6.5.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 77)) (6.5.0)
    Collecting nbformat==5.4.0
      Using cached nbformat-5.4.0-py3-none-any.whl (73 kB)
    Requirement already satisfied: nest-asyncio==1.5.5 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 79)) (1.5.5)
    Collecting networkx==2.8.5
      Using cached networkx-2.8.5-py3-none-any.whl (2.0 MB)
    Collecting notebook==6.4.12
      Using cached notebook-6.4.12-py3-none-any.whl (9.9 MB)
    Collecting numpy==1.23.1
      Using cached numpy-1.23.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.1 MB)
    Requirement already satisfied: oauthlib==3.2.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 83)) (3.2.0)
    Collecting omegaconf==2.2.2
      Using cached omegaconf-2.2.2-py3-none-any.whl (79 kB)
    Collecting opencv-python-headless==4.6.0.66
      Using cached opencv_python_headless-4.6.0.66-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (48.3 MB)
    Requirement already satisfied: opt-einsum==3.3.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 86)) (3.3.0)
    Collecting optuna==2.10.1
      Using cached optuna-2.10.1-py3-none-any.whl (308 kB)
    Requirement already satisfied: packaging==21.3 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 88)) (21.3)
    Collecting pandas==1.4.3
      Using cached pandas-1.4.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
    Requirement already satisfied: pandocfilters==1.5.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 90)) (1.5.0)
    Collecting parso==0.8.3
      Using cached parso-0.8.3-py2.py3-none-any.whl (100 kB)
    Collecting pbr==5.9.0
      Using cached pbr-5.9.0-py2.py3-none-any.whl (112 kB)
    Collecting pdoc3==0.10.0
      Using cached pdoc3-0.10.0-py3-none-any.whl (135 kB)
    Requirement already satisfied: pexpect==4.8.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 94)) (4.8.0)
    Requirement already satisfied: pickleshare==0.7.5 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 95)) (0.7.5)
    Collecting pillow==9.2.0
      Using cached Pillow-9.2.0-cp38-cp38-manylinux_2_28_x86_64.whl (3.2 MB)
    Collecting prettytable==3.3.0
      Using cached prettytable-3.3.0-py3-none-any.whl (26 kB)
    Requirement already satisfied: prometheus-client==0.14.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 98)) (0.14.1)
    Collecting prompt-toolkit==3.0.30
      Using cached prompt_toolkit-3.0.30-py3-none-any.whl (381 kB)
    Collecting protobuf==3.20
      Using cached protobuf-3.20.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.0 MB)
    Collecting psutil==5.9.1
      Using cached psutil-5.9.1-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (284 kB)
    Requirement already satisfied: ptyprocess==0.7.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 102)) (0.7.0)
    Requirement already satisfied: pure-eval==0.2.2 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 103)) (0.2.2)
    Collecting pyarrow==8.0.0
      Using cached pyarrow-8.0.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (29.4 MB)
    Requirement already satisfied: pyasn1-modules==0.2.8 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 105)) (0.2.8)
    Requirement already satisfied: pyasn1==0.4.8 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 106)) (0.4.8)
    Requirement already satisfied: pycparser==2.21 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 107)) (2.21)
    Requirement already satisfied: pygments==2.12.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 108)) (2.12.0)
    Requirement already satisfied: pyparsing==3.0.9 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 109)) (3.0.9)
    Collecting pyperclip==1.8.2
      Using cached pyperclip-1.8.2-py3-none-any.whl
    Requirement already satisfied: pyrsistent==0.18.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 111)) (0.18.1)
    Requirement already satisfied: python-dateutil==2.8.2 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 112)) (2.8.2)
    Collecting pytz==2022.1
      Using cached pytz-2022.1-py2.py3-none-any.whl (503 kB)
    Collecting pywavelets==1.3.0
      Using cached PyWavelets-1.3.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.9 MB)
    Collecting pyyaml==6.0
      Using cached PyYAML-6.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (701 kB)
    Collecting pyzmq==23.2.0
      Using cached pyzmq-23.2.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.1 MB)
    Collecting qudida==0.0.4
      Using cached qudida-0.0.4-py3-none-any.whl (3.5 kB)
    Requirement already satisfied: requests-oauthlib==1.3.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 118)) (1.3.1)
    Collecting requests==2.28.1
      Using cached requests-2.28.1-py3-none-any.whl (62 kB)
    Collecting rsa==4.9
      Using cached rsa-4.9-py3-none-any.whl (34 kB)
    Collecting s3transfer==0.6.0
      Using cached s3transfer-0.6.0-py3-none-any.whl (79 kB)
    Collecting scikit-image==0.19.3
      Using cached scikit_image-0.19.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (14.0 MB)
    Collecting scikit-learn==1.1.1
      Using cached scikit_learn-1.1.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (31.2 MB)
    Requirement already satisfied: scipy==1.8.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 124)) (1.8.1)
    Requirement already satisfied: send2trash==1.8.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 125)) (1.8.0)
    Collecting setuptools==63.2.0
      Using cached setuptools-63.2.0-py3-none-any.whl (1.2 MB)
    Collecting six==1.16.0
      Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
    Collecting sklearn==0.0
      Using cached sklearn-0.0-py2.py3-none-any.whl
    Requirement already satisfied: soupsieve==2.3.2.post1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 129)) (2.3.2.post1)
    Collecting sqlalchemy==1.4.39
      Using cached SQLAlchemy-1.4.39-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
    Collecting stack-data==0.3.0
      Using cached stack_data-0.3.0-py3-none-any.whl (23 kB)
    Collecting stevedore==4.0.0
      Using cached stevedore-4.0.0-py3-none-any.whl (49 kB)
    Requirement already satisfied: tensorboard-data-server==0.6.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 133)) (0.6.1)
    Requirement already satisfied: tensorboard-plugin-wit==1.8.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 134)) (1.8.1)
    Collecting tensorboard==2.8.0
      Using cached tensorboard-2.8.0-py3-none-any.whl (5.8 MB)
    Collecting tensorflow-io-gcs-filesystem==0.26.0
      Using cached tensorflow_io_gcs_filesystem-0.26.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (2.4 MB)
    Collecting tensorflow-probability==0.16.0
      Using cached tensorflow_probability-0.16.0-py2.py3-none-any.whl (6.3 MB)
    Collecting tensorflow==2.8
      Using cached tensorflow-2.8.0-cp38-cp38-manylinux2010_x86_64.whl (497.6 MB)
    Requirement already satisfied: termcolor==1.1.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 139)) (1.1.0)
    Requirement already satisfied: terminado==0.15.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 140)) (0.15.0)
    Collecting tf-estimator-nightly==2.8.0.dev2021122109
      Using cached tf_estimator_nightly-2.8.0.dev2021122109-py2.py3-none-any.whl (462 kB)
    Requirement already satisfied: threadpoolctl==3.1.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 142)) (3.1.0)
    Collecting tifffile==2022.5.4
      Using cached tifffile-2022.5.4-py3-none-any.whl (195 kB)
    Requirement already satisfied: tinycss2==1.1.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 144)) (1.1.1)
    Collecting tornado==6.2
      Using cached tornado-6.2-cp37-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (423 kB)
    Requirement already satisfied: tqdm==4.64.0 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 146)) (4.64.0)
    Collecting traitlets==5.3.0
      Using cached traitlets-5.3.0-py3-none-any.whl (106 kB)
    Collecting typing-extensions==4.3.0
      Using cached typing_extensions-4.3.0-py3-none-any.whl (25 kB)
    Collecting urllib3==1.26.10
      Using cached urllib3-1.26.10-py2.py3-none-any.whl (139 kB)
    Requirement already satisfied: wcwidth==0.2.5 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 150)) (0.2.5)
    Requirement already satisfied: webencodings==0.5.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 151)) (0.5.1)
    Requirement already satisfied: werkzeug==2.1.2 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 152)) (2.1.2)
    Collecting wheel==0.37.1
      Using cached wheel-0.37.1-py2.py3-none-any.whl (35 kB)
    Requirement already satisfied: wrapt==1.14.1 in /usr/local/lib/python3.8/dist-packages (from -r /tmp/pipenv-requirements.txt (line 154)) (1.14.1)
    Collecting zipp==3.8.1
      Using cached zipp-3.8.1-py3-none-any.whl (5.6 kB)
    Installing collected packages: tf-estimator-nightly, pytz, pyperclip, keras, fastjsonschema, dm-tree, antlr4-python3-runtime, zipp, wheel, urllib3, typing-extensions, traitlets, tornado, tensorflow-io-gcs-filesystem, six, setuptools, rsa, pyzmq, pyyaml, psutil, protobuf, prompt-toolkit, prettytable, pillow, pbr, parso, numpy, networkx, mako, kiwisolver, jmespath, idna, greenlet, gast, fonttools, debugpy, colorlog, cmd2, cloudpickle, charset-normalizer, cffi, certifi, cachetools, autopage, absl-py, tifffile, tensorflow-probability, stevedore, sqlalchemy, requests, pywavelets, pyarrow, opencv-python-headless, omegaconf, jupyter-core, jedi, importlib-resources, importlib-metadata, imageio, h5py, grpcio, google-auth, cmaes, bleach, stack-data, scikit-learn, scikit-image, pandas, markdown, jupyter-client, jsonschema, hydra-core, cliff, botocore, alembic, sklearn, s3transfer, qudida, pdoc3, optuna, nbformat, ipython, tensorboard, nbclient, ipykernel, boto3, albumentations, tensorflow, notebook
      Attempting uninstall: keras
        Found existing installation: keras 2.7.0
        Uninstalling keras-2.7.0:
          Successfully uninstalled keras-2.7.0
      Attempting uninstall: fastjsonschema
        Found existing installation: fastjsonschema 2.15.3
        Uninstalling fastjsonschema-2.15.3:
          Successfully uninstalled fastjsonschema-2.15.3
      Attempting uninstall: zipp
        Found existing installation: zipp 3.8.0
        Uninstalling zipp-3.8.0:
          Successfully uninstalled zipp-3.8.0
      Attempting uninstall: wheel
        Found existing installation: wheel 0.34.2
        Uninstalling wheel-0.34.2:
          Successfully uninstalled wheel-0.34.2
      Attempting uninstall: urllib3
        Found existing installation: urllib3 1.25.8
        Uninstalling urllib3-1.25.8:
          Successfully uninstalled urllib3-1.25.8
      Attempting uninstall: typing-extensions
        Found existing installation: typing_extensions 4.2.0
        Uninstalling typing_extensions-4.2.0:
          Successfully uninstalled typing_extensions-4.2.0
      Attempting uninstall: traitlets
        Found existing installation: traitlets 5.2.1.post0
        Uninstalling traitlets-5.2.1.post0:
          Successfully uninstalled traitlets-5.2.1.post0
      Attempting uninstall: tornado
        Found existing installation: tornado 6.1
        Uninstalling tornado-6.1:
          Successfully uninstalled tornado-6.1
      Attempting uninstall: tensorflow-io-gcs-filesystem
        Found existing installation: tensorflow-io-gcs-filesystem 0.25.0
        Uninstalling tensorflow-io-gcs-filesystem-0.25.0:
          Successfully uninstalled tensorflow-io-gcs-filesystem-0.25.0
      Attempting uninstall: six
        Found existing installation: six 1.14.0
        Uninstalling six-1.14.0:
          Successfully uninstalled six-1.14.0
      Attempting uninstall: setuptools
        Found existing installation: setuptools 62.2.0
        Uninstalling setuptools-62.2.0:
          Successfully uninstalled setuptools-62.2.0
      Attempting uninstall: rsa
        Found existing installation: rsa 4.8
        Uninstalling rsa-4.8:
          Successfully uninstalled rsa-4.8
      Attempting uninstall: pyzmq
        Found existing installation: pyzmq 22.3.0
        Uninstalling pyzmq-22.3.0:
          Successfully uninstalled pyzmq-22.3.0
      Attempting uninstall: psutil
        Found existing installation: psutil 5.9.0
        Uninstalling psutil-5.9.0:
          Successfully uninstalled psutil-5.9.0
      Attempting uninstall: protobuf
        Found existing installation: protobuf 3.20.1
        Uninstalling protobuf-3.20.1:
          Successfully uninstalled protobuf-3.20.1
      Attempting uninstall: prompt-toolkit
        Found existing installation: prompt-toolkit 3.0.29
        Uninstalling prompt-toolkit-3.0.29:
          Successfully uninstalled prompt-toolkit-3.0.29
      Attempting uninstall: pillow
        Found existing installation: Pillow 9.1.0
        Uninstalling Pillow-9.1.0:
          Successfully uninstalled Pillow-9.1.0
      Attempting uninstall: parso
        Found existing installation: parso 0.7.1
        Uninstalling parso-0.7.1:
          Successfully uninstalled parso-0.7.1
      Attempting uninstall: numpy
        Found existing installation: numpy 1.22.3
        Uninstalling numpy-1.22.3:
          Successfully uninstalled numpy-1.22.3
      Attempting uninstall: kiwisolver
        Found existing installation: kiwisolver 1.4.2
        Uninstalling kiwisolver-1.4.2:
          Successfully uninstalled kiwisolver-1.4.2
      Attempting uninstall: jmespath
        Found existing installation: jmespath 0.10.0
        Uninstalling jmespath-0.10.0:
          Successfully uninstalled jmespath-0.10.0
      Attempting uninstall: idna
        Found existing installation: idna 2.8
        Uninstalling idna-2.8:
          Successfully uninstalled idna-2.8
      Attempting uninstall: gast
        Found existing installation: gast 0.4.0
        Uninstalling gast-0.4.0:
          Successfully uninstalled gast-0.4.0
      Attempting uninstall: fonttools
        Found existing installation: fonttools 4.33.3
        Uninstalling fonttools-4.33.3:
          Successfully uninstalled fonttools-4.33.3
      Attempting uninstall: debugpy
        Found existing installation: debugpy 1.6.0
        Uninstalling debugpy-1.6.0:
          Successfully uninstalled debugpy-1.6.0
      Attempting uninstall: cffi
        Found existing installation: cffi 1.15.0
        Uninstalling cffi-1.15.0:
          Successfully uninstalled cffi-1.15.0
      Attempting uninstall: certifi
        Found existing installation: certifi 2019.11.28
        Uninstalling certifi-2019.11.28:
          Successfully uninstalled certifi-2019.11.28
      Attempting uninstall: cachetools
        Found existing installation: cachetools 5.1.0
        Uninstalling cachetools-5.1.0:
          Successfully uninstalled cachetools-5.1.0
      Attempting uninstall: absl-py
        Found existing installation: absl-py 1.0.0
        Uninstalling absl-py-1.0.0:
          Successfully uninstalled absl-py-1.0.0
      Attempting uninstall: requests
        Found existing installation: requests 2.22.0
        Uninstalling requests-2.22.0:
          Successfully uninstalled requests-2.22.0
      Attempting uninstall: jupyter-core
        Found existing installation: jupyter-core 4.10.0
        Uninstalling jupyter-core-4.10.0:
          Successfully uninstalled jupyter-core-4.10.0
      Attempting uninstall: jedi
        Found existing installation: jedi 0.17.2
        Uninstalling jedi-0.17.2:
          Successfully uninstalled jedi-0.17.2
      Attempting uninstall: importlib-resources
        Found existing installation: importlib-resources 5.7.1
        Uninstalling importlib-resources-5.7.1:
          Successfully uninstalled importlib-resources-5.7.1
      Attempting uninstall: importlib-metadata
        Found existing installation: importlib-metadata 4.11.3
        Uninstalling importlib-metadata-4.11.3:
          Successfully uninstalled importlib-metadata-4.11.3
      Attempting uninstall: h5py
        Found existing installation: h5py 3.6.0
        Uninstalling h5py-3.6.0:
          Successfully uninstalled h5py-3.6.0
      Attempting uninstall: grpcio
        Found existing installation: grpcio 1.46.1
        Uninstalling grpcio-1.46.1:
          Successfully uninstalled grpcio-1.46.1
      Attempting uninstall: google-auth
        Found existing installation: google-auth 2.6.6
        Uninstalling google-auth-2.6.6:
          Successfully uninstalled google-auth-2.6.6
      Attempting uninstall: bleach
        Found existing installation: bleach 5.0.0
        Uninstalling bleach-5.0.0:
          Successfully uninstalled bleach-5.0.0
      Attempting uninstall: stack-data
        Found existing installation: stack-data 0.2.0
        Uninstalling stack-data-0.2.0:
          Successfully uninstalled stack-data-0.2.0
      Attempting uninstall: scikit-learn
        Found existing installation: scikit-learn 0.24.1
        Uninstalling scikit-learn-0.24.1:
          Successfully uninstalled scikit-learn-0.24.1
      Attempting uninstall: markdown
        Found existing installation: Markdown 3.3.7
        Uninstalling Markdown-3.3.7:
          Successfully uninstalled Markdown-3.3.7
      Attempting uninstall: jupyter-client
        Found existing installation: jupyter-client 7.3.1
        Uninstalling jupyter-client-7.3.1:
          Successfully uninstalled jupyter-client-7.3.1
      Attempting uninstall: jsonschema
        Found existing installation: jsonschema 4.5.1
        Uninstalling jsonschema-4.5.1:
          Successfully uninstalled jsonschema-4.5.1
      Attempting uninstall: botocore
        Found existing installation: botocore 1.19.63
        Uninstalling botocore-1.19.63:
          Successfully uninstalled botocore-1.19.63
      Attempting uninstall: s3transfer
        Found existing installation: s3transfer 0.3.7
        Uninstalling s3transfer-0.3.7:
          Successfully uninstalled s3transfer-0.3.7
      Attempting uninstall: nbformat
        Found existing installation: nbformat 4.4.0
        Uninstalling nbformat-4.4.0:
          Successfully uninstalled nbformat-4.4.0
      Attempting uninstall: ipython
        Found existing installation: ipython 8.3.0
        Uninstalling ipython-8.3.0:
          Successfully uninstalled ipython-8.3.0
      Attempting uninstall: tensorboard
        Found existing installation: tensorboard 2.9.0
        Uninstalling tensorboard-2.9.0:
          Successfully uninstalled tensorboard-2.9.0
      Attempting uninstall: nbclient
        Found existing installation: nbclient 0.6.3
        Uninstalling nbclient-0.6.3:
          Successfully uninstalled nbclient-0.6.3
      Attempting uninstall: ipykernel
        Found existing installation: ipykernel 5.1.1
        Uninstalling ipykernel-5.1.1:
          Successfully uninstalled ipykernel-5.1.1
      Attempting uninstall: boto3
        Found existing installation: boto3 1.16.63
        Uninstalling boto3-1.16.63:
          Successfully uninstalled boto3-1.16.63
      Attempting uninstall: tensorflow
        Found existing installation: tensorflow 2.7.2
        Uninstalling tensorflow-2.7.2:
          Successfully uninstalled tensorflow-2.7.2
      Attempting uninstall: notebook
        Found existing installation: notebook 6.4.11
        Uninstalling notebook-6.4.11:
          Successfully uninstalled notebook-6.4.11
    Successfully installed absl-py-1.2.0 albumentations-1.2.1 alembic-1.8.1 antlr4-python3-runtime-4.9.3 autopage-0.5.1 bleach-5.0.1 boto3-1.24.34 botocore-1.27.34 cachetools-5.2.0 certifi-2022.6.15 cffi-1.15.1 charset-normalizer-2.1.0 cliff-3.10.1 cloudpickle-2.1.0 cmaes-0.8.2 cmd2-2.4.2 colorlog-6.6.0 debugpy-1.6.2 dm-tree-0.1.7 fastjsonschema-2.16.1 fonttools-4.34.4 gast-0.5.3 google-auth-2.9.1 greenlet-1.1.2 grpcio-1.47.0 h5py-3.7.0 hydra-core-1.2.0 idna-3.3 imageio-2.19.5 importlib-metadata-4.12.0 importlib-resources-5.8.0 ipykernel-6.15.1 ipython-8.4.0 jedi-0.18.1 jmespath-1.0.1 jsonschema-4.7.2 jupyter-client-7.3.4 jupyter-core-4.11.1 keras-2.8.0 kiwisolver-1.4.4 mako-1.2.1 markdown-3.4.1 nbclient-0.6.6 nbformat-5.4.0 networkx-2.8.5 notebook-6.4.12 numpy-1.23.1 omegaconf-2.2.2 opencv-python-headless-4.6.0.66 optuna-2.10.1 pandas-1.4.3 parso-0.8.3 pbr-5.9.0 pdoc3-0.10.0 pillow-9.2.0 prettytable-3.3.0 prompt-toolkit-3.0.30 protobuf-3.20.0 psutil-5.9.1 pyarrow-8.0.0 pyperclip-1.8.2 pytz-2022.1 pywavelets-1.3.0 pyyaml-6.0 pyzmq-23.2.0 qudida-0.0.4 requests-2.28.1 rsa-4.9 s3transfer-0.6.0 scikit-image-0.19.3 scikit-learn-1.1.1 setuptools-63.2.0 six-1.16.0 sklearn-0.0 sqlalchemy-1.4.39 stack-data-0.3.0 stevedore-4.0.0 tensorboard-2.8.0 tensorflow-2.8.0 tensorflow-io-gcs-filesystem-0.26.0 tensorflow-probability-0.16.0 tf-estimator-nightly-2.8.0.dev2021122109 tifffile-2022.5.4 tornado-6.2 traitlets-5.3.0 typing-extensions-4.3.0 urllib3-1.26.10 wheel-0.37.1 zipp-3.8.1
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m[33mWARNING: There was an error checking the latest version of pip.[0m[33m
    [0m


```python
import os
from pathlib import Path

if os.getenv("ENVIRONMENT_NAME") != "local":
    os.chdir(Path().resolve().parent)

if os.getenv("ENVIRONMENT_NAME") == "local":
    os.environ["AWS_PROFILE"] = "datascience"
```


```python
print("Current working directory (should be equal to the project root path):", os.getcwd())
```


```python
import src
```


```python
########################################################
# USE THIS CODE ALWAYS AS FIRST CELL IN YOUR NOTEBOOKS #
########################################################

# DO NOT MODIFY THIS CODE
import sys
from pathlib import Path
sys.path.insert(0,str(Path(os.getcwd()).resolve()))
import os

from car_azimuth_predictor.config import load_config
load_config()
from car_azimuth_predictor.config import current_config

########################################################
```


```python
# TODO: Add your code here
```


```python
from car_azimuth_predictor.data_gathering import collect_data

collect_data(current_config)
```


```python
from car_azimuth_predictor.feature_generation import generate_features

generate_features(current_config)
```


```python
from car_azimuth_predictor.split_dataset import split_dataset

split_dataset(current_config)
```

## Approach 1
Output 2 variables (sin, cos), MSE loss 


```python
import tensorflow as tf

from src.utils.training_tools import (
    tf_mean_absolute_angle_error_sin_cos_output,
    tf_rmse_angle_sin_cos_output,
    tf_r2_angle_score_sin_cos_output,
    tf_median_absolute_angle_error_sin_cos_output,
    tf_acc_pi_6_sin_cos_output,
    horizontal_flip_pose_sin_cos_output
)
```


```python
from src.dataset_generation import generate_datasets

gt_cols = ['azimuth_sin', 'azimuth_cos']
train_dataset, validation_dataset, test_dataset = generate_datasets(current_config, gt_cols=gt_cols, pose_flip_fn=horizontal_flip_pose_sin_cos_output)
```


```python
input_layer = tf.keras.layers.Input(shape=(1280,))

mlp_middle = tf.keras.layers.Dense(32, activation='relu', name='mlp_middle')(input_layer)
mlp_output = tf.keras.layers.Dense(2, activation='tanh', name='mlp_output')(mlp_middle)

bottom = tf.keras.models.Model(inputs=input_layer, outputs=mlp_output)
```


```python
from src.model_generation import generate_model

model = generate_model(current_config, bottom=bottom)
```


```python
model.summary()
```


```python
loss = tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error")
metrics=[
    tf_mean_absolute_angle_error_sin_cos_output,
    tf_rmse_angle_sin_cos_output,
    tf_r2_angle_score_sin_cos_output,
    tf_median_absolute_angle_error_sin_cos_output,
    tf_acc_pi_6_sin_cos_output
]
optimizer = tf.keras.optimizers.Adamax(learning_rate=0.001)
```


```python
from src.train_model import train_model

train_history, current_datetime_strgfied = train_model(current_config, model=model, train_dataset=train_dataset, validation_dataset=validation_dataset, optimizer=optimizer, loss=loss, metrics=metrics, persist_train_history=True)
```


```python
from src.plot_training_curves import plot_training_curves

plot_training_curves(train_history, "Training curves - Approach 1. MeanSquaredError")
```


```python
from src.evaluate_model import evaluate_model
import tensorflow_hub as hub

custom_objects = {
    "KerasLayer": hub.KerasLayer,
    "tf_mean_absolute_angle_error_sin_cos_output": tf_mean_absolute_angle_error_sin_cos_output,
    "tf_rmse_angle_sin_cos_output": tf_rmse_angle_sin_cos_output,
    "tf_r2_angle_score_sin_cos_output": tf_r2_angle_score_sin_cos_output,
    "tf_median_absolute_angle_error_sin_cos_output": tf_median_absolute_angle_error_sin_cos_output,
    "tf_acc_pi_6_sin_cos_output": tf_acc_pi_6_sin_cos_output
}

current_datetime_strgfied = "20220715-093435"
evaluate_model(current_config, current_datetime_strgfied, 36, test_dataset, custom_objects)
```

## Approach 2
Output 2 variables (sin, cos), Cosine Similarity loss 


```python
import tensorflow as tf

from src.utils.training_tools import (
    tf_mean_absolute_angle_error_sin_cos_output,
    tf_rmse_angle_sin_cos_output,
    tf_r2_angle_score_sin_cos_output,
    tf_median_absolute_angle_error_sin_cos_output,
    tf_acc_pi_6_sin_cos_output,
    horizontal_flip_pose_sin_cos_output
)
from src.dataset_generation import generate_datasets

gt_cols = ['azimuth_sin', 'azimuth_cos']
train_dataset, validation_dataset, test_dataset = generate_datasets(current_config, gt_cols=gt_cols, pose_flip_fn=horizontal_flip_pose_sin_cos_output)
input_layer = tf.keras.layers.Input(shape=(1280,))

mlp_middle = tf.keras.layers.Dense(32, activation='relu', name='mlp_middle')(input_layer)
mlp_output = tf.keras.layers.Dense(2, activation='tanh', name='mlp_output')(mlp_middle)

bottom = tf.keras.models.Model(inputs=input_layer, outputs=mlp_output)
```


```python
from src.model_generation import generate_model

model = generate_model(current_config, bottom=bottom)
```


```python
loss = tf.keras.losses.CosineSimilarity()
metrics = [
    tf_mean_absolute_angle_error_sin_cos_output,
    tf_rmse_angle_sin_cos_output,
    tf_r2_angle_score_sin_cos_output,
    tf_median_absolute_angle_error_sin_cos_output,
    tf_acc_pi_6_sin_cos_output
]
optimizer = tf.keras.optimizers.Adamax(learning_rate=0.001)
```


```python
from src.train_model import train_model

train_history, current_datetime_strgfied = train_model(current_config, model=model, train_dataset=train_dataset,
                                           validation_dataset=validation_dataset, optimizer=optimizer, loss=loss,
                                           metrics=metrics, persist_train_history=True)
```


```python
from src.plot_training_curves import plot_training_curves

plot_training_curves(train_history, "Training curves - Approach 2. CosineSimilarity")
```


```python
from src.evaluate_model import evaluate_model
import tensorflow_hub as hub
custom_objects = {
    "KerasLayer": hub.KerasLayer,
    "tf_mean_absolute_angle_error_sin_cos_output": tf_mean_absolute_angle_error_sin_cos_output,
    "tf_rmse_angle_sin_cos_output": tf_rmse_angle_sin_cos_output,
    "tf_r2_angle_score_sin_cos_output": tf_r2_angle_score_sin_cos_output,
    "tf_median_absolute_angle_error_sin_cos_output": tf_median_absolute_angle_error_sin_cos_output,
    "tf_acc_pi_6_sin_cos_output": tf_acc_pi_6_sin_cos_output
}

current_datetime_strgfied = "20220715-095559"
evaluate_model(current_config, current_datetime_strgfied, 8, test_dataset, custom_objects=custom_objects)
```

## Approach 3
Output 2 variable (angle from 0 to pi, angle from pi/2 to 3/2 pi), Custom crossentropy loss


```python
import tensorflow as tf
input_layer = tf.keras.layers.Input(shape=(1280,))

mlp_middle = tf.keras.layers.Dense(
    32, activation="relu", name="mlp_middle"
)(input_layer)

angle1_sigmoid_output = tf.keras.layers.Dense(
    1, activation="sigmoid", name="angle1_output"
)(mlp_middle)
angle2_sigmoid_output = tf.keras.layers.Dense(
    1, activation="sigmoid", name="angle2_output"
)(mlp_middle)

# concatenate two together
angle_concatenated = tf.keras.layers.Concatenate(
    axis=1, name="concatenate_angles_2_vars"
)([angle1_sigmoid_output, angle2_sigmoid_output])

bottom = tf.keras.models.Model(inputs=input_layer, outputs=angle_concatenated)
```


```python
from src.model_generation import generate_model

model = generate_model(current_config, bottom=bottom)
```


```python
from src.dataset_generation import generate_datasets
from src.utils.training_tools import (
    angle_double_output_loss,
    tf_acc_pi_6_double_sigmoid,
    tf_mean_absolute_angle_error_double_sigmoid,
    tf_median_absolute_angle_error_double_sigmoid,
    tf_r2_angle_score_double_sigmoid,
    tf_rmse_angle_score_double_sigmoid,
    horizontal_flip_pose_double_sigmoid
)

gt_cols = ['azimuth_norm_abs', 'azimuth_radians_shifted_0.5_pi_norm_abs']
train_dataset, validation_dataset, test_dataset = generate_datasets(current_config, gt_cols=gt_cols, pose_flip_fn=horizontal_flip_pose_double_sigmoid)
```


```python

optimizer = tf.keras.optimizers.Adamax(learning_rate=0.001)
loss = angle_double_output_loss
metrics = [
    tf_mean_absolute_angle_error_double_sigmoid,
    tf_median_absolute_angle_error_double_sigmoid,
    tf_r2_angle_score_double_sigmoid,
    tf_rmse_angle_score_double_sigmoid,
    tf_acc_pi_6_double_sigmoid,
]
```


```python
from src.train_model import train_model

train_history, current_datetime_strgfied = train_model(current_config, model=model, train_dataset=train_dataset, validation_dataset=validation_dataset, optimizer=optimizer, loss=loss, metrics=metrics)
```


```python
import json

histories_path = "/root/car-azimuth-predictor-experimentation/training_histories"
os.makedirs(histories_path, exist_ok=True)
with open(os.path.join(histories_path, "approach_3_patience10.json"), "w") as fp:
    json.dump(train_history.history, fp)
```


```python
from src.plot_training_curves import plot_training_curves
import json

history_path = "/root/car-azimuth-predictor-experimentation/training_histories/approach_3.json"
with open(history_path, "r") as fp:
    train_history = json.load(fp)
plot_training_curves(train_history, "Training curves - Approach 3. DoubleBinaryCrossentropy")
```


```python
from src.evaluate_model import evaluate_model
import tensorflow_hub as hub

custom_objects = {
    "KerasLayer": hub.KerasLayer,
    "angle_double_output_loss": angle_double_output_loss,
    "tf_mean_absolute_angle_error_double_sigmoid": tf_mean_absolute_angle_error_double_sigmoid,
    "tf_rmse_angle_score_double_sigmoid": tf_rmse_angle_score_double_sigmoid,
    "tf_r2_angle_score_double_sigmoid": tf_r2_angle_score_double_sigmoid,
    "tf_median_absolute_angle_error_double_sigmoid": tf_median_absolute_angle_error_double_sigmoid,
    "tf_acc_pi_6_double_sigmoid": tf_acc_pi_6_double_sigmoid
}

current_datetime_strgfied = "20220715-101105"
model, _ = evaluate_model(current_config, current_datetime_strgfied, 12, test_dataset, custom_objects=custom_objects)
```


```python
len(os.listdir("/root/car-azimuth-predictor-experimentation/data/raw/PASCAL3D+_release1.1/Images/car_imagenet"))
```


```python
from src.visualize import visualize_predictions

visualize_predictions(model, test_dataset)
```

## Random experimentations and plots


```python
import requests
import io
import tempfile
import matplotlib.pyplot as plt
import math
from PIL import Image
import numpy as np
from tensorflow.keras.applications.efficientnet_v2 import (
    preprocess_input as preprocess_input_effnet,
)
from src.utils.training_tools import np_get_angle_from_double_sigmoids
from src.utils.visualization_tools import plot_image_from_path


urls = [
    'https://upload.wikimedia.org/wikipedia/commons/6/6b/Fiat_Panda_1.2_8V_Lounge_%28III%29_%E2%80%93_Frontansicht_%281%29%2C_25._Februar_2012%2C_D%C3%BCsseldorf.jpg',
    'https://prod.pictures.autoscout24.net/listing-images/6bfcbee3-287c-c936-e043-1250030acba4_8fc165c2-c4ac-4b7e-839d-d8493643d946.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/3802d738-e48b-4d83-8591-91909d46364c_a62d9238-0abf-459e-bf5e-adb0adbf518c.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/3802d738-e48b-4d83-8591-91909d46364c_c42ff950-03eb-4453-b05f-66712e334045.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/7c46ed9c-2a35-4a0d-9cb4-dd580ab3a06a_76e97c5d-bc23-4e32-bd82-1faf05820772.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/5d998939-3d32-4f30-ba6a-0b7be9b7417e_9b2ada8b-83d7-4e60-8372-6caf4f773e28.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/91cd3f2d-ad89-4d9a-ab62-29a575fd3403_6211ebb0-6a30-44f7-9281-85d9396c6057.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/91cd3f2d-ad89-4d9a-ab62-29a575fd3403_2be35d4c-b029-4a8e-a051-b4bf98d5c6d8.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/91cd3f2d-ad89-4d9a-ab62-29a575fd3403_1ebcd7cc-c2e1-4f12-91a1-4e569d4fe723.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/8bc04ac1-b48c-4c21-9cd5-7f7f2c9d0fcd_00b68deb-3f96-44c8-bcf0-6e6c55ad2135.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/83af03db-5170-4778-8ab8-13a7d3dbf31a_986b9ca3-adda-44a9-84d6-9c35d09fcc6e.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/83af03db-5170-4778-8ab8-13a7d3dbf31a_bf251591-e5e3-4c57-9fdd-53c9ce10ee96.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/83af03db-5170-4778-8ab8-13a7d3dbf31a_62a1aee8-a4f9-400d-b343-889df15fe389.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/e74fc24f-2f2b-4219-812f-2fa43dc2e923_2c1f525f-2ecc-4bef-aae8-0c9ad8e650f4.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/e74fc24f-2f2b-4219-812f-2fa43dc2e923_a267a0c3-7672-4088-ac68-c26c7f429f82.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/677f431e-7478-4828-9cca-f6c4d9ae96f1_079d9bb9-8093-4e11-a991-873be527cbe8.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/e31139cf-5c92-4cd4-82e9-0fcd530c94f7_34c8865c-0465-4450-aa7b-41faf53826e5.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/b65fc27b-ad27-4e66-ace1-ac2742464eca_9e7e66db-adef-493b-a472-e402cc918685.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/f12d0232-111f-4887-a9eb-112f91c3efe5_5fe3939e-b81b-4f18-a4d3-ee7b5858dbfc.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/f12d0232-111f-4887-a9eb-112f91c3efe5_870664b6-23aa-464d-b481-9f6ec883fca8.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/8f5ac529-c8f4-408d-a3ac-664e967bf409_2b4dceb9-7d45-44c1-876e-5aecbb51dad7.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/8069a9b0-e78e-4cba-8e37-76437312534a_e563f624-0e7f-4d6e-9331-1edcf100b548.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/e8d79a2d-057f-45f3-a231-c17662d1175a_07c7315f-03a2-45f4-9fcb-7d8e6424e8dc.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/c939465c-7cfe-4ff2-b062-6ebff742c163_0d7c9145-33a5-4b21-be67-5d3e585a6148.jpg/720x540.webp',
    'https://prod.pictures.autoscout24.net/listing-images/62d6b64c-63ea-4fcf-b813-83945cb525f0_99254a7d-d4b0-4476-b683-78704a01cf8f.jpg/720x540.webp'

]

plt.figure(figsize=(24, 24))
square_size = int(math.ceil(math.sqrt(len(urls))))

for i, url in enumerate(urls):
    with tempfile.NamedTemporaryFile() as fp:

        res = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}, stream=True)
        fp.write(res.raw.read())

        # virt_file.seek(0)
        img = Image.open(fp.name)
        img = img.resize([224, 224])
        img.save(fp.name + '.resized.jpg')


        X = np.array([preprocess_input_effnet(np.array(img))])

        y_pred = model.predict(X)

        # print(y_pred.shape)

        y_pred_degrees = np_get_angle_from_double_sigmoids(y_pred) / np.pi * 180


        # y_pred_angle = np.arctan2(y_pred[:, 0], y_pred[:, 1]) / math.pi * 180

        plt.subplot(square_size, square_size, i + 1)
        plot_image_from_path(fp.name + '.resized.jpg', float(y_pred_degrees[0]))
```


```python

```
