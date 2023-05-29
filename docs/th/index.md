# Fenv (เฟนวี)

Fenv เป็นเครื่องมือที่ง่ายและมีประสิทธิภาพที่จะช่วยคุณจัดการสภาพแวดล้อมเสมือนและสร้างไฟล์ Python พื้นฐานด้วยคำสั่งเดียว ด้วย Fenv คุณสามารถสร้างโฟลเดอร์โปรเจ็กต์ใหม่ได้อย่างรวดเร็ว สร้างสภาพแวดล้อมเสมือนภายในโฟลเดอร์นั้น และสร้างไฟล์ Python พื้นฐานที่จำเป็นพร้อมกันได้ในคราวเดียว เครื่องมือนี้เหมาะสำหรับนักพัฒนาที่ทำงานในโครงการ Python หลายโครงการบ่อยๆ และต้องการวิธีการที่เรียบง่ายและมีประสิทธิภาพสำหรับการจัดการสภาพแวดล้อมเสมือนจริง

## คุณสมบัติ

- สร้างโฟลเดอร์โครงการใหม่ด้วยคำสั่งเดียว
- สร้างสภาพแวดล้อมเสมือนอย่างรวดเร็วภายในโฟลเดอร์โครงการ
- สร้างไฟล์ Python พื้นฐานที่จำเป็นพร้อมกัน
- เหมาะสำหรับนักพัฒนาที่ทำงานในโครงการ Python หลายโครงการ
- เพิ่ม `black` สำหรับจัดการรูปแบบ python
- แพ็คเกจสามารถติดตั้งและถอนการติดตั้งและเพิ่มลงในไฟล์ `requirements.txt` พร้อมๆกันในเวลาเดียวกัน

## ติดตั้ง

```
pip install fenv
```

or

```
pip install --upgrade fenv
```

## คำสั่ง

```cmd
$ fenv -h

Usage:
  fenv [options] <command>

Commands:

    new       Create a new project
    install   Install packages
    uninstall Uninstall packages
    update    Update packages to file requirements.txt
    env   Create only virtualenv and no create base file

General Options:
  -h, --help  Show this help message and exit

```

## โครงสร้าง

    |_ .vscode/
    |    |_ settings.json
    |
    |_ env_name/
    |    |_ Lib
    |    |_ Scripts
    |    |_ .gitignore
    |    |_ pyvenv
    |
    |_ main.py
    |_ readme.md
    |_ requirements.txt

## การติดตั้ง

ในการติดตั้ง Fenv เพียงเรียกใช้คำสั่งต่อไปนี้:

```sh
pip install fenv
```

## การใช้งาน

Fenv ช่วยให้การเริ่มต้นโครงการ Python ใหม่เป็นเรื่องง่ายด้วยการจัดเตรียมโซลูชันแบบ all-in-one นี่คือวิธีการใช้งาน:

## สร้างโฟลเดอร์โครงการใหม่พร้อม virtualenv และไฟล์พื้นฐาน:

```sh
fenv new <project_folder>
```

## เปิดใช้งานสภาพแวดล้อมเสมือนจริง:

### for windows

```
cd project_folder
source env/bin/activate
```

### for linux

```
cd project_folder
source env/bin/activate
```

# คำสั่งสำหรับ Windows เท่านั้น

## ติดตั้งแพ็คเกจ

```
fenv install <package_name>
```

ติดตั้งแพ็คเกจและเพิ่มลงใน requirement.txt หากไม่ใส่ชื่อแพ็คเกจ ข้อความ `Maybe you forgot to put the name of the package to install? for example fenv install <package_name>` จะปรากฏขึ้น

## ถอนการติดตั้งแพ็คเกจ

```
fenv uninstall <package_name>
```

ถอนการติดตั้งแพ็คเกจและลบออกจาก requirement.txt

## อัปเดต requirements.txt

```
fenv update <package_name>
```

อัปเดตแพ็คเกจทั้งหมดลงในไฟล์ requirement.txt

## สร้างแค่ virtualenv เท่านั้น

```
fenv env
```

สร้าง virtualenv ด้วยชื่อที่กำหนดเองหรือชื่ออัตโนมัติ 2 ตัวเลือก จากนั้นสร้างไฟล์ settings.json สำหรับ vscode ไม่ได้สร้างไฟล์พื้นฐานเพิ่มให้
