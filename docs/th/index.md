# Fenv (เฟนวี)

Fenv เป็นเครื่องมือที่ง่ายและมีประสิทธิภาพที่จะช่วยคุณจัดการสภาพแวดล้อมเสมือนและสร้างไฟล์ Python พื้นฐานด้วยคำสั่งเดียว ด้วย Fenv คุณสามารถสร้างโฟลเดอร์โปรเจ็กต์ใหม่ได้อย่างรวดเร็ว สร้างสภาพแวดล้อมเสมือนภายในโฟลเดอร์นั้น และสร้างไฟล์ Python พื้นฐานที่จำเป็นพร้อมกันได้ในคราวเดียว เครื่องมือนี้เหมาะสำหรับนักพัฒนาที่ทำงานในโครงการ Python หลายโครงการบ่อยๆ และต้องการวิธีการที่เรียบง่ายและมีประสิทธิภาพสำหรับการจัดการสภาพแวดล้อมเสมือนจริง

## คุณสมบัติ

- สร้างโฟลเดอร์โครงการใหม่ด้วยคำสั่งเดียว
- สร้างสภาพแวดล้อมเสมือนอย่างรวดเร็วภายในโฟลเดอร์โครงการ
- สร้างไฟล์ Python พื้นฐานที่จำเป็นพร้อมกัน
- เหมาะสำหรับนักพัฒนาที่ทำงานในโครงการ Python หลายโครงการ
- เพิ่ม `black` สำหรับจัดการรูปแบบ python
- แพ็คเกจสามารถติดตั้งและถอนการติดตั้งและเพิ่มลงในไฟล์ `requirements.txt` พร้อมๆกันในเวลาเดียวกัน

## Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
