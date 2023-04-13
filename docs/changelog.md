### 0.0.12.2

- [x] Add command `fenv clone <git url>` [](https://github.com/watchakorn-18k/Fenv/issues/7) ![](https://i.imgur.com/fGizSeu.gif)
- [x] Optimize code to match case

### 0.0.12.1

- [x] Remove `fenv deactivate` from [pull/6](https://github.com/watchakorn-18k/Fenv/pull/6/files#diff-c8c31647a371f705e0fe45e4a3091400d282af4643adb128636378717392a79d) @yassine20011
- [x] Clean code [env_all.py](https://github.com/watchakorn-18k/Fenv/pull/6/files#diff-75263248e3c88543bbd5e52333f6d3bf4cdfe36cb3e0c685bf65aa0f77829820) , [manage_file.py](https://github.com/watchakorn-18k/Fenv/pull/6/files#diff-b2587f7f2faf4e65b162d52ab45a8f0facefc0485718cadc198a3a064ab1ce48) @yassine20011
- [x] Fix in file `state_env.py` [pull/6](https://github.com/watchakorn-18k/Fenv/pull/6/files#diff-0cb3f6829c4ad490de31b6b38b7cb0885596892ec2d578f045828acb3e13f1e2) @yassine20011

### 0.0.12.0

- [x] An improved string using f-string format @yassine20011 [pull/5/files](https://github.com/watchakorn-18k/Fenv/pull/5/files)
- [x] Add installation instructions for Windows users using pipx @yassine20011 [pull/5/files](https://github.com/watchakorn-18k/Fenv/pull/5/files)

### 0.0.11.9

- [x] Add command more `fenv deactivate` Command hint to deactivate virtual environment with folder
- [x] Add command more `fenv activate` Command hint to activate virtual environment with folder
      ![](https://i.imgur.com/H7MURw3.gif)

### 0.0.11.8

- Fix error ModuleNotFoundError: No module named 'dotenv' and not show version fenv

### 0.0.11.7

- [x] `fenv uninstall <package>` can remove packages and package dependencies all in one Tested [Windows]
  - before ![](https://i.imgur.com/2zRW1xY.gif)
  - after ![](https://i.imgur.com/oZ7LMN9.gif)
- [x] Add command `fenv clean` to clean packages left lib basic files pass test [Windows] and [Linux] ![](https://i.imgur.com/QPkGn0F.gif)
- [x] Added fev.cfg file
- [x] Support command all in Linux

### 0.0.11.6

- [x] Fix bug create readme.md change `env_directory()` to `name`

### 0.0.11.5

- [x] Added Tree path in md after generating projects , can you try command `fenv update` ![](https://i.imgur.com/vDz2Gs0.gif)
- [x] Added create file .gitignore
- [x] Edit readme.md small changes
- [x] Fix if an `env` folder does not exist, the modified `fenv install <packages>` command will prompt you to confirm whether you would like to create a new `env`. If you choose not to create a new `env`, the installation will proceed using `python main` ![](https://i.imgur.com/M0shh8x.gif)
- [x] Added command `fenv install` alone will install file requirements.txt in directory current ![](https://i.imgur.com/cgApbCa.gif)
- [x] Added after use `fenv onlyenv` created settings then activate env one time ![](https://i.imgur.com/mwEUSrg.gif)

### 0.0.11.4

- [x] Fix bugs small

### 0.0.11.3

- [x] Fix bugs settings in .vscode
- [x] Fix bugs line 609 and 624

### 0.0.11.2

- [x] Fix bugs small

### 0.0.11.1

- [x] Change new pattern command `-onlyenv` to `onlyenv`

### 0.0.10

- [x] Add option `-onlyenv` for create only virtualenv without base file all
- [x] Add command install for install package and add module to file requirements.txt

### 0.0.9

- [x] Release 0.0.9
